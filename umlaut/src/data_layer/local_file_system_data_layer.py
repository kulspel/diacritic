import glob
import json
import os
from typing import Any

from bs4 import BeautifulSoup

from data_layer.data_layer import DataLayer, DataLayerIdentifier
from data_layer.metadata import Metadata, ScrapeMetadata


class LocalFileSystem(DataLayer):
    # NOTE should one get some return value after a (non)succesfull save?
    @staticmethod
    def save(data_layer_identifier: DataLayerIdentifier, data: Any) -> None:
        file_extension = ""
        data_to_save = None

        if isinstance(data, dict):
            file_extension = ".json"
            data_to_save = json.dumps(data)  # NOTE we could prettify the data
        elif isinstance(data, BeautifulSoup):
            # TODO abstract away the knowledge of what scraping lib we're using
            file_extension = ".html"
            data_to_save = str(data)  # NOTE we could prettify the data
        else:
            print("Unknown format")
            print(data)
            raise NotImplementedError

        # HACK dont really like that we take no consideration of where the script is run from
        path = "data/%s%s" % (
            '/'.join(data_layer_identifier.lower().split("::")), file_extension)

        # If the directories don't exist then the "open" call will fail with a FileNotFoundError
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # FIXME handle collisions in identifier, right now it will just overwrite
        if data_to_save:
            with open(path, 'w') as file:
                file.write(data_to_save)
        else:
            print("data_to_save was never set")
            print(data)  # type: ignore
            print(file_extension)
            raise NotImplementedError

    @staticmethod
    def load(data_layer_identifier: DataLayerIdentifier) -> Any:
        path = "data/%s" % ('/'.join(data_layer_identifier.lower().split("::")))
        possible_files = glob.glob(path + ".*")

        if possible_files:
            with open(possible_files[0], 'r') as file:
                content = file.read()
                _, extension = os.path.splitext(file.name)

                if extension == ".json":
                    return json.loads(content)
                else:
                    print("Unknown format")
                    print(content)
                    raise NotImplementedError
        else:
            return None

    @staticmethod
    def load_metadata(data_layer_identifier: DataLayerIdentifier) -> Metadata:
        metadata: Metadata = LocalFileSystem.load(
            data_layer_identifier + "::METADATA")  # HACK THis is horrible, the load method returns Any and there's no static checking that this is sane
        return metadata

    @staticmethod
    def update_metadata(data_layer_identifier: DataLayerIdentifier, update: Metadata) -> None:
        old_metadata: Metadata = LocalFileSystem.load(
            data_layer_identifier + "::METADATA")
        new_metadata = None

        if old_metadata:
            new_metadata = old_metadata | update
        else:
            new_metadata = update

        return LocalFileSystem.save(data_layer_identifier + "::METADATA", new_metadata)

    @ staticmethod
    def update_scrape_metadata(data_layer_identifier: DataLayerIdentifier, update: ScrapeMetadata) -> None:
        return LocalFileSystem.update_metadata(data_layer_identifier=data_layer_identifier, update={"scrape": update})
