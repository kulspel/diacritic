import argparse
import json
from typing import cast

from data_layer.data_layer import DataLayer
from data_layer.local_file_system_data_layer import LocalFileSystem
from id_service.data_layer_id_service import DataLayerIdService, ParentIdentifier
from id_service.id_service import IdService
from scrape_config.scrape_config import Config, ScrapeType, SquidScrapeConfig
from scrape_runner import ScrapeRunner
from scraper.squid_scraper import SquidScraper


class OnDeviceScrapeRunner(ScrapeRunner[ParentIdentifier]):

    @staticmethod
    # TODO make this spawn the scrape in a separate thread so one doesnt wait around for it
    def start_scrape(data_layer: DataLayer, id_service: IdService[ParentIdentifier], config: Config):
        scrape_type = config['scrape_config']["scrape_type"]
        if ScrapeType[scrape_type] == ScrapeType.SQUID_SCRAPE:
            SquidScraper(id_service=id_service, data_layer=data_layer).run_scrape(
                # HACK casting like this probably super unsafe
                scrape_config=cast(SquidScrapeConfig, config['scrape_config'])
            )

        return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Run a scrape using the supplied config.')
    parser.add_argument('-c', '--config', type=open,
                        help='A config for the scrape')

    args = parser.parse_args()

    config: Config = json.loads(args.config.read())
    # HACK THis is horrible, the method returns Any and there's no static checking that this is sane
    # NOTE should we do the json loading elsewhere?

    data_layer = LocalFileSystem()
    id_service = DataLayerIdService(data_layer=data_layer)
    OnDeviceScrapeRunner.start_scrape(
        data_layer=data_layer, id_service=id_service, config=config)
