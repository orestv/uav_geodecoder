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


@pytest.fixture
def gpx_test(gpx_contents: str) -> GPXTestCase:
    return GPXTestCase(
        gpx_contents=gpx_contents,
        point_count=5,
        starting_point=lib.GPXPoint(49.2351317723592, 28.4581775814941)
    )


def test_gpx_loader_correct_point_count(gpx_test: GPXTestCase):
    assert hasattr(lib, "GPXLoader")
    loader = lib.GPXLoader(gpx_test.gpx_contents)

    actual_data = loader.track_data
    assert isinstance(actual_data, lib.GPXTrackData)
    assert len(actual_data.points) == gpx_test.point_count
    assert actual_data.points[0] == gpx_test.starting_point


