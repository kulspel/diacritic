from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from data_layer.data_layer import toDataLayerIdentifier
from id_service.id_service import Id
from scrape_config.scrape_config import SquidScrapeConfig

from scraper.scraper import Scraper

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class SquidScraper(Scraper[SquidScrapeConfig]):

    def run_scrape(self, scrape_config: SquidScrapeConfig) -> Id:

        page = requests.get(scrape_config['origin_url'])
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup.prettify())

        self.data_layer.save(
            toDataLayerIdentifier([str(self.parent_identifier.get_parent_identifier()), str(self.scrape_id), "origin_page"]), soup)

        return self.scrape_id
