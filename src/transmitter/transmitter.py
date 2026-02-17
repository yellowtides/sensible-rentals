import os
import requests

from src.core.types.property import Property
from src.core.eligibility_checker.eligibility_checker import PropertyScoreAttributes

ENDPOINT = os.getenv("NOTIFICATION_ENDPOINT")
PATH_TO_FAVICON = 'https://static.vecteezy.com/system/resources/thumbnails/022/750/436/small/3d-home-icon-free-png.png'


class Transmitter:
    def _make_ntfy_headers(self, property: Property):
        return {
            "Click": property.url,
            "Attach": property.image,
            "Filename": "property.jpg",
            "Title": property.address.strip(),
            "Priority": "5",
            "Icon": PATH_TO_FAVICON,
            "Tags": "house_with_garden"
        }

    def _make_ntfy_data(self, property: Property, property_score_attributes: PropertyScoreAttributes):
        return '\n'.join([f"€{property.price} p.m.", f"{property_score_attributes.distance_in_minutes} minutes away"]).encode(encoding='utf-8')

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
