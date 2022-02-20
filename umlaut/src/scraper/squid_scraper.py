from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from data_layer.data_layer import DataLayer
from id_service.id_service import IdService
from scrape_config.scrape_config import SquidScrapeConfig

from scraper.scraper import Scraper

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class SquidScraper(Scraper[SquidScrapeConfig]):

    @classmethod
    def run_scrape(cls, id_service: IdService, data_layer: DataLayer, scrape_config: SquidScrapeConfig):
        print("run_scrape")

        print("parent_identifier", cls.parent_identifier.get_parent_identifier())
        # page = requests.get(self.scrape_config['origin_url'])
        # html_content = page.text
        # soup = BeautifulSoup(html_content, 'html.parser')
        # print(soup.prettify())
