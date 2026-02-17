from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location

options = [
    PropertyTypesOption([PropertyType.APARTMENT]),
    LocationsOption([Location.DUBLIN_6_DUBLIN, Location.DUBLIN_6_DUBLIN]),
    PriceOption(2000, 2600),
    BedOption(1, 1),
]


def find_properties():
    api = DaftSearch(SearchType.RENT)
    return [property.title for property in api.search(options)]


def find_properties():
    # For now, return some mock data.
    return ["Rathmines Road Upper, Dublin 6, Rathgar, Dublin 6",
            "Ramleh Hall, Convent Avenue, Milltown, Dublin 6"]
