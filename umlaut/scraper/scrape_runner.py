import argparse
import json
from typing import cast

from data_layer.data_layer import DataLayer
from data_layer.local_file_system_data_layer import LocalFileSystem
from scrape_config.scrape_config import Config, ScrapeType, SquidScrapeConfig

# NOTE should this return something, i.e start the scrape and return the id, and let the scrape continue running in the background


def run_scrape(data_layer: DataLayer, config: Config):
    scrape_type = config['scrape_config']["scrape_type"]
    scrape_config = None
    if ScrapeType[scrape_type] == ScrapeType.SQUID_SCRAPE:
        scrape_config = cast(SquidScrapeConfig, config['scrape_config'])
        print(scrape_config)

    data_layer.save(data_layer_identifier="hello::world",
                    data={"hello2": "world"})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run a scrape using the supplied config.')
    parser.add_argument('-c', '--config', type=open,
                        help='A config for the scrape')

    args = parser.parse_args()

    config: Config = json.loads(args.config.read())
    # NOTE should we do the json loading elsewhere?

    data_layer = LocalFileSystem()

    run_scrape(data_layer=data_layer, config=config)
