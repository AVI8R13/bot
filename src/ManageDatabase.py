import sqlite3
import os
from datetime import datetime

class ManageDatabase:
    def __init__(self):
        if not os.path.exists("db"):
            os.mkdir("db/")

    def createDb(self, serverID):

        #set up sqlite database for server case logs
        conn = sqlite3.connect("db/serverCases.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS serverCases (
            serverID STRING,
            bans INT,
            kicks INT,
            warns INT,
            lockdowns INT
        )""")
        conn.commit()
        rows = c.fetchall()
        if not rows: 
            c.execute("INSERT INTO serverCases (serverID, bans, kicks, warns, lockdowns) VALUES (?, ?, ?, ?, ?)",
            (serverID, 0, 0, 0, 0))
            conn.commit()
        conn.close()

        #set up sqlite database for user case logs
        conn = sqlite3.connect(f"db/{serverID}_userCases.db")
        c = conn.cursor()
        c.execute(f"""CREATE TABLE IF NOT EXISTS userCases (
            userID TEXT DEFAULT '',
            responsibleModerator TEXT,
            caseType TEXT,
            reason TEXT,
            date TEXT,
            time TEXT
        )""")
        conn.commit()
        conn.close()

        #set up sqlite database for user warnings
        conn = sqlite3.connect(f"db/{serverID}_userWarnings.db")
        c = conn.cursor()
        c.execute(f"""CREATE TABLE IF NOT EXISTS userWarnings (
            userID TEXT DEFAULT '',
            responsibleModerator TEXT,
            warnNumber INT DEFAULT 0,
            reason TEXT,
            date TEXT,
            time TEXT
        )""")
        conn.commit()
        conn.close()

        #set up sqlite database for global warnings
        conn = sqlite3.connect(f"db/users_globalWarnings.db")
        c = conn.cursor()
        c.execute(f"""CREATE TABLE IF NOT EXISTS globalWarnings (
            userID TEXT DEFAULT '',
            warnNumber INT DEFAULT 0
        )""")
        conn.commit()
        conn.close()

    def getCases(self, serverID, caseType):
        conn = sqlite3.connect("db/serverCases.db")
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        cases = c.execute(f"SELECT * FROM serverCases WHERE serverID = {serverID}").fetchone()
        conn.close()
        return cases[caseType] + 1
    
    def updateCase(self, caseInfo, serverID):

        #Updates count of cases in a server
        conn = sqlite3.connect("db/serverCases.db")
        c = conn.cursor()
        if caseInfo['caseType'] == "bans":
            c.execute("UPDATE serverCases SET bans = bans + 1 WHERE serverID = ?", (serverID,))
        elif caseInfo['caseType'] == "kicks":
            c.execute("UPDATE serverCases SET kicks = kicks + 1 WHERE serverID =  ?", (serverID,))
        elif caseInfo['caseType'] == "warns":
            c.execute("UPDATE serverCases SET warns = warns + 1 WHERE serverID =? ", (serverID,))
        elif caseInfo['caseType'] == "lockdowns":
            c.execute("UPDATE serverCases SET lockdowns = lockdowns + 1 WHERE serverID = ?", (serverID,))
        conn.commit()
        conn.close()

        #Updates server logs
        conn = sqlite3.connect(f"db/{serverID}_userCases.db")
        c = conn.cursor()
        c.execute(f"INSERT INTO userCases (userID, responsibleModerator, caseType, reason, date, time) VALUES (?, ?, ?, ?, ?, ?)",
        (caseInfo['userID'], caseInfo['responsibleModerator'], caseInfo['caseType'], caseInfo['reason'], caseInfo['date'], caseInfo['time']))
        conn.commit()
        conn.close()

        if caseInfo['caseType'] == "warns":
            #Updates user warnings
            conn = sqlite3.connect(f"db/{serverID}_userWarnings.db")
            c = conn.cursor()
            c.execute(f"INSERT INTO userWarnings (userID, responsibleModerator, warnNumber, reason, date, time) VALUES (?, ?, ?, ?, ?, ?)",
            (caseInfo['userID'], caseInfo['responsibleModerator'], caseInfo['caseType'], caseInfo['reason'], caseInfo['date'], caseInfo['time']))
            conn.commit()
            conn.close()

            #Updates global warnings
            conn = sqlite3.connect(f"db/users_globalWarnings.db")
            c = conn.cursor()
            c.execute(f"UPDATE globalWarnings SET warnNumber = warnNumber + 1 WHERE userID = ?", (caseInfo['userID'],))
            conn.commit()
            conn.close()