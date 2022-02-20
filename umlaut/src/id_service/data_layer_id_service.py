from dataclasses import dataclass
from id_service.id_service import IdService
from data_layer.data_layer import DataLayer


@dataclass(frozen=True)
class DataLayerIdService(IdService):
    data_layer: DataLayer

    def getId(self):
        pass
