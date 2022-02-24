from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Generic, TypeVar

import requests
from bs4 import BeautifulSoup
from data_layer.data_layer import (DataLayer, DataLayerIdentifier,
                                   toDataLayerIdentifier)
from id_service.id_service import Id, IdService
from scrape_config.scrape_config import ScrapeConfig

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


# NOTE would be nice if we could constrain T to
Config = TypeVar('Config', bound='ScrapeConfig')


@dataclass(frozen=True)
class Scraper(ABC, Generic[Config]):
    parent_identifier = 'SCRAPES'
    id_service: IdService
    data_layer: DataLayer
    scrape_config: Config
    scrape_id: Id = field(init=False)
    identifier: DataLayerIdentifier = field(init=False)
    # HACK can we remove this lint suppression?

    def __post_init__(self):

        object.__setattr__(
            self,
            'scrape_id',
            self.id_service.get_id(class_identifier=self.parent_identifier)
        )

        object.__setattr__(
            self,
            'identifier',
            toDataLayerIdentifier(
                [
                    self.parent_identifier,
                    str(self.scrape_id)
                ]
            )
        )

        # NOTE are we coupling our code really bad right now?
        # "start_time": datetime.now().isoformat(),
        self.data_layer.update_scrape_metadata(
            self.identifier, {"scrape_config": self.scrape_config})

    @ abstractmethod
    def run_scrape(self) -> Id:
        raise NotImplementedError

    # NOTE Perhaps abstract away the info that we're doing it via BeatifulSoup?
    def scrape_url(self, url: str) -> BeautifulSoup:
        page = requests.get(url)
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')

        return soup

        # TODO or perhaps just be able to create a scrape from a partially completed one.
        # @ abstractmethod
        # def resume_scrape(self, scrape_id :Id) -> Id:
        #     raise NotImplementedError
