from src.core.property_finder.property_finder import PropertyFinder
from src.core.eligibility_checker.eligibility_checker import EligibilityChecker, EligibilityCheck, Checkers

import os

from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption,
    PriceOption, BedOption, AdState, AdStateOption,
    SortOption, Sort, FurnishingOption, Furnishing
)
from daft_scraper.search.options_location import LocationsOption, Location

WORKPLACE_ADDRESS = os.getenv('WORKPLACE_ADDRESS')
PROPERTY_OPTIONS = [
    PropertyTypesOption([PropertyType.APARTMENT,
                         PropertyType.HOUSE]),
    LocationsOption([Location.DUBLIN_6_DUBLIN,
                    Location.DUBLIN_4_DUBLIN,
                    Location.DUBLIN_18_DUBLIN,
                    Location.DUBLIN_14_DUBLIN,
                    Location.BLACKROCK_DUBLIN,
                    Location.RATHMINES_DUBLIN,
                    Location.SANDYMOUNT_DUBLIN,
                    Location.RANELAGH_DUBLIN,
                    Location.SANDYFORD_DUBLIN,
                    Location.SANDYMOUNT_DUBLIN]),
    AdStateOption(AdState.AVAILABLE),
    SortOption(Sort.MOST_RECENT),
    FurnishingOption(Furnishing.FURNISHED),
    PriceOption(2000, 2600),
    BedOption(1, 1),
]

property_finder = PropertyFinder(PROPERTY_OPTIONS)
checkers = Checkers(workplace_address=WORKPLACE_ADDRESS)
eligibility_checker = EligibilityChecker(
    eligibility_checks=[EligibilityCheck.WITHIN_35_MINUTES], checkers=checkers
)

for property in property_finder.search_properties():
    property_score = eligibility_checker.score_property(property)
    is_property_eligible = eligibility_checker.grade_property_score(
        property_score
    )
    if not is_property_eligible:
        continue

    print(f'Found eligible property!')
    print(f'Property: {property}\n',
          f'Property score: {property_score}')
    print('---')
