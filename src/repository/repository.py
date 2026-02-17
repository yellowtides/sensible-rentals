import pickle

from src.core.types.property import Property

REPOSITORY_PATH = '.artifacts/last_property.pkl'


class Repository:
    def read_last_property(self) -> Property | None:
        with open(REPOSITORY_PATH, 'rb') as last_property_file:
            try:
                return pickle.load(last_property_file)
            except:
                return None

    def write_last_property(self, property: Property):
        with open(REPOSITORY_PATH, 'wb') as last_property_file:
            return pickle.dump(property, last_property_file)
