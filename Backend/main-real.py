from fastapi import FastAPI
import json
import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# ------------ CORS --------------- # 
origins = ['http://127.0.0.1:8080']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------ VIEW BENCH LIST --------------- # 
@app.get("/bench_list")
async def read_bench_list():
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['bench_list'])

# ------------ VIEW PLAYER LIST --------------- #
@app.get("/players")
async def read_player_list():
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'])


# ------------ VIEW  SPECIFIED PLAYERs BENCH HISTORY --------------- #
@app.get("/bench_history/{player_name}")
async def read_player_name(player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'][player_name])

 # ------------ VIEW  SPECIFIED PLAYERs BENCH COUNT --------------- #
@app.get("/bench_count/{player_name}")
async def read_player_name(player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(len(data['players'][player_name]['bench_history']))   

# ------------ BENCH PLAYERS --------------- #

@app.post("/bench/{player_name}")
async def bench_player(player_name):

    # -- open JSON file -- #
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)
    # -- Variables -- #
    bench_list = data['bench_list']

    # -- benches player -- # 
    if not player_name in bench_list: # checks if name is on bench_list - if not gives error
        return('Error ' +player_name + " isn't on the bench list")
    else: # benches player
         bench_list.remove(player_name)
         bench_list.append(player_name)
         date = datetime.datetime.now()
         date_formatted = date.strftime("%b %d %H:%M:%S %Y")
         data['players'][player_name]['bench_history'].append(date_formatted) 

    # -- writes the updated bench list to JSON -- #
    with open('bench.json','w') as outfile:
        json.dump(data, outfile)
    return(bench_list)

# ------------ ADD PLAYER --------------- #

@app.post("/add/{new_player_name}")
async def add_new_player(new_player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)
    
    players = data['players']
    bench_list = data['bench_list']

    if not new_player_name in bench_list:
        bench_list.insert(0,new_player_name)
        players[new_player_name] = { 'bench_history' : [] }
    else:
        return('error ' +new_player_name + " is already on the roster")
    with open('bench.json','w') as outfile:
        json.dump(data, outfile)
    return(data)

# ------------ DELETE PLAYER --------------- #

@app.post("/delete/{old_player_name}")
async def del_old_player(old_player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)
    
    players = data['players']
    bench_list = data['bench_list']

    if  old_player_name in bench_list:
        bench_list.remove(old_player_name)
        del(players[old_player_name])
    else:
        return('error ' +old_player_name + " isn't on the roster")

    with open('bench.json','w') as outfile:
        json.dump(data, outfile)
    return(data)





    

