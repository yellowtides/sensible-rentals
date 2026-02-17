import os
import json
import requests

from src.core.types.property import Property
from src.core.eligibility_checker.eligibility_checker import PropertyScoreAttributes

ENDPOINT = os.getenv("NOTIFICATION_ENDPOINT")


class Transmitter:
    def _make_ntfy_headers(self, property: Property):
        return {
            "Click": property.url,
            "Filename": "property.jpg",
            "Title": property.address.strip(),
            "Priority": "5",
            "Tags": "house_with_garden",
            "Actions": f"view, See on Daft, {property.url}"
        }

    def _make_ntfy_data(self, property: Property, property_score_attributes: PropertyScoreAttributes):
        return '\n'.join([
            f"€{property.price} p.m.",
            f"{property_score_attributes.distance_in_minutes} minutes away"
        ]).encode(encoding='utf-8')

    def transmit(self, property: Property, property_score_attributes: PropertyScoreAttributes):
        requests.post(
            ENDPOINT,
            data=(self._make_ntfy_data(
                property, property_score_attributes
            )),
            headers=self._make_ntfy_headers(
                property
            )
        )
