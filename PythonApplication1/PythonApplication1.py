import requests
import json

print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

while (x <= 10):
    print("Shit is counting: ", x)
    x = x + 1

status = {'X-TBA-Auth-Key':'ir3K1D1jaFLVPteNNBo7Q3CeZocBaEU8kIygdLmBMqHOq7fthFiwffAbi5s25NpO'}
r = requests.get('https://www.thebluealliance.com/api/v3/event/2018mndu/teams/simple', params=status)
print(r)
print(r.text)
stuffs = json.loads(r.text)

teams = []
for stuff in stuffs:
    teams.append(stuff["team_number"])

n = len(teams) - 1 

print(teams[0])

while ( n >= 0 ):
    print(teams[n])
    n = n - 1
