from abc import ABC, abstractmethod

from data_layer.data_layer import DataLayer
from scrape_config.scrape_config import Config

# NOTE should this return something, i.e start the scrape and return the id, and let the scrape continue running in the background


class ScrapeRunner(ABC):

    @staticmethod
    @abstractmethod
    def start_scrape(data_layer: DataLayer, config: Config) -> int:
        pass
