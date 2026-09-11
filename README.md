# *GmE 205 Laboratory 3 — Spatial Object Systems in Python*

The main objective of this laboratory activity is to refactor the spatial object model from Laboratory 2 by using Shapely for geometry storage, introducing a shared `SpatialObject` base class, and creating structured input and output boundaries while preserving the meaning and responsibilities of each object.

### Objectives

The objectives of this laboratory are to:

- Refactor `Point` so that Shapely stores its geometry while preserving coordinate validation and public access to longitude and latitude.
- Use dictionaries as structured input and output without treating them as the domain objects themselves.
- Introduce a `SpatialObject` base class for shared spatial behavior such as bounding boxes and intersections.
- Implement `Parcel` as another spatial type that shares common spatial behavior with `Point`.
- Generate reproducible JSON and visualization outputs and verify the model through focused tests.

### Tools and Technologies

The following tools were used:

- *Python 3.x*
- *Visual Studio Code*
- *Git*
- *GitHub*
- *Shapely*
- *Pandas*
- *Matplotlib*

### How to set up the virtual environment

1. Open the project folder (`gme205-lab3`) in VS Code.
2. Open the terminal (`Terminal -> New Terminal`) and create the virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Confirm that the terminal prompt shows `(.venv)`.
4. Select the interpreter inside `.venv` using `Ctrl + Shift + P -> Python: Select Interpreter`.
5. Install the required packages and update `requirements.txt`:

```bash
pip install pandas matplotlib shapely
pip freeze > requirements.txt
```

## Reflection

#### Refactoring

The `Point` class was restructured internally, longitude and latitude are no longer stored as separate values. They now live inside a Shapely `Point` object, which gets passed up to the `SpatialObject` base class. Despite this change, anything using the object still works the same way. `p.lon`, `p.lat`, and `p.to_tuple()` can still be accessed through properties that read from `geometry.x` and `geometry.y`.

> **Key idea:** The internal storage changed, but nothing about how external code interacts with `Point` had to change.

#### Responsibility

Each class handles what it's actually meant for. Shapely takes care of storing geometry and running geometric operations. `SpatialObject` holds behavior that both spatial types share, while `Point` and `Parcel` each keep their own specific logic. `Point` still handles coordinate validation, lat/lon access, Haversine distance, and point-specific attributes, whereas `Parcel` stays focused on its `parcel_id` and parcel-related data.

> **Responsibility rule:** Shapely owns geometry, `SpatialObject` owns shared spatial behavior, and each subclass owns its own domain logic.

#### Data Boundary

`from_dict()` passes everything straight to the constructor rather than re-implementing validation itself. This keeps coordinate checks in one place. Whether a `Point` is created directly or from a dictionary, the constructor always validates the input.

> **Data boundary:** `from_dict()` handles reading external data; the constructor is the single place where validation happens.

#### Output Boundary

`as_dict()` returns plain values, such as strings, numbers, and lists, rather than exposing the Shapely object directly. This makes the output easier to inspect, serialize to JSON, or pass to another system without exposing the underlying implementation.

> **Output boundary:** Domain objects describe themselves using simple, portable values that are safe to write to files or send across systems.

#### Inheritance

`intersects()` lives in `SpatialObject` because intersection isn't specific to points or parcels, so it makes more sense to keep the method in one shared class instead of repeating it in each one. Both `Point` and `Parcel` inherit from `SpatialObject`, so they both get this method without either one duplicating it.

> **Inheritance rule:** Behavior shared across types belongs in the base class once, not scattered across subclasses.

#### Coordinate Meaning

Shapely's `geometry.distance()` works in a flat Cartesian space using the coordinates provided to it. When those coordinates are longitude and latitude, the result is expressed in degrees rather than meters. This is why the Haversine method from Lab 2 is still retained. Shapely handles planar geometry operations, while the model remains responsible for interpreting what the coordinates represent and which units are appropriate.

> **Coordinate meaning:** A geometry library will calculate distance correctly for its coordinate space, but it's the model's job to know what that space is and what the numbers mean.

#### Scale

Using `SpatialObject`, inheritance, and clear input or output boundaries keeps things maintainable. Shared behavior lives in one place, and each class has a clear job. That said, if the system ever grows to millions of spatial objects, looping through them one by one won't cut it. At that point, spatial indexing, chunked processing, database-backed storage, and more efficient query strategies would be needed.

> **Scale insight:** Clean object design keeps code readable and maintainable, but real-world scale demands more than good structure alone.
