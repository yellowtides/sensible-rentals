
from enum import Enum
from typing import List
import json
from src.core.distance_calculator.distance_calculator import DistanceCalculator
from src.core.types.property import Property
from datetime import timedelta, datetime


class Checkers:
    def __init__(self, workplace_address: str | None = None):
        self.distance_calculator = DistanceCalculator(
            workplace_address
        )


class PropertyScoreAttributes:
    def __init__(self, property: Property, checkers: Checkers):
        self.distance = checkers.distance_calculator.find_distance_from(
            property.address
        )
        self.distance_in_minutes = round(
            self.distance.duration_seconds / 60, 2
        )
        self.posted_at = property.created_at

    def __str__(self):
        return json.dumps(self, default=vars)


class EligibilityCheck(Enum):
    WITHIN_35_MINUTES_OF_WORKPLACE = "within-35-minutes"
    POSTED_1_DAY_AGO = "posted-1-day-ago"

    def check(self, property_score_attributes: PropertyScoreAttributes) -> bool:
        if self is EligibilityCheck.WITHIN_35_MINUTES_OF_WORKPLACE:
            return property_score_attributes.distance_in_minutes <= 35
        if self is EligibilityCheck.POSTED_1_DAY_AGO:
            yesterday = datetime.now() - timedelta(days=1)
            return property_score_attributes.posted_at / 1000 >= datetime.timestamp(yesterday)
        return True


class EligibilityChecker:
    def __init__(self, eligibility_checks: List[EligibilityCheck], checkers: Checkers):
        self.eligibility_checks = eligibility_checks
        self.checkers = checkers

    def score_property(self, property: Property) -> PropertyScoreAttributes:
        return PropertyScoreAttributes(property, self.checkers)

    def grade_property_score(self, property_score: PropertyScoreAttributes) -> bool:
        return all(map(lambda ec: ec.check(property_score), self.eligibility_checks))
