# UAV Video Geocoder

Generate sensible subtitles for movies shot from my drone.

It: 
- loads the flight .gpx tracks from a directory 
- iterates over MP4 files in another directory
- matches the video with the tracks by time and finds the location of each video
- queries a geolocation API to find a PoI name for that video
- writes .srt subtitles for each video.

All useful code is in `lib`.

## Usage

Install ffmpeg.

`python3 -m pip install requirements.txt`
`python3 main.py --movies_path /home/user/movies --gpx_path /home/user/gpx`

## Testing

Install `pytest`. Run `pytest` in root.
