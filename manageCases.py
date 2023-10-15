import json
import os

class ManageCases:
    def __init__(self):
        pass

    def getCases(self, caseType, serverID):

        try:  
            with open(f'data/{serverID}_caseCounts.json', 'r') as caseCounts:
                cases = json.load(caseCounts)
        except FileNotFoundError:
            caseCounts = open(f'data/{serverID}_caseCounts.json', 'x')
            caseCounts.write('{"bans": 0, "kicks": 0}')
            cases = json.load(caseCounts)
            caseCounts.close()
        
        banCase = int(cases['bans'])
        kickCase = int(cases['kicks'])
        if caseType == "ban":
            banCase+=1
        elif caseType == "kick":
            kickCase+=1

        return banCase, kickCase,

    def updateCases(self, banCase, kickCase, serverID): 
        with open(f'data/{serverID}_caseCounts.json', 'w') as updateCases: #dumps new case data
            cases = {
                "bans": banCase,
                "kicks": kickCase,
            }
            json.dump(cases, updateCases)


