# NOTE not sure if this belongs here, should probably be in some model package
from typing import TypedDict

from scrape_config.scrape_config import ScrapeConfig


class IdServiceMetadata(TypedDict):
    id_counter: int


class Metadata(TypedDict, total=False):
    start_time: str  # NOTE Would be nice to have this as datetime, but datetime isnt json serializable, a problem for the future, for now, just don'ät put any weird strings in here, should be settable by setting some jsonencoder
    id_service: IdServiceMetadata
    scrape_config: ScrapeConfig
