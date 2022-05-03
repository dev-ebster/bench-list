from importlib.util import spec_from_file_location
from logging import RootLogger
from fastapi import FastAPI
from pydantic import BaseModel
import json
import datetime
from fastapi.middleware.cors import CORSMiddleware

class Player(BaseModel):
    name: str
    klasse: str
    spec: str
    role: str
    rank: str

app = FastAPI()
# ------------ CORS --------------- # 
#origins = ['http://127.0.0.1:8080']
origins = ['http://127.0.0.1:5500']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ VIEW BENCH LIST --------------- # 
@app.get("/bench-list")
async def read_bench_list():
    with open('roster.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['bench-list'])

# ------------ VIEW PLAYER LIST --------------- #
@app.get("/players")
async def read_player_list():
    with open('roster.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'])

# ------------ VIEW SPECIFIC PLAYER --------------- #
@app.get("/players/{player_name}")
async def read_player_list(player_name):
    with open('roster.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'][player_name])

# ------------ BENCH PLAYERS --------------- #

@app.post("/bench/{player_name}")
async def bench_player(player_name):

    # -- open JSON file -- #
    with open('roster.json', 'r') as json_file:
        data = json.load(json_file)
    # -- Variables -- #
    bench_list = data['bench-list']

    # -- benches player -- # 
    if not player_name in bench_list: # checks if name is on bench_list - if not gives error
        return('Error ' +player_name + " isn't on the bench list")
    else: # benches player
         bench_list.remove(player_name)
         bench_list.append(player_name)
         #date = datetime.datetime.now()
         #date_formatted = date.strftime("%b %d %H:%M:%S %Y")
         #data['players'][player_name]['bench-history'].append(date_formatted) 

    # -- writes the updated bench list to JSON -- #
    with open('roster.json','w') as outfile:
        json.dump(data, outfile)
    return(bench_list)




    # TEST GROUND

@app.post("/add-player/{player_name}")
async def add_player(player_name: str, player: Player):
    return(player)
        