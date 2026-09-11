import unittest
import sys
import os

# Allow tests to import spatial.py from src/
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "src")
    )
)

from spatial import Point, Parcel
from shapely.geometry import Polygon
from shapely.geometry.base import BaseGeometry


class TestSpatialObjects(unittest.TestCase):

    # ==================================================
    # TEST 1 - Valid Point
    # ==================================================
    def test_valid_point(self):
        p = Point("A", 121.0, 14.6)

        self.assertEqual(p.id, "A")
        self.assertEqual(p.geometry.x, 121.0)
        self.assertEqual(p.geometry.y, 14.6)


    # ==================================================
    # TEST 2 - Invalid Longitude
    # ==================================================
    def test_invalid_longitude(self):

        with self.assertRaises(ValueError):
            Point("BAD", 999, 14.6)


    # ==================================================
    # TEST 3 - from_dict() Valid Record
    # ==================================================
    def test_from_dict_valid(self):

        record = {
            "id": "A",
            "lon": 121.0,
            "lat": 14.6,
            "name": "Gate",
            "tag": "POI"
        }

        p = Point.from_dict(record)

        self.assertIsInstance(p, Point)
        self.assertEqual(p.id, "A")


    # ==================================================
    # TEST 4 - from_dict() Invalid Record
    # ==================================================
    def test_from_dict_invalid(self):

        invalid_record = {
            "id": "BAD",
            "lon": 999,
            "lat": 14.6
        }

        with self.assertRaises(ValueError):
            Point.from_dict(invalid_record)


    # ==================================================
    # TEST 5 - Point Bounding Box
    # ==================================================
    def test_point_bbox(self):

        p = Point("A", 121.0, 14.6)

        self.assertEqual(
            p.bbox(),
            (121.0, 14.6, 121.0, 14.6)
        )


    # ==================================================
    # TEST 6 - Parcel Bounding Box
    # ==================================================
    def test_parcel_bbox(self):

        geom = Polygon([
            (0, 0),
            (10, 0),
            (10, 5),
            (0, 5)
        ])

        parcel = Parcel(
            101,
            geom,
            {"zone": "Residential"}
        )

        self.assertEqual(
            parcel.bbox(),
            (0.0, 0.0, 10.0, 5.0)
        )


    # ==================================================
    # TEST 7 - Inside Point Intersects Parcel
    # ==================================================
    def test_inside_intersects(self):

        geom = Polygon([
            (0, 0),
            (10, 0),
            (10, 5),
            (0, 5)
        ])

        parcel = Parcel(
            101,
            geom,
            {"zone": "Residential"}
        )

        inside = Point("IN", 2, 2)

        self.assertTrue(
            inside.intersects(parcel)
        )


    # ==================================================
    # TEST 8 - Outside Point Does Not Intersect
    # ==================================================
    def test_outside_intersects(self):

        geom = Polygon([
            (0, 0),
            (10, 0),
            (10, 5),
            (0, 5)
        ])

        parcel = Parcel(
            101,
            geom,
            {"zone": "Residential"}
        )

        outside = Point("OUT", 12, 2)

        self.assertFalse(
            outside.intersects(parcel)
        )


    # ==================================================
    # TEST 9 - as_dict() Has No Shapely Object
    # ==================================================
    def test_as_dict_json_ready(self):

        p = Point(
            "A",
            121.0,
            14.6,
            name="Gate",
            tag="POI"
        )

        data = p.as_dict()

        for value in data.values():
            self.assertFalse(
                isinstance(value, BaseGeometry)
            )


if __name__ == "__main__":
    unittest.main()