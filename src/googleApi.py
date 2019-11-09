import urllib.request, urllib.error
import settings
import json

# document
# https://developers.google.com/maps/documentation/distance-matrix/intro?hl=ja
class GoogleAPI:
    def FetchDistanceFromGoogleApi(self, departure, destination):
        # create query parameters
        params = {
            'origins': departure,
            'destinations': destination,
            'mode': 'walking',
            'language': 'ja-JP',
            'key': settings.GOOGLE_API_KEY
        }

        req = urllib.request.Request(
            f'https://maps.googleapis.com/maps/api/distancematrix/json?{urllib.parse.urlencode(params)}',
        )
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')

        return json.loads(body)
