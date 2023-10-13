import json
import os

class ManageCases:
    def __init__(self):
        self = self

    def getCases(self):
        with open('caseCounts.json', 'r') as caseCounts:
            cases = json.load(caseCounts)
        banCase = int(cases['bans'])
        kickCase= int(cases['kicks'])
        banCase+=1
        return cases

    def updateCase(self, banCase, kickCase):
        with open('caseCounts.json', 'w') as updateCases: #dumps new case data
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "lockdowns": 0
            }
            json.dump(cases, updateCases)