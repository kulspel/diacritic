from abc import ABC, abstractmethod
from dataclasses import dataclass

# TODO This one needs to be abstracted to it's own package separate from the scraper, since it will be needed in several places

# NOTE Should this type be something like "UmlautIdentifier" if it's needed to be used outside of the DataLayer (to show that it's used more generally)
DataLayerIdentifier = str


@dataclass(frozen=True)
class DataLayer(ABC):

    # NOTE don't know if I can constrain the object type more
    @staticmethod
    @abstractmethod
    def save(data_layer_identifier: DataLayerIdentifier, data: object) -> None:
        raise NotImplementedError

    # def load(self, data_layer_identifier: str):
    #    raise NotImplementedError
