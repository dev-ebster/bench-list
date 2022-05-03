from fastapi import FastAPI
import json

app = FastAPI()


# -- View bench list --  
@app.get("/bench-list")
async def read_bench_list():
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['bench_list'])

# -- View players list -- 
@app.get("/players")
async def read_player_list():
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'])


# -- View player name -- 
@app.get("/players/{player_name}")
async def read_player_name(player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)

    return(data['players'][player_name])


@app.get("bench/{player_name}")
async def bench_player(player_name):
    with open('bench.json', 'r') as json_file:
        data = json.load(json_file)
    bench_list = data['bench_list']
    if player_name in bench_list:
            bench_list.remove(player_name)
            bench_list.append(player_name)
            with open('bench.json','w') as outfile:
                json.dump(data, outfile)
    return(data)