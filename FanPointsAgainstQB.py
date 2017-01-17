import re
import urllib2
import sqlite3

url = urllib2.urlopen('http://fantasy.nfl.com/research/pointsagainst?position=1&statCategory=pointsAgainst&statSeason=2016&statType=seasonPointsAgainst&statWeek=8')
htmltext = url.read()
regex3 = '<div class="c c-[a-z][a-z]?[a-z]"><b></b>(.+?) Defense<br/><em>vs QB</em></div></td><td class="playerOpponent"><span class="nflTeamStat pointsAgainstStatId-opponent nflTeamId-[0-9]?[0-9]">@?[A-Za-z]{1,3}</span></td><td class="stat numeric sorted"><span class="nflTeamStat pointsAgainstStatId-pts nflTeamId-[0-9]?[0-9]">([1-2]?[0-9].[0-9][0-9])</span></td><td class="stat numeric">'
pattern3 = re.compile(regex3)
results3 = re.findall(pattern3,htmltext)
results3.sort()
print results3

conn = sqlite3.connect('teamPointsAgainst2016.db')
c = conn.cursor()

def tableCreate():
    c.execute("CREATE TABLE QBpoints (Team TEXT, QB REAL)")
    conn.commit()

def writeQB():
    i = 0
    while i<32:
        
        c.execute("INSERT INTO QBpoints (Team, QB) VALUES (?,?)", (results3[i]))
        i+=1

    conn.commit()


