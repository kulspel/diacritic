from dataclasses import dataclass
from functools import partial
from typing import Callable, List

from bs4 import BeautifulSoup
from data_layer.data_layer import appendDataLayerIdentifier
from id_service.id_service import Id
from scrape_config.scrape_config import SquidScrapeConfig

from scraper.scraper import Scraper

# HACK the only reason these imports  work is because we run scrape_runner.py which I guess brings these packages into scope somehow


@dataclass(frozen=True)
class Page:
    page: BeautifulSoup
    url: str


@dataclass(frozen=True)
# NOTE This is no longer really a squidscraper really I guess, it's more how we do the next stuff
class SquidScraper(Scraper[SquidScrapeConfig]):

    # TODO __find_links,__extract_sub_pages should be the responsibility of Macron (extractor)
    # TODO change all list in type signature to List
    def __extract_urls(self, html_class_to_extract: str, soup: BeautifulSoup) -> List[str]:
        page_link_elements = soup.find_all(
            "a",
            {"class": html_class_to_extract}
        )

        # TODO see which ones are not strs´
        return[
            str(tag['href'])
            for tag in page_link_elements
        ]

    # HACK ugly mutable stuff
    # NOTE this could pretty easily be done recursively
    def scrape_origin_pages(self, origin_page_url: str) -> List[Page]:

        origin_page = Page(self.scrape_url(origin_page_url), origin_page_url)

        # TODO this needs to be extracted into the config somehow
        number_of_pages = origin_page.page.find_all(
            "div",
            {"class": '__react-root', "data-react-id": "Pagination"}
        )[0]['data-page-count']

        origin_pages = [origin_page]

        # HACK, how do we know that the website starts counting at 1?
        for page_index in range(2, int(number_of_pages)+1):
            url_addition = "?page=%s" % page_index

            next_page_url = origin_page_url + url_addition  # NOTE This is prob pretty stupid
            next_page = Page(self.scrape_url(next_page_url), next_page_url)
            origin_pages.append(next_page)

        return origin_pages

    def run_scrape(self) -> Id:
        origin_page_url = self.scrape_config['base_url'] + \
            self.scrape_config['origin_page']

        origin_pages = self.scrape_origin_pages(origin_page_url)

        # TODO this for loop should be extracted into its own method(s)
        for origin_page in origin_pages:
            origin_page_id = self.id_service.get_id(self.identifier)

            self.data_layer.update_scrape_metadata(
                appendDataLayerIdentifier(
                    self.identifier,
                    str(origin_page_id)
                ),
                {"url": origin_page.url}
            )

            self.data_layer.save(
                appendDataLayerIdentifier(
                    self.identifier,
                    str(origin_page_id),
                    "origin_page"
                ),
                origin_page.page
            )

            sub_page_url_additions = self.__extract_urls(
                self.scrape_config["sub_page_class"],
                soup=origin_page.page
            )

            # TODO this for loop should be extracted into its own method(s)
            for sub_page_url_addition in sub_page_url_additions:
                sub_scrape_id = self.id_service.get_id(
                    appendDataLayerIdentifier(
                        self.identifier,
                        str(origin_page_id)
                    )
                )

                sub_page_url = self.scrape_config['base_url'] + \
                    sub_page_url_addition

                self.data_layer.update_scrape_metadata(
                    appendDataLayerIdentifier(
                        self.identifier,
                        str(origin_page_id),
                        str(sub_scrape_id)
                    ),
                    {"url": sub_page_url}
                )

                sub_page = self.scrape_url(sub_page_url)

                self.data_layer.save(
                    appendDataLayerIdentifier(
                        self.identifier,
                        str(origin_page_id),
                        str(sub_scrape_id),
                        "sub_page"
                    ),
                    sub_page
                )

                # print(sub_scrape_id)

        return self.scrape_id
