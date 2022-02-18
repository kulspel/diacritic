from dataclasses import dataclass
from scraper.scraper import Scraper
import requests
from bs4 import BeautifulSoup

from scrape_config.scrape_config import SquidScrapeConfig


@dataclass(frozen=True)
class SquidScraper(Scraper):
    scrape_config: SquidScrapeConfig

    def run_scrape(self):
        page = requests.get(self.scrape_config['origin_url'])
        html_content = page.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print(soup.prettify())
