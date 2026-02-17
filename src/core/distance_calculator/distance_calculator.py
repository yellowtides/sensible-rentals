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


class Geocode:
    def __init__(self, lat: float, lng: float):
        self.lat = float(lat)
        self.lng = float(lng)

    def __dict__(self):
        return {'location': {'latLng': {'latitude': self.lat, 'longitude': self.lng}}}

    def __str__(self):
        return json.dumps(self.__dict__())


class Distance:
    def __init__(self, distance_meters: int, duration_seconds: int):
        self.distance_meters = int(distance_meters)
        self.duration_seconds = int(duration_seconds)

    def __dict__(self):
        return {'distance_meters': self.distance_meters, 'duration_seconds': self.duration_seconds}

    def __str__(self):
        return json.dumps(self.__dict__())


class DistanceCalculator:
    def __init__(self, destination: str):
        self.destination = str(destination)
        self.destination_geocode = self.geocode(destination)

    def geocode(self, point: str) -> Geocode:
        params = {**DEFAULT_GEOCODE_API_PARAMS, **{'address': point}}
        response = requests.get(f"{GEOCODE_API_ROOT}", params=params)
        json_data = response.json()
        json_geocode = json_data['results'][0]['geometry']['location']
        return Geocode(lat=json_geocode['lat'], lng=json_geocode['lng'])

    def find_distance_to(self, point: str):
        point_geocode = self.geocode(point)
        payload = json.dumps({'origin': point_geocode.__dict__(),
                             'destination': self.destination_geocode.__dict__(),
                              **DEFAULT_ROUTE_API_PARAMS})
        headers = {**DEFAULT_ROUTE_API_HEADERS}
        response = requests.post(f"{ROUTE_API_ROOT}",
                                 data=payload, headers=headers)
        json_data = response.json()
        json_distance = json_data['routes'][0]
        return Distance(distance_meters=json_distance['distanceMeters'], duration_seconds=json_distance['duration'][:-1])
