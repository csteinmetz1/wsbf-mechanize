import sys
import json
import spotipy
import datetime
import spotipy.util as util
import urllib.request

class chart_playlist():
    def __init__(self, token):
        if token:
            self.sp = spotipy.Spotify(auth=token)
            self.user_id = self.sp.me()['id']
            self.track_api = 'https://wsbf.net/api/charts/tracks.php'

            # date/time info
            self.stop_dt  = datetime.datetime.now()
            self.start_dt = self.stop_dt - datetime.timedelta(weeks=1)

            # data storage
            self.chart_data = {}
            self.track_ids = []

    def get_top20_tracks(self):
        url = self.track_api + f"?date1={self.start_dt.timestamp()}&date2={self.stop_dt.timestamp()}"

        with urllib.request.urlopen(url) as tracks:
            self.chart_data = json.loads(tracks.read().decode())        

    def find_track_ids(self):    
        for t in self.chart_data:
            q = f"{t['lb_track_name']} {t['lb_artist']}"
            try:
                track_id = self.sp.search(q, limit=1, offset=0, type='track')['tracks']['items'][0]['id']
                self.track_ids.append(track_id)
            except:
                pass

    def build_playlist(self):
        week = self.start_dt.isocalendar()[1]
        playlist_name = f"WSBF Top 20 - Week {week}"
        playlist_id = self.sp.user_playlist_create(self.user_id, playlist_name)['id']
        self.sp.user_playlist_add_tracks(self.user_id, playlist_id, self.track_ids)

if __name__ == '__main__':
    config_file = sys.argv[1]
    config = json.load(open(config_file))
    token = util.prompt_for_user_token(
            config['username'],
            config['scope'], 
            client_id=config['client_id'],
            client_secret=config['client_secret'], 
            redirect_uri=config['redirect_uri'])

    c = chart_playlist(token) 
    c.get_top20_tracks()
    c.find_track_ids()
    c.build_playlist()
