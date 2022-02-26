from typing import TypedDict

from model.scrape_config import ScrapeConfig  # type: ignore
# FIXME Figure out how to do this, creating stubs puts them in the root of diacritic, and moving the .pyi files here breaks pylance....


class IdServiceMetadata(TypedDict):
    id_counter: int


class ScrapeMetadata(TypedDict, total=False):
    # FIXME start_time
    # start_time: str
    url: str
    # NOTE should IdServiceMetadata be part of ScrapeMetadata or should it be top level?
    id_service: IdServiceMetadata
    scrape_config: ScrapeConfig


class Metadata(TypedDict, total=False):
    scrape: ScrapeMetadata
