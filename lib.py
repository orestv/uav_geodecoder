import datetime
from dataclasses import dataclass

import typing

import gpxpy


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
class MovieLocationData:
    nearest_location_name: str


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
    def __init__(self, gpx_files: typing.List[str]):
        pass

    def get_location_data(self, period: TimePeriod) -> MovieLocationData:
        pass


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

    def write_subtitles(self, movie_location_data: MovieLocationData, movie_path: str):
        pass
