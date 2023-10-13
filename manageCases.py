import json
import os

class ManageCases:
    def __init__(self):
        pass

    def getCases(self, caseType):
           
        with open('data/caseCounts.json', 'r') as caseCounts:
            cases = json.load(caseCounts)
        banCase = int(cases['bans'])
        kickCase = int(cases['kicks'])
        if caseType == "ban":
            banCase+=1
        elif caseType == "kick":
            kickCase+=1
        
        return banCase, kickCase

    def updateCases(self, banCase, kickCase): 
        with open('data/caseCounts.json', 'w') as updateCases: #dumps new case data
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "lockdowns": 0
            }
            json.dump(cases, updateCases)