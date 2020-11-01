import datetime
import itertools
import os
import subprocess
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


class GEOLocator:
    def get_poi(self, point: GPXPoint) -> POI:
        lookup_result = reverse_geocode.get(
            (point.longitude, point.latitude)
        )
        return POI(city=lookup_result["city"])


class POILocator:
    def __init__(self, geolocator: GEOLocator):
        self.geolocator = geolocator

    def get_poi(self, movie_location: MovieLocation) -> POI:
        first_point = movie_location.points[0]
        return self.geolocator.get_poi(first_point)


class MovieParser:
    def __init__(self, movie_path):
        self.movie_path = movie_path

    def get_period(self) -> TimePeriod:
        fprobe = self._get_fprobe()
        parsed_fprobe = self._parse_fprobe(fprobe)
        return self._get_time_period(parsed_fprobe)

    def _get_time_period(self, parsed_fprobe: typing.Dict[str, str]) -> TimePeriod:
        s_creation_time = parsed_fprobe["TAG:creation_time"]
        s_duration_seconds = parsed_fprobe["duration"]

        s_creation_time_isoformat = s_creation_time.replace("Z", "+00:00")
        delta = datetime.timedelta(seconds=float(s_duration_seconds))
        start = datetime.datetime.fromisoformat(s_creation_time_isoformat)
        end = start + delta
        return TimePeriod(start, end)

    def _get_fprobe(self) -> str:
        """ffprobe -v error -show_format DJI_0257.MP4"""
        cmd = f'ffprobe -i "{self.movie_path}" -show_format'
        output = subprocess.check_output(
            cmd,
            shell=True,  # Let this run in the shell
            stderr=subprocess.STDOUT
        )
        return output.decode("utf-8")

    def _parse_fprobe(self, fprobe: str) -> dict:
        result = {}
        for line in fprobe.split(os.linesep):
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            result[key] = value
        return result

    def get_subtitle_metadata(self) -> SubtitleMetadata:
        pass


class SubtitleGenerator:
    def __init__(self, subtitle_metadata: SubtitleMetadata):
        pass

    # todo: add another layer before this to convert MovieLocation into something verbose.
    def write_subtitles(self, movie_location: MovieLocation, movie_path: str):
        pass
