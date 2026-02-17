import requests
import os
import json

API_KEY = os.getenv("GOOGLE_API_KEY")
GEOCODE_API_ROOT = "https://maps.googleapis.com/maps/api/geocode/json"
DEFAULT_GEOCODE_API_PARAMS = {'key': f'{API_KEY}'}

ROUTE_API_ROOT = "https://routes.googleapis.com/directions/v2:computeRoutes"
DEFAULT_ROUTE_API_PARAMS = {'travelMode': 'TRANSIT',
                            'computeAlternativeRoutes': False,
                            'arrivalTime': '2026-02-16T09:00:00Z'}
DEFAULT_ROUTE_API_HEADERS = {'X-Goog-Api-Key': f'{API_KEY}',
                             'X-Goog-FieldMask': 'routes.duration,routes.distanceMeters'}


class LatLng:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class Location:
    def __init__(self, latLng: LatLng):
        self.latLng = latLng


class Geocode:
    def __init__(self, location: Location):
        self.location = location

    def __str__(self):
        return json.dumps(self.__dict__)


class Distance:
    def __init__(self, distance_meters: int, duration_seconds: int):
        self.distance_meters = int(distance_meters)
        self.duration_seconds = int(duration_seconds)

    def __str__(self):
        return json.dumps(self.__dict__)


class DistanceCalculator:
    def __init__(self, destination_address: str):
        self.destination_address = str(destination_address)
        self.destination_address_geocode = self.geocode(destination_address)

    def geocode(self, point: str) -> Geocode:
        params = {**DEFAULT_GEOCODE_API_PARAMS, **{'address': point}}
        response = requests.get(f"{GEOCODE_API_ROOT}", params=params)
        json_data = response.json()
        json_geocode = json_data['results'][0]['geometry']['location']
        return Geocode(Location(LatLng(latitude=json_geocode['lat'], longitude=json_geocode['lng'])))

    def find_distance_from(self, origin_address: str):
        origin_address_geocode = self.geocode(origin_address)
        payload = json.dumps({'origin': origin_address_geocode,
                              'destination': self.destination_address_geocode,
                              **DEFAULT_ROUTE_API_PARAMS}, default=vars)
        headers = {**DEFAULT_ROUTE_API_HEADERS}
        response = requests.post(f"{ROUTE_API_ROOT}",
                                 data=payload, headers=headers)
        json_data = response.json()
        json_distance = json_data['routes'][0]
        return Distance(distance_meters=json_distance['distanceMeters'], duration_seconds=json_distance['duration'][:-1])
