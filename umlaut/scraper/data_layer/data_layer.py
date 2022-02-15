# TODO This one needs to be abstracted to it's own package separate from the scraper, since all will need to use it
class DataLayer:

    # NOTE don't know if I can constrain the object type more
    def save(self, data_layer_identifier: str, data: object):
        pass

    # def load(self, data_layer_identifier: str):
    #    pass
