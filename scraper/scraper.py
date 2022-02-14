import argparse
from scraper.data_layer.data_layer import DataLayer

from scraper.data_layer.local_file_system_data_layer import LocalFileSystem


def main(data_layer: DataLayer):
    print("hello world")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Scrape some websites using the supplied scrapeconfig.')
    parser.add_argument('-c', '--config', type=open,
                        help='an integer for the accumulator')

    args = parser.parse_args()

    data_layer = LocalFileSystem

    main(data_layer=data_layer)
