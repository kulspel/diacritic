# NOTE not sure if this belongs here, should probably be in some model package
from typing import TypedDict
from datetime import datetime

from scrape_config.scrape_config import ScrapeConfig


class IdServiceMetadata(TypedDict):
    id_counter: int


class Metadata(TypedDict, total=False):
    start_time: datetime
    id_service: IdServiceMetadata
    scrape_config: ScrapeConfig
