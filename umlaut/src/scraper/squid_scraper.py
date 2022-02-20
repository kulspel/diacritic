from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from data_layer.data_layer import DataLayer
from id_service.id_service import IdService
from scrape_config.scrape_config import SquidScrapeConfig

from scraper.scraper import Scraper
from id_service.data_layer_id_service import ParentIdentifier

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class SquidScraper(Scraper[SquidScrapeConfig]):

    @classmethod
    def run_scrape(cls, id_service: IdService[ParentIdentifier], data_layer: DataLayer, scrape_config: SquidScrapeConfig):
        scrape_id = id_service.get_id(class_identifier=cls.parent_identifier)

        print(scrape_id)
        # page = requests.get(self.scrape_config['origin_url'])
        # html_content = page.text
        # soup = BeautifulSoup(html_content, 'html.parser')
        # print(soup.prettify())
