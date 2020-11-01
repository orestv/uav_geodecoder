import itertools
import os, sys
import logging
import concurrent.futures

import click

import lib


def load_gpx(p):
    logging.info("Reading %s", p)
    with open(p) as f:
        contents = f.read()
    logging.info("Contents read, parsing")
    loader = lib.GPXLoader(contents)
    return loader


def get_gpx_db(root: str) -> lib.GPXDatabase:
    import pickle
    try:
        with open("db.pickle", "rb") as f:
            return pickle.load(f)
    except Exception as e:
        logging.exception(e)
    tracks = list()
    paths = [
        os.path.join(root, fname)
        for fname in os.listdir(root)
    ]

    executor = concurrent.futures.ProcessPoolExecutor(4)
    loaders = executor.map(load_gpx, paths)

    tracks = [
        loader.track_data for loader in loaders
    ]

    db = lib.GPXDatabase(tracks)
    with open("db.pickle", "wb") as f:
        pickle.dump(db, f)
    return db


@click.command()
@click.argument("movies_path", type=click.Path())
@click.argument("gpx_path", type=click.Path())
def generate_movie_subtitles(movies_path: str, gpx_path: str):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
    )
    gpx_db = get_gpx_db(gpx_path)
    movie_paths = [
        os.path.join(movies_path, f)
        for f in os.listdir(movies_path)
        if f.endswith(".MP4")
    ]

    executor = concurrent.futures.ProcessPoolExecutor(8)
    pois = executor.map(
        get_movie_poi,
        itertools.repeat(gpx_db),
        movie_paths
    )

    for path, poi in zip(movie_paths, pois):
        logging.info("Shot in %s: %s", poi, path)

    #     print(movie_fname)
    #
    # gpx_db = lib.GPXDatabase(gpx_paths)
    # movie_parser = lib.MovieParser(movie_filename)
    # movie_location_data = gpx_db.get_location_data(movie_parser.get_period())
    # subtitle_generator = lib.SubtitleGenerator(
    #     movie_parser.get_subtitle_metadata()
    # )
    # subtitle_generator.write_subtitles(
    #     movie_location_data,
    #     movie_filename
    # )


def get_movie_poi(gpx_db, movie_path):
    logging.info("Parsing %s", movie_path)
    movie_period = lib.MovieParser(movie_path).get_period()
    logging.info("Movie is %s - %s", movie_period.start, movie_period.end)
    movie_location = gpx_db.get_movie_location(movie_time=movie_period)
    if not movie_location:
        return None
    poi = lib.POILocator(lib.GEOLocator()).get_poi(movie_location)
    return poi


if __name__ == '__main__':
    generate_movie_subtitles()
