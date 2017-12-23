from os import remove
from os.path import join, exists
from subprocess import run

from hydra_agent.utils import temp_file_name


class V8:
    def __init__(self, config, template=None):
        self.path = join(config['v8']['path'], "1cv8")
        self.template = template

    def create_ib(self, ib):
        log_file = temp_file_name()

        parameters = [
            self._escape(self.path),
            'createinfobase',
            self._escape(self._build_connection_string(ib)),
            '/AddToList', self._escape(ib['name']),
            '/Out', self._escape(log_file),
            '/L', self._escape(ib['locale']),
            '/DisableStartupDialogs', '/DisableStartupMessages'
        ]
        if self.template:
            parameters.append(self._escape(self.template))

        command = ' '.join(parameters)

        try:
            result = run(parameters)
            with open(log_file) as log:
                return result.returncode, log.read()
        except Exception as ex:
            pass
            return 1, str(ex)
        finally:
            if exists(log_file):
                remove(log_file)

        pass
        # TODO: сделать создание ИБ

    def update_cf(self):
        pass
        # TODO: сделать обновление конфигурации

    def update_ib(self):
        pass
        # TODO: сделать обновление конфигурации ИБ

    @staticmethod
    def _build_connection_string(ib):
        connection_string = ''
        parameters = []
        if 'file' in ib:
            parameters.append('File=\'%s\';' % ib['file'])
            parameters.append('Locale=\'%s\';' % ib['locale'])
        else:
            pass

        connection_string = ''.join(parameters)

        return connection_string

    @staticmethod
    def _escape(parameter):
        return '%s' % parameter
