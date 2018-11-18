from abc import ABC, abstractmethod


class ConnectionString(ABC):

    @property
    def connection_string(self):
        parts = []
        for k, v in self._get_properties().items():
            if getattr(self, k):
                parts.append(f"{v}='{getattr(self, k)}'")
        return ";".join(parts) + ";"

    @abstractmethod
    def _get_properties(self):
        pass

    def __repr__(self):
        return self.connection_string
