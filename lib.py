import datetime
import itertools
from dataclasses import dataclass

import typing

import gpxpy
import reverse_geocode


@dataclass
class MovieDetails:
    pass


@dataclass
class GPXPoint:
    latitude: float
    longitude: float
    time: datetime.datetime


@dataclass
class GPXTrackData:
    points: typing.List[GPXPoint]
    starting_point: GPXPoint
    start_time: datetime.datetime
    end_time: datetime.datetime


@dataclass
class TimePeriod:
    start: datetime.datetime
    end: datetime.datetime


@dataclass
class SubtitleMetadata:
    pass


@dataclass
class POI:
    city: str


@dataclass
class MovieLocation:
    points: typing.List[GPXPoint]


class GPXLoader:
    def __init__(self, gpx_contents: str):
        self.gpx_contents = gpx_contents
        self._parsed_gpx = gpxpy.parse(self.gpx_contents)

    @property
    def track_data(self) -> GPXTrackData:
        gpx_points = self._parsed_gpx.tracks[0].segments[0].points
        points = [
            GPXPoint(p.latitude, p.longitude, p.time)
            for p in gpx_points
        ]
        return GPXTrackData(
            points=points,
            starting_point=points[0],
            start_time=points[0].time,
            end_time=points[-1].time,
        )


class GPXDatabase:
    def __init__(self, tracks: typing.List[GPXTrackData]):
        self.tracks = tracks
        chained_tracks: typing.Iterable[GPXPoint] = itertools.chain(*(t.points for t in self.tracks))
        self.chained_tracks: typing.Iterable[GPXPoint] = sorted(chained_tracks, key=lambda p: p.time)

    def get_movie_location(self, movie_time: TimePeriod) -> MovieLocation:
        matching_points = [
            p
            for p in self.chained_tracks
            if movie_time.start <= p.time <= movie_time.end
        ]
        return MovieLocation(
            points=matching_points
        )


class POILocator:
    def get_poi(self, movie_location: MovieLocation) -> POI:
        first_point = movie_location.points[0]
        lookup_result = reverse_geocode.get(
            (first_point.longitude, first_point.latitude)
        )
        return POI(city=lookup_result["city"])


class MovieParser:
    def __init__(self, movie_file_path):
        pass

    def get_period(self) -> TimePeriod:
        pass

    def get_subtitle_metadata(self) -> SubtitleMetadata:
        pass


class SubtitleGenerator:
    def __init__(self, subtitle_metadata: SubtitleMetadata):
        pass

    # todo: add another layer before this to convert MovieLocation into something verbose.
    def write_subtitles(self, movie_location: MovieLocation, movie_path: str):
        pass
