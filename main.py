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
    for movie_fname in os.listdir(movies_path):
        if not movie_fname.endswith(".MP4"):
            continue
        movie_path = os.path.join(movies_path, movie_fname)

        movie_period = lib.MovieParser(movie_path).get_period()
        logging.info("Movie is %s - %s", movie_period.start, movie_period.end)
        movie_location = gpx_db.get_movie_location(movie_time=movie_period)
        # logging.info("Movie located at %s", movie_location)
        try:
            poi = lib.POILocator(lib.GEOLocator()).get_poi(movie_location)
        except Exception as e:
            logging.info("Failed to get POI: no points")
            continue
        logging.info("Movie POI is %s", poi)


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


if __name__ == '__main__':
    generate_movie_subtitles()
