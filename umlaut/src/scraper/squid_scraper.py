from scraper.scraper import Scraper
from scrape_config.scrape_config import SquidScrapeConfig
from id_service.id_service import Id
from data_layer.data_layer import appendDataLayerIdentifier
from bs4 import Tag
from dataclasses import dataclass


# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class SquidScraper(Scraper[SquidScrapeConfig]):

    def run_scrape(self) -> Id:
        origin_page_url = self.scrape_config['base_url'] + \
            self.scrape_config['origin_page']
        self.data_layer.update_metadata(
            self.identifier, {"url": origin_page_url})

        origin_page = self.scrape_page(origin_page_url)

        self.data_layer.save(
            appendDataLayerIdentifier(
                self.identifier,
                "origin_page"
            ),
            origin_page
        )

        sub_page_link_elements = origin_page.find_all(
            "a",
            {"class": self.scrape_config["sub_page_class"]}
        )

        sub_pages = [
            tag['href']
            for tag in sub_page_link_elements
            if isinstance(tag, Tag)
        ]

        # TODO see which ones are not Tags

        sub_page_scrape_ids = [
            self.scrape_sub_page(sub_page)
            for sub_page in sub_pages
            if isinstance(sub_page, str)
        ]

        # TODO see which ones are not strs
        # FIXME looking at the output it looks like we get 2 sub page scrapes with the same ids, which is kinda bad since we won't handle collisions cracefully
        print(sub_page_scrape_ids)

        # TODO implement how to go to the "next page" and continue scraping

        return self.scrape_id

    # NOTE should this be done in parallel?
    def scrape_sub_page(self, sub_page_url_addition: str) -> Id:

        # NOTE this information is already in the identifier, should there be a way of getting it from that?
        sub_scrape_id = self.id_service.get_id(self.identifier)

        sub_page_url = self.scrape_config['base_url'] + sub_page_url_addition

        self.data_layer.update_metadata(
            appendDataLayerIdentifier(
                self.identifier,
                str(sub_scrape_id)
            ),
            {"url": sub_page_url}
        )

        sub_page = self.scrape_page(sub_page_url)
        # print(sub_page)

        self.data_layer.save(
            appendDataLayerIdentifier(
                self.identifier,
                str(sub_scrape_id),
                "sub_page"
            ),
            sub_page
        )

        return sub_scrape_id
