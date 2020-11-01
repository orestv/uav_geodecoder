import datetime
from dataclasses import dataclass

import pytest
import typing

from pytest_mock import MockerFixture

import lib


@dataclass
class GPXTestCase:
    gpx_contents: str
    point_count: int
    starting_point: lib.GPXPoint
    start_time = datetime.datetime.fromisoformat("2020-08-23T07:43:02.100+00:00")
    end_time = datetime.datetime.fromisoformat("2020-08-23T07:43:02.600+00:00")


@pytest.fixture
def gpx_test(gpx_contents: str) -> GPXTestCase:
    return GPXTestCase(
        gpx_contents=gpx_contents,
        point_count=5,
        starting_point=lib.GPXPoint(49.2351317723592, 28.4581775814941,
                                    datetime.datetime.fromisoformat("2020-08-23T07:43:02.100+00:00"))
    )


@pytest.fixture
def gpx_tracks(gpx_contents, gpx_contents_2):
    return [
        lib.GPXLoader(gpx_contents).track_data,
        lib.GPXLoader(gpx_contents_2).track_data
    ]


@pytest.fixture
def gpx_db(gpx_tracks) -> lib.GPXDatabase:
    return lib.GPXDatabase(gpx_tracks)


def test_gpx_loader_correct_gpx_loaded(gpx_test: GPXTestCase):
    assert hasattr(lib, "GPXLoader")
    loader = lib.GPXLoader(gpx_test.gpx_contents)

    actual_data = loader.track_data
    assert isinstance(actual_data, lib.GPXTrackData)
    assert len(actual_data.points) == gpx_test.point_count
    assert actual_data.starting_point == gpx_test.starting_point
    assert actual_data.start_time == gpx_test.start_time
    assert actual_data.end_time == gpx_test.end_time


def test_gpx_movie_points(gpx_db: lib.GPXDatabase):
    movie_time = lib.TimePeriod(
        datetime.datetime.fromisoformat("2020-08-23T07:43:02.200+00:00"),
        datetime.datetime.fromisoformat("2020-08-23T07:43:02.400+00:00"),
    )
    expected_movie_location = lib.MovieLocation(
        points=[
            lib.GPXPoint(longitude=28.4581776455937, latitude=49.2351316601347,
                         time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.200+00:00")),
            lib.GPXPoint(longitude=28.4581777713502, latitude=49.235131395275,
                         time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.300+00:00")),
            lib.GPXPoint(longitude=28.458177902354, latitude=49.2351312680944,
                         time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.400+00:00")),
        ]
    )
    actual_movie_location = gpx_db.get_movie_location(movie_time)
    assert actual_movie_location == expected_movie_location
