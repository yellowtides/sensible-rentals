import src.core.property_finder.property_finder as pf
import src.core.distance_calculator.distance_calculator as dc
import os

POINT_OF_INTEREST = os.getenv('POINT_OF_INTEREST')

for property in pf.find_properties():
    distance_calculator = dc.DistanceCalculator(POINT_OF_INTEREST)
    distance_to_property = distance_calculator.find_distance_to(property)
    commute_time_hours = distance_to_property.duration_seconds / 60
    print(f'Property address: {property}\n',
          f'Commute time (hours): {commute_time_hours}')
    print('---')
