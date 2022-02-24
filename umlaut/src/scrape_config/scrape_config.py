from enum import Enum
from typing import TypedDict

# NOTE Should this package be some kind of Model package instead?


class JobParameters(TypedDict):
    test_run: bool
    override_existing: bool


class ScrapeType(Enum):
    SQUID_SCRAPE = 1


class ScrapeConfig(TypedDict):
    # NOTE how to solve the whole ID issue, the configs basically needs to be persisted and controlled by the DataLayer
    id: int
    # NOTE version is in a similar situation to id but maybe not as bad, mostly that it's pretty stupid to have it here with the current state of the project (it's not used)
    version: str
    name: str
    description: str
    scrape_type: str
    # FIXME Would want this one to be ScrapeType but ran into issues when comparing this value to ScrapeType enum
    base_url: str


class SquidScrapeConfig(ScrapeConfig):
    origin_page: str
    sub_page_class: str
    next_page_class: str  # NOTE Maybe next_page_class should be on ScrapeConfig, also in general I need to think about which ones should be optional and handle that everywhere


class Config(TypedDict):
    job_parameters: JobParameters
    scrape_config: ScrapeConfig
