# NOTE not sure if this belongs here, should probably be in some model package
from typing import TypedDict

from scrape_config.scrape_config import ScrapeConfig


class IdServiceMetadata(TypedDict):
    id_counter: int


class ScrapeMetada(TypedDict, total=False):
    # NOTE are times even needed?
    # start_time: str  # NOTE Would be nice to have this as datetime, but datetime isnt json serializable, a problem for the future, for now, just don'ät put any weird strings in here, should be settable by setting some jsonencoder
    # end_time:str
    url: str
    id_service: IdServiceMetadata
    scrape_config: ScrapeConfig
