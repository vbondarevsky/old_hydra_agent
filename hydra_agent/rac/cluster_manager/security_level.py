from enum import IntEnum


class SecurityLevel(IntEnum):
    InsecureConnection = 0
    ProtectedConnectionOnlyDuringAdminAuthentication = 1
    ProtectedConnectionDuringEntireSession = 2
