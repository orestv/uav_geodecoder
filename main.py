import typing

import click

import lib


def get_gpx_paths(root: str) -> typing.List[str]:
    pass


@click.command()
@click.argument("movie_filename", type=click.Path)
def generate_movie_subtitles(movie_filename: str):
    gpx_paths = get_gpx_paths(".")
    gpx_db = lib.GPXDatabase(gpx_paths)
    movie_parser = lib.MovieParser(movie_filename)
    movie_location_data = gpx_db.get_location_data(movie_parser.get_period())
    subtitle_generator = lib.SubtitleGenerator(
        movie_parser.get_subtitle_metadata()
    )
    subtitle_generator.write_subtitles(
        movie_location_data,
        movie_filename
    )


if __name__ == '__main__':
    generate_movie_subtitles()
