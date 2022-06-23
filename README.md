# happy-city
What's more fun than shouting vague instructions to your friends to prevent seismic disaster? Doing so in the public sector, of course! This is a fast take on a game we all love, Spaceteam.

Forked from [OpenSpaceTeam](https://github.com/openspaceteam).

## Installation
### Requirements
- Python 3.6 (doesn't work in <= 3.5 nor 2. Check with `python --version`. May have to use `python3`.)
- PIP (check with `pip --version`)
- VirtualEnv (for Mac setup see [here](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html))
- node.js
- npm

### First Steps
```bash
$ git clone https://github.com/nat-foo/happy-city.git
$ cd happy-city
```

### Backend
```bash
$ cd api
$ virtualenv -p $(which python3.6) .venv
$ source .venv/bin/activate
(.venv)$ pip install -r requirements.txt
(.venv)$ python3 happycity.py

 _   _                           _____ _ _         
| | | |                         /  __ (_) |        
| |_| | __ _ _ __  _ __  _   _  | /  \/_| |_ _   _ 
|  _  |/ _` | '_ \| '_ \| | | | | |   | | __| | | |
| | | | (_| | |_) | |_) | |_| | | \__/\ | |_| |_| |
\_| |_/\__,_| .__/| .__/ \__, |  \____/_|\__|\__, |
            | |   | |     __/ |               __/ |
            |_|   |_|    |___/               |___/ 


INFO:root:Using SSL
======== Running on http://0.0.0.0:4433 ========
(Press CTRL+C to quit)
```

### Frontend
```bash
$ cd ../game
$ npm i
$ npm start

Run localhost on 0.0.0.0:8080.
```

## License
This project is licensed under the GNU AGPL 3 License. See the "LICENSE" file for more information.

