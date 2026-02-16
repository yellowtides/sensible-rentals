# from daft_scraper.search import DaftSearch, SearchType
# from daft_scraper.search.options import (
#     PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
#     PriceOption, BedOption
# )
# from daft_scraper.search.options_location import LocationsOption, Location

# options = [
#     PropertyTypesOption([PropertyType.APARTMENT]),
#     FacilitiesOption([Facility.PARKING, Facility.SERVICED_PROPERTY]),
#     LocationsOption([Location.DUBLIN_6_DUBLIN]),
#     PriceOption(0, 4000),
#     BedOption(1, 2),
# ]


def find_properties():
    """Return some mock data."""
    return ["Rathmines Road Upper, Dublin 6, Rathgar, Dublin 6",
            "Ramleh Hall, Convent Avenue, Milltown, Dublin 6"]
    # api = DaftSearch(SearchType.RENT)
    # return api.search(options)
