import argparse
import json
from typing import cast

from data_layer.data_layer import DataLayer
from data_layer.local_file_system_data_layer import LocalFileSystem
from id_service.data_layer_id_service import DataLayerIdService
from id_service.id_service import Id, IdService
from model.scrape_config import Config, ScrapeType, SquidScrapeConfig
from scrape_runner import ScrapeRunner
from scraper.squid_scraper import SquidScraper


class OnDeviceScrapeRunner(ScrapeRunner):
    # TODO implement event/listener design pattern

    # @staticmethod
    # def get_matching_scrape_id(data_layer: DataLayer, config: Config) -> Id:
    #     return 1

    @staticmethod
    # TODO make this spawn the scrape in a separate thread so one doesnt wait around for it
    def start_scrape(data_layer: DataLayer, id_service: IdService, config: Config) -> Id:
        scrape_type = config['scrape_config']['scrape_type']

        if ScrapeType[scrape_type] == ScrapeType.SQUID_SCRAPE:
            # TODO
            # if config['job_parameters']['override_existing']:
            #     scrape_id = OnDeviceScrapeRunner.get_matching_scrape_id(
            #         data_layer=data_layer, config=config)

            scrape_id = SquidScraper(
                id_service=id_service,
                data_layer=data_layer,
                # HACK casting like this probably super unsafe
                scrape_config=cast(SquidScrapeConfig, config['scrape_config'])
            ).run_scrape()

            return scrape_id
        else:
            print("Unknown ScrapeType")
            print(config)
            raise NotImplementedError


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
