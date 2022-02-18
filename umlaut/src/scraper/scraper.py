from abc import ABC, abstractmethod

#from scrape_config.scrape_config import ScrapeConfig


class Scraper(ABC):
    #scrape_config: ScrapeConfig

    @abstractmethod
    def run_scrape(self):
        pass
