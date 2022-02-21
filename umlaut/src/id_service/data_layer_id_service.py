from dataclasses import dataclass

from data_layer.data_layer import DataLayer, DataLayerIdentifier

from id_service.id_service import Id, IdService

# HACK the only reason this import (DataLayer) work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class DataLayerIdService(IdService):
    data_layer: DataLayer

    def get_id(self, class_identifier: DataLayerIdentifier) -> Id:
        # HACK the id_counter in the metadata file is 1000% not atomic, not sure how to fix right now

        metadata = self.data_layer.load_metadata(class_identifier)

        if metadata and 'id_service' in metadata:
            id_counter = metadata['id_service']['id_counter'] + 1
            self.data_layer.update_metadata(
                class_identifier,
                {"id_service": {"id_counter": id_counter}})

            return id_counter
        else:
            # NOTE This might be redundant, with the defaults of Metadata.py
            # NOTE there no longer are any defaults in Metadata.py,
            id_counter = 1
            self.data_layer.update_metadata(
                class_identifier,
                {"id_service": {"id_counter": id_counter}})

            return id_counter
