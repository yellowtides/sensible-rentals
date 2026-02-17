from daft_scraper.listing import Listing

import json


class Property:
    def __init__(self, listing: Listing):
        self.address = listing.title
        self.created_at = listing.publishDate
        self.image = listing.image
        self.url = listing.url

    def __str__(self) -> str:
        return json.dumps(self.__dict__, default=vars)
