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
    teams.append(team["key"]) #adds team number to the end of the list teams

n = len(teams) - 1 #gets total number of teams in index 0

print(teams[0]) #Prints team 0 in list

while ( n >= 0 ): #works backwards to 0 listing off all team numbers 
    print(teams[n])
    n = n - 1

n = len(teams) - 1 #resetting the team list for my while loop iteration

regionals = [] #making a list of regionals attended by the teams in the "teams" list
while ( n >= 0 ): #as long as we have more than one team left in out list counter 
    teamiterate = teams[n] #use that teams index to get the team_key  
    linkR = 'https://www.thebluealliance.com/api/v3/team/'+ str(teamiterate) + '/events/2018'
    tempteamjsontext = requests.get(linkR, params=status) #then assign the json file we retrive for that team to "tempteamjsontext"
    regionaltext = json.loads(tempteamjsontext.text) #change the json file we get to a readable list
    for i in regionaltext: #now we iterate through this list
        regionals.append("2018" + i["event_code"]) #and add every event code to the list "regionals"
    n = n - 1 #now change our list counter down one and do this for each subsequent team until it gets to zero
regionals=list(set(regionals)) #this gets rid of duplicates in the list "regionals"
#the list "regionals" now has all of the events attended by all of the teams in the regional specified in the original stuffs link
""" Goals
Multy thread program?
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

#jeef is dip