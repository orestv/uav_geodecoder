import datetime
from dataclasses import dataclass

import typing


@dataclass
class MovieDetails:
    pass


@dataclass
class TimePeriod:
    start: datetime.datetime
    end: datetime.datetime


@dataclass
class MovieLocationData:
    nearest_location_name: str


class GPXDatabase:
    def __init__(self, gpx_files: typing.List[str]):
        pass

    def get_location_data(self, period: TimePeriod) -> MovieLocationData:
        pass


class Movie
