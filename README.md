# wsbf-mechanize
Python scripts to automate various things at WSBF

## Overview
These scripts are intended to run a linux machine in the engineering office (jean at the moment). The scripts will be setup using cron jobs so that they occur at set intervals. Make sure to setup the `config.json` file correctly or the scripts may not operate correctly. This repo contains the following scripts:

* `backup_auto_rotation.py` - copy new rotation music onto the backup automation PC at the TX
* `eas_backup.py` - save daily copies of the EAS log files (in XML format)
* `chart_playlist.py` - update a Spotify playlist of the WSBF Top 20 songs played weekly

## Setup

clone this repository 

```
git clone https://github.com/csteinmetz1/wsbf-mechanize
```

install requirements

```
pip install -r requirements.txt
```

create `config.json` file in root directory
(ask compe for pre-made file)

```json
{
    "spotify" : {
        "scope" : "playlist-modify-public user-top-read",
        "username" : "USERNAME",
        "client_id" : "CLIENT_ID",
        "client_secret" : "CLIENT_SECRET",
        "redirect_uri" : "http://localhost:8888/callback"
    },
    "eas" : {
        "log" : "http://eas.wsbf.net/cgi-bin/logcgi.cgi",
        "username" : "USERNAME", 
        "password" : "PASWORD",
        "output" : "store/eas"
    }
}
```

Configure cron jobs