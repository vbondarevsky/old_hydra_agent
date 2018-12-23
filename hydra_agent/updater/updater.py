# This file is part of HYDRA - cross-platform remote administration
# system for 1C:Enterprise (https://github.com/vbondarevsky/hydra_agent).
# Copyright (C) 2017  Vladimir Bondarevskiy.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os.path
import urllib.parse
import xml.etree
from distutils.version import LooseVersion

import aiohttp
import networkx


class Updater:

    def __init__(self, url, vendor, configuration, version, user, password, path):
        self.url = url
        self.vendor = vendor
        self.configuration = configuration
        self.version = LooseVersion(version)
        self.user = user
        self.password = password
        self.path = path
        self.chunk_size = 1024

    async def download_updates(self, updates):
        for update in updates:
            update_file = os.path.join(self.path, update["file"])
            if not os.path.exists(update_file):
                if not os.path.exists(os.path.dirname(update_file)):
                    os.makedirs(os.path.dirname(update_file))
                print("download: " + update["file"])
                with open(update_file, "wb") as f:
                    url = urllib.parse.urljoin(self.url, update["file"])
                    async for chunk in self._read_from_url(url):
                        f.write(chunk)

    async def build_updates_sequence(self):
        max_version = self.version

        graph = networkx.Graph()

        updates = {}
        async for update in self._read_update_element():
            if update["vendor"] != self.vendor or LooseVersion(update["version"]) < self.version:
                continue
            max_version = max(max_version, LooseVersion(update["version"]))
            for target in update["target"]:
                if target >= self.version:
                    graph.add_node(target, weight=self._convert_to_integer(target))
                    graph.add_node(update["version"], weight=self._convert_to_integer(update["version"]))
                    graph.add_edge(target, update["version"])
                    updates[update["version"]] = update
        update_seq = []
        for node in networkx.shortest_path(graph, str(self.version), str(max_version), weight="weight")[1:]:
            update_seq.append(updates[node])
        return update_seq

    async def _read_update_element(self):
        can_read_update = False
        async for event, element in self._read_xml_from_url():
            tag = element.tag.replace("{http://v8.1c.ru/configuration-updates}", "")
            if event == "start" and tag == "update":
                if element.attrib["configuration"] != self.configuration:
                    continue
                can_read_update = True
                update = {
                    "configuration": element.attrib["configuration"],
                    "vendor": "",
                    "version": "",
                    "platform": "",
                    "size": 0,
                    "target": set(),
                }
                continue
            if event == "end" and tag == "update":
                if can_read_update:
                    yield update
                can_read_update = False

            if can_read_update:
                value = element.text
                if event == "end":
                    if tag == "vendor":
                        update["vendor"] = value
                    elif tag == "file":
                        update["file"] = value
                    elif tag == "size":
                        update["size"] = int(value)
                    elif tag == "version":
                        update["version"] = value
                        update["platform"] = element.attrib.get("platform", "")
                    elif tag == "target":
                        update["target"].add(value)

    async def _read_xml_from_url(self):
        parser = xml.etree.ElementTree.XMLPullParser(["start", "end"])
        url = urllib.parse.urljoin(self.url, "v8cscdsc.xml")
        async for chunk in self._read_from_url(url):
            parser.feed(chunk)
            for event in parser.read_events():
                yield event

    def _create_session(self):
        headers = {"User-Agent": "1C+Enterprise/8.3"}
        auth = aiohttp.BasicAuth(self.user, self.password)
        return aiohttp.ClientSession(headers=headers, auth=auth)

    async def _read_from_url(self, url):
        async with self._create_session() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    async for chunk in response.content.iter_any():
                        yield chunk

    @staticmethod
    def _convert_to_integer(version):
        parts = version.split(".")
        return -sum([int(parts[i]) * 1000 ** (len(parts) - i - 1) for i in range(len(parts))])
