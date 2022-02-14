from scraper.data_layer.data_layer import DataLayer


class LocalFileSystem(DataLayer):

    def save(self, data_layer_identifier: str, data):
        path = data_layer_identifier.split("::")
        return super().save(data_layer_identifier, data)
