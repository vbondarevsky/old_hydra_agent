from .settings import settings
from .v8 import V8
from .rac import Rac
from .ring import Ring
from .mssql import Mssql
from .postgre import Postgre

v8 = V8(settings.v8)
rac = Rac(settings.rac)
ring = Ring(settings.ring)
db = Postgre(settings.db)