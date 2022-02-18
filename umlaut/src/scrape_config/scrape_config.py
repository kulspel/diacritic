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
    # NOTE version is in a similar situation to id but maybe not as bad
    version: str
    name: str
    description: str
    # TODO Make this nullable? Don't even know if that's a thing in Python
    scrape_type: str
    # NOTE Would want this one to be ScrapeType but ran into issues when comparing this value to ScrapeType enum


class SquidScrapeConfig(ScrapeConfig):
    origin_url: str


class Config(TypedDict):
    job_parameters: JobParameters
    scrape_config: ScrapeConfig
