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
            with open(f'data/{serverID}_caseCounts.json', 'w') as caseCounts:
                template = {"bans": 0, "kicks": 0, "warns": 0}            
                json.dump(template, caseCounts)
            with open(f'data/{serverID}_caseCounts.json') as caseCounts:
                cases = json.load(caseCounts)

        banCase = int(cases['bans'])
        kickCase = int(cases['kicks'])
        warnCase = int(cases['warns'])
        if caseType == "ban":
            banCase+=1
        elif caseType == "kick":
            kickCase+=1
        elif caseType == "warn":
            warnCase+=1

        return banCase, kickCase, warnCase

    def updateCases(self, banCase, kickCase, warnCase, serverID): 
        with open(f'data/{serverID}_caseCounts.json', 'w') as updateCases: 
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "warns": warnCase, 
            }
            json.dump(cases, updateCases)

    def logCases(self, serverID, member, caseType, reason, banCase, kickCase, warnCase):
        if caseType == "ban":
            case = f"ban{banCase}"
        elif caseType == "kick":
            case = f"kick{kickCase}"
        elif caseType == "warn":
            case = f"warn{warnCase}"
        caseData = {
            "Case": case,
            "Member": str(member),
            "Reason": reason
        }
        try:
            with open(f'data/{serverID}_Cases.json', 'r') as logCases:
                cases = json.load(logCases)
        except (FileNotFoundError, json.JSONDecodeError):
            cases = []
        cases.append(caseData)
        with open(f'data/{serverID}_Cases.json', 'w') as logCases:
            json.dump(cases, logCases, indent=4)

    def logUserWarns(self, userID, member, reason, warnCase):
        data = {
            "Warning": warnCase,
            "Reason": reason
        }
        try:
            with open(f'data/{userID}_Warnings.json', 'r') as warnings:
                userWarnings = json.load(warnings)
        except (FileNotFoundError):
            userWarnings = []
        userWarnings.append(data)
        with open(f'data/{userID}_Warnings.json', 'w'):
            json.dump(userWarnings, warnings)