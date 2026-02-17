from typing import List

from daft_scraper.search import DaftSearch, SearchType, Listing
from src.core.types.property import Property

from src.core.distance_calculator.distance_calculator import DistanceCalculator


class PropertyFinder:
    def __init__(self, options):
        self.options = options
        self.daft_api = DaftSearch(SearchType.RENT)
        self.result = None

    def search_properties(self) -> List[Property]:
        if self.result is None:
            self.result = self.daft_api.search(self.options)
        listings = [listing for listing in self.result]
        return list(map(Property, listings))

    def search_properties(self) -> List[Property]:
        # For now, return some mock data.
        return [Property(Listing({'title': 'Rathmines Road Upper, Dublin 6, Rathgar, Dublin 6', 'publishDate': 0, 'image': {}})),
                Property(Listing({'title': 'Ramleh Hall, Convent Avenue, Milltown, Dublin 6', 'publishDate': 0, 'image': {}}))]
