from abc import ABC, abstractmethod

from data_layer.data_layer import DataLayer
from model.scrape_config import Config
from id_service.id_service import Id, IdService


class ScrapeRunner(ABC):

    @staticmethod
    @abstractmethod
    def start_scrape(data_layer: DataLayer, id_service: IdService, config: Config) -> Id:
        raise NotImplementedError
