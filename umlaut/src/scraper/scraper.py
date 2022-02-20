from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from id_service.id_service import IdService
from data_layer.data_layer import DataLayer
from scrape_config.scrape_config import ScrapeConfig

from scrape_config.scrape_config import ScrapeConfig

# NOTE would be nice if we could constrain T to
Config = TypeVar('Config', bound='ScrapeConfig')


@dataclass(frozen=True)
class Scraper(ABC, Generic[Config]):
    #scrape_config: ScrapeConfig
    # id: Id  # NOTE should this be str, int, or some other type?

    @staticmethod
    @abstractmethod
    def run_scrape(id_service: IdService, data_layer: DataLayer, scrape_config: Config):
        pass
