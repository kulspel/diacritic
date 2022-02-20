from dataclasses import dataclass
from scraper.scraper import Scraper
import requests
from bs4 import BeautifulSoup

from scrape_config.scrape_config import SquidScrapeConfig
from data_layer.data_layer import DataLayer
from id_service.id_service import IdService


@dataclass(frozen=True)
class SquidScraper(Scraper[SquidScrapeConfig]):

    @staticmethod
    def run_scrape(id_service: IdService, data_layer: DataLayer, scrape_config: SquidScrapeConfig):
        print("run_scrape")
        print("id_service", id_service)
        # page = requests.get(self.scrape_config['origin_url'])
        # html_content = page.text
        # soup = BeautifulSoup(html_content, 'html.parser')
        # print(soup.prettify())
