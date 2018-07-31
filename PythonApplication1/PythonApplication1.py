import requests #stuff for https data retreaval
import json #Cuz the datas steralized 
import os #cuz file path stuff
import datetime

TBA = 'https://www.thebluealliance.com/api/v3'
status = {'X-TBA-Auth-Key':'ir3K1D1jaFLVPteNNBo7Q3CeZocBaEU8kIygdLmBMqHOq7fthFiwffAbi5s25NpO'} #seting up auth key

r = requests.get('https://www.thebluealliance.com/api/v3/event/2018mndu/teams/simple', params=status) #requesting info from TBA
print(r)
print(r.text)
stuffs = json.loads(r.text) #takes the json and de steralises it into a list

teams = [] #soon to be list of team numbers
for team in stuffs:                   #sorts through stuffs deviding it up into team     
    teams.append(team["key"]) #adds team number to the end of the list teams

n = len(teams) - 1 #gets total number of teams in index 0

while ( n >= 0 ): #works backwards to 0 listing off all team numbers 
    print(teams[n])
    n = n - 1

if not os.path.exists('data/events/last_updated.json'): #Checks that the file path exists before writing to it
        with open('data/events/' + 'last_updated' + '.json', 'w') as outfile: #creats json file and puts the data in it
            json.dump({'date':'null'}, outfile)
with open('data/events/last_updated.json', 'r') as lastUpdate:
    date = json.load(lastUpdate)
    
if (date["date"] != str(datetime.date.today())): #Checks to see if last updated json was created
    n = len(teams) - 1 #resetting the team list for my while loop iteration
    
    regionals = [] #making a list of regionals attended by the teams in the "teams" list
    print('Gathering Data')
    while ( n >= 0 ): #as long as we have more than one team left in out list counter 
        teamiterate = teams[n] #use that teams index to get the team_key
        print(teamiterate, end='')
        linkR = 'https://www.thebluealliance.com/api/v3/team/'+ str(teamiterate) + '/events/2018'
        tempteamjsontext = requests.get(linkR, params=status) #then assign the json file we retrive for that team to "tempteamjsontext"
        regionaltext = json.loads(tempteamjsontext.text) #change the json file we get to a readable list
        for i in regionaltext: #now we iterate through this list
            regionals.append("2018" + i["event_code"]) #and add every event code to the list "regionals"
            print('---', end='')
        print('')
        n = n - 1 #now change our list counter down one and do this for each subsequent team until it gets to zero
    regionals=list(set(regionals)) #this gets rid of duplicates in the list "regionals"
    #the list "regionals" now has all of the events attended by all of the teams in the regional specified in the original stuffs link


""" Goals
Multy thread program?
Figure pull match numbers then look up in regonal folder?
    https://www.thebluealliance.com/api/v3/team/frc5690/event/2018mndu/matches
take the data and save as a json for sepecific team

Flieing ideas
    Data_Dump
        Teams
            5690
                match data
                team evaluation
            254
                match data
                team evaluation
        Events
            2018mndu
"""

def eventMatchPuller(eventKey): #Function for requesting event matches and then writing them to a file path
    evData = requests.get(TBA + '/event/' + eventKey + '/matches', params=status)
    evDataJson = json.loads(evData.text)
    print(' --- ', end='')
    with open('data/events/' + eventKey + '.json', 'w') as outfile:
        json.dump(evDataJson, outfile)
        print('Dumped')

if (date["date"] != str(datetime.date.today())): #Checks to see if last updated json was created
    print('Writing Data')
    for i in regionals:
        print(i, end='')
        eventMatchPuller(i)
    print('All Data Aquired')

if (date["date"] != str(datetime.date.today())): #Checks to see if last updated json was created
    with open('data/events/' + 'last_updated' + '.json', 'w') as outfile: #creats json file and puts the data in it
        date = str(datetime.date.today())
        dateJson = {
        "date": date
        }
        json.dump(dateJson, outfile) 
        



#take all the match data for a team across regionals and put it into a folder


#find a team to find match data for
#check if a folder is created for that team or create a folder for that team
#find all the matches that particular team participated in
#retrive all of the .json files of the matches that team participated in
#store the .jsons in the folder that was created/checked
#do this for every team in the regional specified under the stuffs variable 
