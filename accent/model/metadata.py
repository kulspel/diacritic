# NOTE just realized that this will likely be a real nightmare if different services are reading/writing to the same metadata. We could simply prepend it with e.g umlaut to not have services messing with eachthers metadata
from typing import TypedDict

from model.scrape_config import ScrapeConfig  # type: ignore
# FIXME Figure out how to do this, creating stubs puts them in the root of diacritic, and moving the .pyi files here breaks pylance....


class IdServiceMetadata(TypedDict):
    id_counter: int


class ScrapeMetadata(TypedDict, total=False):
    # NOTE are times even needed?
    # start_time: str  # NOTE Would be nice to have this as datetime, but datetime isnt json serializable, a problem for the future, for now, just don'ät put any weird strings in here, should be settable by setting some jsonencoder
    # end_time:str
    url: str
    # NOTE should IdServiceMetadata be part of ScrapeMetadata or should it be top level?
    id_service: IdServiceMetadata
    scrape_config: ScrapeConfig


class Metadata(TypedDict, total=False):
    scrape: ScrapeMetadata
