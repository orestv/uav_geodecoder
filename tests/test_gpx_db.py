import datetime
from dataclasses import dataclass

import pytest
import typing

from pytest_mock import MockerFixture, mock

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


@pytest.fixture
def mocked_geolocator(mocker: MockerFixture):
    return mocker.Mock()


def test_gpx_loader_correct_gpx_loaded(gpx_test: GPXTestCase):
    assert hasattr(lib, "GPXLoader")
    loader = lib.GPXLoader(gpx_test.gpx_contents)

    actual_data = loader.track_data
    assert isinstance(actual_data, lib.GPXTrackData)
    assert len(actual_data.points) == gpx_test.point_count
    assert actual_data.starting_point == gpx_test.starting_point
    assert actual_data.start_time == gpx_test.start_time
    assert actual_data.end_time == gpx_test.end_time


@pytest.mark.parametrize(
    "movie_time,expected_movie_location",
    [
        (
                lib.TimePeriod(
                    datetime.datetime.fromisoformat("2020-08-23T07:43:02.200+00:00"),
                    datetime.datetime.fromisoformat("2020-08-23T07:43:02.400+00:00"),
                ),
                lib.MovieLocation(
                    points=[
                        lib.GPXPoint(longitude=28.4581776455937, latitude=49.2351316601347,
                                     time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.200+00:00")),
                        lib.GPXPoint(longitude=28.4581777713502, latitude=49.235131395275,
                                     time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.300+00:00")),
                        lib.GPXPoint(longitude=28.458177902354, latitude=49.2351312680944,
                                     time=datetime.datetime.fromisoformat("2020-08-23T07:43:02.400+00:00")),
                    ]
                )
        ),
        (
                lib.TimePeriod(
                    datetime.datetime.fromisoformat("2020-08-23T09:36:53.301+00:00"),
                    datetime.datetime.fromisoformat("2020-08-23T09:36:54.000+00:00"),
                ),
                lib.MovieLocation(
                    points=[
                        lib.GPXPoint(longitude=27.7083590832049, latitude=49.4775612029395,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.400+00:00")),
                        lib.GPXPoint(longitude=27.708359075693, latitude=49.4775611492685,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.500+00:00")),
                        lib.GPXPoint(longitude=27.7083590906078, latitude=49.4775611607134,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.600+00:00")),
                        lib.GPXPoint(longitude=27.7083589214513, latitude=49.4775612767829,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.700+00:00")),
                        lib.GPXPoint(longitude=27.7083589184853, latitude=49.4775612974664,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.800+00:00")),
                        lib.GPXPoint(longitude=27.7083589250721, latitude=49.4775614029315,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:53.900+00:00")),
                        lib.GPXPoint(longitude=27.7083589304429, latitude=49.4775614224571,
                                     time=datetime.datetime.fromisoformat("2020-08-23T09:36:54.000+00:00")),
                    ]
                )
        )
    ]
)
def test_gpx_movie_points(gpx_db: lib.GPXDatabase, movie_time, expected_movie_location):
    actual_movie_location = gpx_db.get_movie_location(movie_time)
    assert actual_movie_location == expected_movie_location


def test_get_poi(mocked_geolocator: mock.Mock, movie_location: lib.MovieLocation):
    locator = lib.POILocator(mocked_geolocator)

    expected_poi = lib.POI(city="Lviv")
    mocked_geolocator.get_poi.return_value = expected_poi

    actual_poi = locator.get_poi(movie_location)
    assert actual_poi == expected_poi

    mocked_geolocator.get_poi.assert_called_with(movie_location.points[0])


def test_get_poi_for_point(mocker: MockerFixture):
    point = lib.GPXPoint(49.2351317723592, 28.4581775814941, datetime.datetime.utcnow())
    mocked_response = {'country_code': 'UA', 'city': 'Lviv', 'country': 'Ukraine'}
    mocker.patch("reverse_geocode.get").return_value = mocked_response

    expected_poi = lib.POI(city="Lviv")

    actual_poi = lib.GEOLocator().get_poi(point)
    assert actual_poi == expected_poi


def test_get_movie_period(mocker: MockerFixture):
    movie_path = "mock_path"
    parser = lib.MovieParser(movie_path)

    mock_fprobe_response = """[FORMAT]
filename=DJI_0257.MP4
nb_streams=1
nb_programs=0
format_name=mov,mp4,m4a,3gp,3g2,mj2
format_long_name=QuickTime / MOV
start_time=0.000000
duration=51.285000
size=664271893
bit_rate=103620457
probe_score=100
TAG:major_brand=isom
TAG:minor_version=512
TAG:compatible_brands=isomiso2avc1mp41
TAG:creation_time=2020-08-20T12:34:45.000000Z
TAG:encoder=Lavf56.15.102
[/FORMAT]"""
    mocker.patch.object(parser, "_get_fprobe").return_value = mock_fprobe_response
    expected_period = lib.TimePeriod(
        datetime.datetime.fromisoformat("2020-08-20T12:34:45.000000+00:00"),
        datetime.datetime.fromisoformat("2020-08-20T12:35:36.285000+00:00")
    )

    actual_period = parser.get_period()

    assert expected_period == actual_period


def test_parse_fprobe():
    fprobe_output = """[FORMAT]
filename=DJI_0257.MP4
nb_streams=1
nb_programs=0
format_name=mov,mp4,m4a,3gp,3g2,mj2
format_long_name=QuickTime / MOV
start_time=0.000000
duration=51.285000
size=664271893
bit_rate=103620457
probe_score=100
TAG:major_brand=isom
TAG:minor_version=512
TAG:compatible_brands=isomiso2avc1mp41
TAG:creation_time=2020-08-20T12:34:45.000000Z
TAG:encoder=Lavf56.15.102
[/FORMAT]"""
    parser = lib.MovieParser("")
    parsed_fprobe = parser._parse_fprobe(fprobe_output)

    assert parsed_fprobe["filename"] == "DJI_0257.MP4"
    assert parsed_fprobe["TAG:creation_time"] == "2020-08-20T12:34:45.000000Z"
