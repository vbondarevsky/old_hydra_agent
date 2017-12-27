from hydra_agent.rac.infobase_manager.infobase import InfoBase

raw = 'infobase : 4a824148-db94-11e7-7b82-000d3a2c0d8b\nname     : test_acc\ndescr    : \n\n'


def test_create_from_string():
    ib = InfoBase(raw=raw)
    assert ib.id == '4a824148-db94-11e7-7b82-000d3a2c0d8b'
    assert ib.name == 'test_acc'
    assert ib.description == ''


def test_create_from_id():
    ib = InfoBase(id='4a824148-db94-11e7-7b82-000d3a2c0d8b\n')
    assert ib.id == '4a824148-db94-11e7-7b82-000d3a2c0d8b'
