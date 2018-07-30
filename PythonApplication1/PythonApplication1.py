import requests #stuff for https data retreaval
import json #Cuz the datas steralized 

print("This line will hopefully be printed.") #cuz idk what im doing

x = 1 #i copyed and pasted this bit 
if x == 1:
    # indented four spaces
    print("x is 1.")

while (x <= 10):
    print("Shit is counting: ", x)
    x = x + 1

status = {'X-TBA-Auth-Key':'ir3K1D1jaFLVPteNNBo7Q3CeZocBaEU8kIygdLmBMqHOq7fthFiwffAbi5s25NpO'} #seting up auth key
r = requests.get('https://www.thebluealliance.com/api/v3/event/2018mndu/teams/simple', params=status) #requesting info from TBA
print(r)
print(r.text)
stuffs = json.loads(r.text) #takes the json and de steralises it into a list

teams = [] #soon to be list of team numbers
for team in stuffs:                   #sorts through stuffs deviding it up into team     
    teams.append(team["team_number"]) #adds team number to the end of the list teams

n = len(teams) - 1 #gets totel number of team 

print(teams[0]) #Prints team 0 in list

while ( n >= 0 ): #works backwards to 0 listing off all team numbers 
    print(teams[n])
    n = n - 1


""" Goals
Take match data and dump to regonal folder
    https://www.thebluealliance.com/api/v3/event/2018mndu/matches
Figure pull match numbers then look up in regonal folder?
    https://www.thebluealliance.com/api/v3/team/frc5690/event/2018mndu/matches
take the data and save as a json for sepecific team

Flieing ideas
    Data_Dump
        Teams
            5690
            254
        Events
            2018mndu
"""