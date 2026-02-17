from daft_scraper.listing import Listing

import json


class Property:
    def __init__(self, listing: Listing):
        self.address = listing.title
        self.created_at = listing.publishDate
        self.image = listing.media["images"][0]["size720x480"]
        self.url = listing.url
        self.id = listing.id
        self.price = listing.price

    def __str__(self) -> str:
        return json.dumps(self.__dict__, default=vars)
