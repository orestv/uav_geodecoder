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
        starting_point=lib.GPXPoint(49.2351317723592, 28.4581775814941, datetime.datetime.fromisoformat("2020-08-23T07:43:02.100+00:00"))
    )


def test_gpx_loader_correct_gpx_loaded(gpx_test: GPXTestCase):
    assert hasattr(lib, "GPXLoader")
    loader = lib.GPXLoader(gpx_test.gpx_contents)

    actual_data = loader.track_data
    assert isinstance(actual_data, lib.GPXTrackData)
    assert len(actual_data.points) == gpx_test.point_count
    assert actual_data.starting_point == gpx_test.starting_point
    assert actual_data.start_time == gpx_test.start_time
    assert actual_data.end_time == gpx_test.end_time


