# NOTE not sure if this belongs here, should probably be in some model package
# NOTE just realized that this will likely be a real nightmare if different services are reading/writing to the same metadata. We could simply prepend it with e.g umlaut to not have services messing with eachthers metadata
from typing import TypedDict

from scrape_config.scrape_config import ScrapeConfig


class IdServiceMetadata(TypedDict):
    id_counter: int


# NOTE perhaps a bit cheeky but wouldnt it be a little fun to call this UmlautMetadata and have the field be called "umlaut" instead of "scrape"
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
