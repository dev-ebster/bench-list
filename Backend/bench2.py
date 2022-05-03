from datetime import datetime
import json
import sys
import datetime

#open json file as read
with open('bench.json', 'r') as json_file:
    data = json.load(json_file)

#variables
if len(sys.argv) >= 2:
    player_name = sys.argv[2]
    command = sys.argv[1]

bench_list = data['bench_list']
players = data['players']
date = datetime.datetime.now()
date_formatted = date.strftime("%d %B %Y")
add_player_txt = "bench_history: []"


# command bench prints the bench list
if len(sys.argv) < 2:
    print(bench_list)
else: 
    if len(sys.argv) == 3 and command == 'bench': #check if command is the following bench x-player
        if player_name in bench_list:
            bench_list.remove(player_name)
            bench_list.append(player_name) #benches named playerS
            data['players'][player_name]['bench_history'].append(date_formatted) 
            print(bench_list)
            print(data['players'][player_name]['bench_history'])
        else:
            print('error ' + player_name + " is not a valid player name") #if the name isn't on the list, it gives an error
        
    if len(sys.argv) == 3 and command == 'add': #command to add new player to the list (front of list)
        bench_list.insert(0, player_name)
        players[player_name] = { 'bench_history' : [] }
        print(player_name + " added to the list")
        print(bench_list)

    if len(sys.argv) == 3 and command == 'remove': #command to remove player from the list
        bench_list.remove(player_name)
        del(players[player_name])
        print(bench_list)
        print(players)

    if len(sys.argv) == 3 and command == "bench_history":
        print(data['players'][player_name]['bench_history'])

    if len(sys.argv) == 3 and command == "bench_count":
        print(len(data['players'][player_name]['bench_history']))

with open('bench.json','w') as outfile:
    json.dump(data, outfile)
    