from spatial import Point, Parcel
from shapely.geometry import Polygon

# ===================================================================
# PART B Validation
# ===================================================================
# Create Point P
#p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

# Create Point Q
#q = Point("B", 121.1, 14.7, name="Destination", tag="POI")

# Display basic properties of P
#print(p.id)
#print(p.lon, p.lat)
#print(p.to_tuple())
#print(p.geometry.geom_type)

# This is Cartesian distance in the coordinate units. 
# For lon/lat values, do NOT label the result as meters. 
#coordinate_distance = p.geometry.distance(q.geometry)

# Preserve the geodesic meaning from Laboratory 2:
#meters = p.distance_to(q)  # Haversine implementation from Lab 2

#print("Cartesian distance:", coordinate_distance)
#print("Haversine distance:", meters, "meters")

# ===================================================================
# PART C Validation
# ===================================================================
# Dictionary to Point

##record = {
#    "id": "A", 
#    "lon": 121.0,
#    "lat": 14.6,
#    "name": "Gate",
#    "tag": "POI"
#}

#p2 = Point.from_dict(record)

#print(p2.to_tuple())
#print(p2.as_dict())

# Invalid dictionary
#invalid_record = {
#    "id": "B",
#    "lon": 999,
#    "lat": 14.6
#}

#try:
#    invalid_point = Point.from_dict(invalid_record)
#except ValueError as error:
#    print("Invalid record:", error)

# ===================================================================
# PART D Validation
# ===================================================================
#p = Point("A", 121.0, 14.6)
#print(p.bbox())

# ===================================================================
# PART E Validation
# ===================================================================
attributes = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

parcel = Parcel(101, geom, attributes)
print(parcel.bbox())
print(parcel.as_dict())

inside = Point("IN", 2, 2)
outside = Point("OUT", 12, 2)

print(inside.intersects(parcel)) # True
print(outside.intersects(parcel)) # False