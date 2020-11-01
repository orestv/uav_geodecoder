import pytest


@pytest.fixture
def gpx_contents() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="Airdata.com"
 xsi:schemaLocation="https://app.airdata.com/gpx_files/GPX/1/1 https://app.airdata.com/gpx_files/GPX/1/1/gpx.xsd https://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3 https://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3/GpxExtensionsv3.xsd https://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1 https://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1/TrackPointExtensionv1.xsd"
 xmlns="http://www.topografix.com/GPX/1/1"
 xmlns:gpxtpx="http://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1"
 xmlns:gpxx="http://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <trk>
    <name>2020-08-23-10-43-02-Flight-Airdata</name>
    <trkseg>
        <trkpt lon="28.4581775814941" lat="49.2351317723592">
            <ele>276.6492615</ele>
            <speed>0.00</speed>
            <time>2020-08-23T07:43:02.100Z</time>
        </trkpt>
        <trkpt lon="28.4581776455937" lat="49.2351316601347">
            <ele>276.6492615</ele>
            <speed>0.00</speed>
            <time>2020-08-23T07:43:02.200Z</time>
        </trkpt>
        <trkpt lon="28.4581777713502" lat="49.235131395275">
            <ele>276.6492615</ele>
            <speed>0.00</speed>
            <time>2020-08-23T07:43:02.300Z</time>
        </trkpt>
        <trkpt lon="28.458177902354" lat="49.2351312680944">
            <ele>276.6492615</ele>
            <speed>0.00</speed>
            <time>2020-08-23T07:43:02.400Z</time>
        </trkpt>
        <trkpt lon="28.4581783196061" lat="49.2351307242361">
            <ele>276.6492615</ele>
            <speed>0.00</speed>
            <time>2020-08-23T07:43:02.600Z</time>
        </trkpt>
    </trkseg>
  </trk>
</gpx>
"""


@pytest.fixture
def gpx_contents_2():
    return """<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="Airdata.com"
 xsi:schemaLocation="https://app.airdata.com/gpx_files/GPX/1/1 https://app.airdata.com/gpx_files/GPX/1/1/gpx.xsd https://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3 https://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3/GpxExtensionsv3.xsd https://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1 https://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1/TrackPointExtensionv1.xsd"
 xmlns="http://www.topografix.com/GPX/1/1"
 xmlns:gpxtpx="http://app.airdata.com/gpx_files/xmlschemas/TrackPointExtension/v1"
 xmlns:gpxx="http://app.airdata.com/gpx_files/xmlschemas/GpxExtensions/v3"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <trk>
    <name>2020-08-23-12-36-53-Flight-Airdata</name>
    <trkseg>
    
			<trkpt lon="27.708359051961" lat="49.4775612353537">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.100Z</time>
			</trkpt>
			<trkpt lon="27.7083590765339" lat="49.4775612572413">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.200Z</time>
			</trkpt>
			<trkpt lon="27.7083590723588" lat="49.4775611812582">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.300Z</time>
			</trkpt>
			<trkpt lon="27.7083590832049" lat="49.4775612029395">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.400Z</time>
			</trkpt>
			<trkpt lon="27.708359075693" lat="49.4775611492685">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.500Z</time>
			</trkpt>
			<trkpt lon="27.7083590906078" lat="49.4775611607134">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.600Z</time>
			</trkpt>
			<trkpt lon="27.7083589214513" lat="49.4775612767829">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.700Z</time>
			</trkpt>
			<trkpt lon="27.7083589184853" lat="49.4775612974664">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.800Z</time>
			</trkpt>
			<trkpt lon="27.7083589250721" lat="49.4775614029315">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:53.900Z</time>
			</trkpt>
			<trkpt lon="27.7083589304429" lat="49.4775614224571">
				<ele>272.3792419</ele>
				<speed>0.00</speed>
				<time>2020-08-23T09:36:54.000Z</time>
			</trkpt>
    </trkseg>
  </trk>
</gpx>"""
