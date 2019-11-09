import urllib.request, urllib.error
import settings

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
            '{}?{}'.format('https://maps.googleapis.com/maps/api/distancematrix/xml',
            urllib.parse.urlencode(params))
        )
        with urllib.request.urlopen(req) as res:
            body = res.read()

        print(body)
