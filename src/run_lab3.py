from spatial import Point, Parcel
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import pandas as pd
import os
import json


# ==================================================
# FILE PATHS
# ==================================================

DATA_PATH = "data/points.csv"
OUTPUT_DIR = "output"
REPORT_PATH = os.path.join(OUTPUT_DIR, "lab3_report.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "lab3_preview.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)


def main():

    # ==================================================
    # F.1 LOAD POINT DATA
    # ==================================================

    try:
        df = pd.read_csv(DATA_PATH)

    except FileNotFoundError:
        print(f"Error: Cannot find file at '{DATA_PATH}'.")
        print("Make sure you have: data/points.csv")
        raise

    print(f"Loaded {len(df)} points from {DATA_PATH}.")


    # ==================================================
    # CONVERT CSV ROWS INTO POINT OBJECTS
    # ==================================================

    points = []

    for _, row in df.iterrows():
        point = Point(
            row["id"],
            float(row["lon"]),
            float(row["lat"]),
            name=row["name"],
            tag=row["tag"]
        )

        points.append(point)

    print(f"Created {len(points)} Point objects.")


    # ==================================================
    # F.1 CONSTRUCT PARCEL USING CSV COORDINATES
    # ==================================================

    center_point = points[0]

    lon = center_point.geometry.x
    lat = center_point.geometry.y

    offset = 0.001

    geom = Polygon([
        (lon - offset, lat - offset),
        (lon + offset, lat - offset),
        (lon + offset, lat + offset),
        (lon - offset, lat + offset)
    ])

    attributes = {
        "area": None,
        "zone": "Demonstration Parcel",
        "is_active": True
    }

    parcel = Parcel(
        101,
        geom,
        attributes
    )


    # ==================================================
    # F.2 EVALUATE RELATIONSHIP OF EVERY POINT
    # ==================================================

    print("\n=== POINT-PARCEL RELATIONSHIPS ===")

    relationships = {}

    for point in points:

        intersects = point.intersects(parcel)

        if intersects:
            status = "IN"
        else:
            status = "OUT"

        relationships[
            f"{point.id}_intersects_parcel"
        ] = intersects

        print(
            f"{point.id} ({point.name}): "
            f"{status} - intersects = {intersects}"
        )


    # ==================================================
    # BUILD POINT DATA
    # ==================================================

    point_data = {}

    for point in points:

        point_data[point.id] = {
            "id": point.id,
            "name": point.name,
            "tag": point.tag,

            "geometry": [
                point.geometry.x,
                point.geometry.y
            ],

            "bbox": list(
                point.bbox()
            )
        }


    # ==================================================
    # F.2 BUILD JSON REPORT
    # ==================================================

    report = {
        "point": point_data,

        "parcel": parcel.as_dict(),

        "relationships": relationships
    }


    # ==================================================
    # WRITE JSON REPORT
    # ==================================================

    with open(
        REPORT_PATH,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            indent=4
        )

    print(
        f"\nSaved report to: {REPORT_PATH}"
    )


    # ==================================================
    # F.3 CREATE VISUALIZATION
    # ==================================================

    plt.figure()

    parcel_x, parcel_y = (
        parcel.geometry.exterior.xy
    )

    plt.plot(
        parcel_x,
        parcel_y
    )

    for point in points:

        intersects = point.intersects(
            parcel
        )

        if intersects:
            status = "IN"
        else:
            status = "OUT"

        plt.scatter(
            point.geometry.x,
            point.geometry.y
        )

        plt.text(
            point.geometry.x,
            point.geometry.y,
            f" {point.id} - {status}"
        )


    plt.title(
        "Lab 3: Parcel and Point Relationships"
    )

    plt.xlabel(
        "Longitude"
    )

    plt.ylabel(
        "Latitude"
    )

    plt.savefig(
        PLOT_PATH,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()

    print(
        f"Saved preview plot to: {PLOT_PATH}"
    )


if __name__ == "__main__":
    main()