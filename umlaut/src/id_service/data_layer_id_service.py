from abc import ABC, abstractmethod
from dataclasses import dataclass

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
class DataLayerIdService(IdService[ParentIdentifier]):
    data_layer: DataLayer

    def get_id(self, class_identifier: ParentIdentifier) -> Id:
        # HACK the id_counter in the metadata file is 1000% not atomic, not sure how to fix right now

        metadata = self.data_layer.load_metadata(
            class_identifier.get_parent_identifier())

        if metadata and 'id_service' in metadata:
            id_counter = metadata['id_service']['id_counter']
            self.data_layer.update_metadata(class_identifier.get_parent_identifier(), {
                "id_service": {"id_counter": id_counter+1}})
            return id_counter
        else:
            # NOTE This might be redundant, with the defaults of Metadata.py
            id_counter = 1
            self.data_layer.update_metadata(class_identifier.get_parent_identifier(), {
                "id_service": {"id_counter": id_counter}})

            return id_counter
