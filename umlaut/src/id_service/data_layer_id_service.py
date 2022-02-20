from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from data_layer.data_layer import DataLayer, DataLayerIdentifier

from id_service.id_service import Id, IdService

# HACK the only reason this import (DataLayer) work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class ParentIdentifier(ABC):
    # HACK aren't we super duper coupling our shit with this ParentIdentifier composition design pattern? We are kinda coupling all of our classes to a specific implementation of idService, or is it reasonable to assume that all implementations of IdService would need some ParentIdentifier?

    @staticmethod
    @abstractmethod  # Should this be staic or classmethod?
    def get_parent_identifier() -> DataLayerIdentifier:
        raise NotImplementedError


@dataclass(frozen=True)
class DataLayerIdService(IdService):
    data_layer: DataLayer

    def getId(self, obj: Any) -> Id:
        return 1
