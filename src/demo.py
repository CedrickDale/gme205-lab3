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

# ==================================================
# PART H - CHALLENGE 1: DATA TO OBJECT BOUNDARY
# ==================================================

# Valid record
valid_record = {
    "id": "C1",
    "lon": 121.0,
    "lat": 14.6,
    "name": "Challenge Point",
    "tag": "POI"
}

challenge_point = Point.from_dict(valid_record)

print("\n======================================")
print("CHALLENGE 1: DATA TO OBJECT")
print("======================================")
print("Valid Point:")
print("ID:", challenge_point.id)
print("Coordinates:", challenge_point.to_tuple())


# Invalid record
invalid_record = {
    "id": "C2",
    "lon": 999,
    "lat": 14.6
}

try:
    Point.from_dict(invalid_record)

except ValueError as error:
    print("\nInvalid Point:")
    print("ID:", invalid_record["id"])
    print(error)

# ==================================================
# PART H - CHALLENGE 2: OBJECT TO STRUCTURED OUTPUT
# ==================================================

point = Point(
    "C3",
    121.0,
    14.6,
    name="Challenge Point",
    tag="POI"
)
print("\n======================================")
print("CHALLENGE 2: OBJECT TO DATA")
print("======================================")
print("Point as dictionary:")
print(point.as_dict())

parcel_attributes = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}

parcel_geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

parcel = Parcel(
    201,
    parcel_geom,
    parcel_attributes
)

print("\nParcel as dictionary:")
print(parcel.as_dict())

print("\n==============================================")
print("CHALLENGE 3: SHARED SPATIAL BEHAVIOR")
print("==============================================")

parcel_geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

parcel = Parcel(
    301,
    parcel_geom,
    {
        "area": 50.0,
        "zone": "Residential",
        "is_active": True
    }
)

inside = Point("IN", 2, 2)
outside = Point("OUT", 12, 2)

print(
    "Inside point intersects parcel:",
    inside.intersects(parcel)
)

print(
    "Outside point intersects parcel:",
    outside.intersects(parcel)
)

print(
    "Parcel intersects inside point:",
    parcel.intersects(inside)
)

print(
    "Parcel intersects outside point:",
    parcel.intersects(outside)
)