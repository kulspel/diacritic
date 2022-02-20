import json
import os
from data_layer.data_layer import DataLayer


class LocalFileSystem(DataLayer):
    # NOTE should one get some return value after a (non)succesfull save?
    @staticmethod
    def save(data_layer_identifier: str, data: object) -> None:
        # FIXME the file ending probably shouldnt be hardcoded
        # HACK dont really like that we take no consideration of where the script is run from
        path = "data/%s.json" % ('/'.join(data_layer_identifier.split("::")))

        # If the directories don't exist then the "open" call will fail with a FileNotFoundError
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # FIXME handle collisions in identifier, right now it will just overwrite
        with open(path, 'w') as file:
            file.write(json.dumps(data))
