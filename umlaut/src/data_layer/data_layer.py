from abc import ABC, abstractmethod

# TODO This one needs to be abstracted to it's own package separate from the scraper, since all will need to use it


class DataLayer(ABC):

    # NOTE don't know if I can constrain the object type more
    @staticmethod
    @abstractmethod
    def save(data_layer_identifier: str, data: object):
        pass

    # def load(self, data_layer_identifier: str):
    #    pass
