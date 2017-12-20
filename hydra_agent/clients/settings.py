from yaml import load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

settings = load(open('hydra-agent2.yaml'), Loader=Loader)
pass