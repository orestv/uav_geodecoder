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
