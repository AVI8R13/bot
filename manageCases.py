import json
import os
from datetime import datetime

class ManageCases:
    def __init__(self):
        if os.path.exists("data/") == False:
            os.mkdir("data")

    def getCases(self, caseType, serverID):

        try:  
            with open(f'data/{serverID}_caseCounts.json', 'r') as caseCounts:
                cases = json.load(caseCounts)
        except FileNotFoundError:
            with open(f'data/{serverID}_caseCounts.json', 'w') as caseCounts:
                template = {"bans": 0, "kicks": 0, "warns": 0, "lockdowns": 0}         
                json.dump(template, caseCounts)
            with open(f'data/{serverID}_caseCounts.json') as caseCounts:
                cases = json.load(caseCounts)

        banCase = int(cases['bans'])
        kickCase = int(cases['kicks'])
        warnCase = int(cases['warns'])
        lockdownCase = int(cases['lockdowns'])

        if caseType == "ban":
            banCase+=1
        elif caseType == "kick":
            kickCase+=1
        elif caseType == "warn":
            warnCase+=1
        elif caseType == "lockdown":
            lockdownCase+1
 
        return banCase, kickCase, warnCase, lockdownCase

    def updateCases(self, banCase, kickCase, warnCase, lockdownCase, serverID): 
        with open(f'data/{serverID}_caseCounts.json', 'w') as updateCases: 
            cases = {
                "bans": banCase,
                "kicks": kickCase,
                "warns": warnCase,
                "lockdowns": lockdownCase

            }
            json.dump(cases, updateCases)

    def logCases(self, serverID, member, caseType, reason, banCase, kickCase, warnCase, lockdownCase):
        time = datetime.now()
        if caseType == "ban":
            case = f"ban{banCase}"
        elif caseType == "kick":
            case = f"kick{kickCase}"
        elif caseType == "warn":
            case = f"warn{warnCase}"
        elif caseType == "lockdown":
            case = f"lockdown{lockdownCase}"
        caseData = {
            "Case": case,
            "Member": str(member),
            "Reason": reason,
            "Date": time.strftime("%m/%d/%Y"),
            "Time": time.strftime("%H:%M:%S")
        }
        try:
            with open(f'data/{serverID}_Cases.json', 'r') as logCases:
                cases = json.load(logCases)
        except (FileNotFoundError, json.JSONDecodeError):
            cases = []
        cases.append(caseData)
        with open(f'data/{serverID}_Cases.json', 'w') as logCases:
            json.dump(cases, logCases, indent=4)


