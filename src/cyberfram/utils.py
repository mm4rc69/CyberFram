import sqlite3

# SQL statements to create tables
sql_statements = [
    """CREATE TABLE IF NOT EXISTS controls (
            ctrlId INTEGER PRIMARY KEY, 
            ctrlName TEXT NOT NULL,
            ctrDomain TEXT NOT NULL,
            ctrlDescription TEXT NOT NULL, 
            ctrlCreationdate DATE, 
            ctrlHowtomeet TEXT,
            FOREIGN KEY (ctrDomain) REFERENCES domains (domId)     
        );""",
    """CREATE TABLE IF NOT EXISTS domains (
            domId INTEGER PRIMARY KEY, 
            domName TEXT NOT NULL      
        );""",
    """CREATE TABLE IF NOT EXISTS simctrl (
            simctrlId INTEGER PRIMARY KEY, 
            simctrlCtrlid INTEGER NOT NULL,
            FOREIGN KEY (simctrlCtrlid) REFERENCES controls (ctrlId)
        );""",
    """CREATE TABLE IF NOT EXISTS framework (
            frameId INTEGER PRIMARY KEY, 
            frameName TEXT NOT NULL,
            frameCountryOrigine TEXT NOT NULL,
            framePublishedYear INTEGER NOT NULL
        );""",
    """CREATE TABLE IF NOT EXISTS framelevel (
            frmlvlId INTEGER PRIMARY KEY, 
            frmlvlFrameId INTEGER NOT NULL,
            frmlvlDescription TEXT NOT NULL,
            FOREIGN KEY (frmlvlFrameId) REFERENCES framework (frameId)
        );""",
    """CREATE TABLE IF NOT EXISTS frmlvlCtrl (
            frmlvCtrlId INTEGER PRIMARY KEY, 
            frmlvCtrlCtlId INTEGER NOT NULL,
            frmlvCtrlfrmlvlId INTEGER NOT NULL,
            FOREIGN KEY (frmlvCtrlCtlId) REFERENCES controls (Controlld)
        );""",
    """CREATE TABLE IF NOT EXISTS sites (
            siteId INTEGER PRIMARY KEY, 
            siteName TEXT NOT NULL,
            siteCountry TEXT NOT NULL
        );""",
    """CREATE TABLE IF NOT EXISTS siteframeAssign (
            siteframAssId INTEGER PRIMARY KEY, 
            siteframAssSiteId INTEGER NOT NULL,
            siteframAssFrameLvlId INTEGER NOT NULL,
            FOREIGN KEY (siteframAssSiteId) REFERENCES sites (siteId),
            FOREIGN KEY (siteframAssFrameLvlId) REFERENCES framelevel (frmlvlId)
        );""",
    """CREATE TABLE IF NOT EXISTS siteframeassresult (
            siteframresId INTEGER PRIMARY KEY, 
            siteframresAssId INTEGER NOT NULL,
            siteframresCtrlId INTEGER NOT NULL,
            siteframresCtrlSolution TEXT ,
            siteframresCtrlStatus TEXT NOT NULL,
            siteframresCtrlLastUpdate DATE NOT NULL,
            siteframresCtrlEvidence BLOB,
            FOREIGN KEY (siteframresAssId) REFERENCES siteframAssId (siteframAssId),
            FOREIGN KEY (siteframresCtrlId) REFERENCES ntrols (ctrlId)
        );""",
]


# Function to create the database and tables
def createDatabase(dbpath: str):
    try:
        db = dbpath + "/cyberframe.db"
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            # execute statements
            for statement in sql_statements:
                cursor.execute(statement)
            # commit the changes
            conn.commit()
        print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)


def main():
    pass


if __name__ == "__main__":
    main()
