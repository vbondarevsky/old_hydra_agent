class InfoBase:
    def __init__(self, raw: str = '', id: str = ''):
        if id:
            self.id = id.strip()
        else:
            result = self.__parse(raw)
            self.id = result['infobase']
            self.name = result['name']
            self.description = result['descr']

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __parse(self, raw):
        result = {}
        for i in raw.strip().split('\n'):
            k, v = i.split(':', 1)
            result[k.strip()] = v.strip()
        return result
