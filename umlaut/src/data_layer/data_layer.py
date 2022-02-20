from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from data_layer.metadata import ScrapeMetada

# TODO This one needs to be abstracted to it's own package separate from the scraper, since it will be needed in several places

# NOTE Should this type be something like "UmlautIdentifier" if it's needed to be used outside of the DataLayer (to show that it's used more generally)
DataLayerIdentifier = str


def toDataLayerIdentifier(strings: list[str]) -> DataLayerIdentifier:
    return "::".join(map(lambda x: x.upper(), strings))


def appendDataLayerIdentifier(identifier: DataLayerIdentifier, *args: str) -> DataLayerIdentifier:
    return "::".join([identifier] + list(args))


@ dataclass(frozen=True)
class DataLayer(ABC):

    # NOTE don't know if I can constrain the object type more
    @ staticmethod
    @ abstractmethod
    def save(data_layer_identifier: DataLayerIdentifier, data: Any) -> None:
        raise NotImplementedError

    @ staticmethod
    @ abstractmethod
    def load(data_layer_identifier: DataLayerIdentifier) -> Any:
        raise NotImplementedError

    @ staticmethod
    @ abstractmethod
    def load_metadata(data_layer_identifier: DataLayerIdentifier) -> ScrapeMetada:
        raise NotImplementedError

    @ staticmethod
    @ abstractmethod
    # Here we could be cool and type the metadata
    def update_metadata(data_layer_identifier: DataLayerIdentifier, update: ScrapeMetada) -> None:
        raise NotImplementedError
