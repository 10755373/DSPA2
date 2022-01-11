// def create_stop_location_detail(title, latitude, longitude, index, route_index):
point = Point([longitude, latitude])
properties = {
    "title": title,
    'icon': "campsite",
    'marker-color': '#3bb2d0',
    'marker-symbol': index,
    'route_index': route_index
}
feature = Feature(geometry = point, properties = properties)
return feature

def create_stop_locations_details():
stop_locations = []
for route_index, location in enumerate(ROUTE):
    if not location["is_stop_location"]:
        continue
    stop_location = create_stop_location_detail(
        location['name'],
        location['lat'],
        location['long'],
        len(stop_locations) + 1,
        route_index
    )
    stop_locations.append(stop_location)
return stop_locations