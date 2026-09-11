from shapely.geometry import Point as ShapelyPoint
import math


class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")

        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        self.id = id
        self.geometry = ShapelyPoint(lon, lat)
        self.name = name
        self.tag = tag

    @property
    def lon(self):
        return self.geometry.x

    @property
    def lat(self):
        return self.geometry.y

    def to_tuple(self):
        return (self.lon, self.lat)

    def distance_to(self, other):
        return Point.haversine_m(
            self.lon,
            self.lat,
            other.lon,
            other.lat
        )

    @staticmethod
    def haversine_m(lon1, lat1, lon2, lat2):
        R = 6_371_000.0

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)

        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
            math.sin(dphi / 2) ** 2
            + math.cos(phi1)
            * math.cos(phi2)
            * math.sin(dlambda / 2) ** 2
        )

        c = 2 * math.atan2(
            math.sqrt(a),
            math.sqrt(1 - a)
        )

        return R * c

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            d["id"],
            float(d["lon"]),
            float(d["lat"]),
            name=d.get("name"),
            tag=d.get("tag")
        )

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tag": self.tag,
            "geometry": [self.lon, self.lat],
            "bbox": list(self.geometry.bounds)
        }