from abc import ABC, abstractmethod
from typing import Generic

from data_layer.data_layer import DataLayer
from scrape_config.scrape_config import Config
from id_service.id_service import IdService, Identifier

# NOTE should this return something, i.e start the scrape and return the id, and let the scrape continue running in the background


class ScrapeRunner(ABC, Generic[Identifier]):

    @staticmethod
    @abstractmethod
    def start_scrape(data_layer: DataLayer, id_service: IdService[Identifier], config: Config) -> int:
        raise NotImplementedError
