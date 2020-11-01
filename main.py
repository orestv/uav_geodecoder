import typing

import click

import lib


def get_gpx_paths(root: str) -> typing.List[str]:
    pass


@click.command()
@click.argument("movie_filename", type=click.Path)
def generate_movie_subtitles():
    gpx_paths = get_gpx_paths(".")
    gpx_db = lib.GPXDatabase(gpx_paths)


if __name__ == '__main__':
    generate_movie_subtitles()
