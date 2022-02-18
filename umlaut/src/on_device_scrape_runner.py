import argparse
import json
from typing import cast
from data_layer.data_layer import DataLayer
from data_layer.local_file_system_data_layer import LocalFileSystem
from scrape_config.scrape_config import Config, ScrapeType, SquidScrapeConfig
from scrape_runner import ScrapeRunner
from scraper.squid_scraper import SquidScraper


class OnDeviceScrapeRunner(ScrapeRunner):

    @staticmethod
    # TODO make this spawn the scrape in a separate thread so one doesnt wait around for it
    def start_scrape(data_layer: DataLayer, config: Config):
        scrape_type = config['scrape_config']["scrape_type"]
        scraper = None
        if ScrapeType[scrape_type] == ScrapeType.SQUID_SCRAPE:

            scraper = SquidScraper(
                cast(SquidScrapeConfig, config['scrape_config']))

            scraper.run_scrape()

        data_layer.save(data_layer_identifier="hello::world",
                        data={"hello2": "world"})

        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run a scrape using the supplied config.')
    parser.add_argument('-c', '--config', type=open,
                        help='A config for the scrape')

    args = parser.parse_args()

    config: Config = json.loads(args.config.read())
    # NOTE should we do the json loading elsewhere?

    data_layer = LocalFileSystem()

    OnDeviceScrapeRunner.start_scrape(data_layer=data_layer, config=config)
