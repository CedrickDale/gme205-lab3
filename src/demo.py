from spatial import Point

# Create Point P
p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

# Create Point Q
q = Point("B", 121.1, 14.7, name="Destination", tag="POI")

# Display basic properties of P
print(p.id)
print(p.lon, p.lat)
print(p.to_tuple())
print(p.geometry.geom_type)

# This is Cartesian distance in the coordinate units. 
# For lon/lat values, do NOT label the result as meters. 
coordinate_distance = p.geometry.distance(q.geometry)

# Preserve the geodesic meaning from Laboratory 2:
meters = p.distance_to(q)  # Haversine implementation from Lab 2

print("Cartesian distance:", coordinate_distance)
print("Haversine distance:", meters, "meters")

# Dictionary to Point

record = {
    "id": "A", 
    "lon": 121.0,
    "lat": 14.6,
    "name": "Gate",
    "tag": "POI"
}

p2 = Point.from_dict(record)

print(p2.to_tuple())
print(p2.as_dict())

# Invalid dictionary
invalid_record = {
    "id": "B",
    "lon": 999,
    "lat": 14.6
}

try:
    invalid_point = Point.from_dict(invalid_record)
except ValueError as error:
    print("Invalid record:", error)