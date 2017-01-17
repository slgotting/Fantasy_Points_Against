import re
import urllib2
import operator
import sqlite3

conn = sqlite3.connect('teamPointsAgainst2016.db')
c = conn.cursor()

week17Home = ['JETS','DOLPHINS','EAGLES','REDSKINS','BENGALS','STEELERS','VIKINGS',
              'LIONS','TITANS','COLTS','FALCONS','BUCCANEERS','BRONCOS','CHARGERS',
              'RAMS']
week17Away = ['BILLS','PATRIOTS','COWBOYS','GIANTS','RAVENS','BROWNS','BEARS',
              'PACKERS','TEXANS','JAGUARS','SAINTS','PANTHERS','RAIDERS','CHIEFS',
              'CARDINALS','SEAHAWKS']
week1Home = ['BRONCOS','FALCONS','TITANS','EAGLES','JETS','SAINTS','CHIEFS',
             'RAVENS','TEXANS','JAGUARS','SEAHAWKS','COWBOYS','COLTS','CARDINALS',
             'REDSKINS','49ERS']
week1Away = ['PANTHERS','BUCCANEERS','VIKINGS','BROWNS','BENGALS','RAIDERS',
             'CHARGERS','BILLS','BEARS','PACKERS','DOLPHINS','GIANTS','LIONS',
             'PATRIOTS','STEELERS','RAMS']


def wfd():      #write full data of teams for season, given tables are already created
    i = 0
    j = 1
    while i < 31:

        
        url = urllib2.urlopen('http://www.nfl.com/schedules/2016/REG/' + teams[i])
        htmltext = url.read()
        regex = '<span class="team-name [ah][ow][am][ey] ">(.+?)</span>'
        pattern = re.compile(regex)
        results = re.findall(pattern,htmltext)
        print results
        if len(results) == 9:
            while j<8:
                for row in c.execute('SELECT QB, RB, WR FROM fullTeamPointsAgainst WHERE Team =?', ([str(results[j]).upper()])):
                    QBrow = str(row[:1]).replace('(','').replace(',','').replace(')','')
                    print QBrow
                    RBrow = str(row[1:2]).replace('(','').replace(',','').replace(')','')
                    print RBrow
                    WRrow = str(row[2:3]).replace('(','').replace(',','').replace(')','')
                    print WRrow
                    c.execute('INSERT INTO ' + teams[i] + ' VALUES (?,?,?,?,?)',
                              (j + 9
                               , results[j], QBrow, RBrow, WRrow))
                j+=1
        if len(results) == 10:
            while j<9:
                for row in c.execute('SELECT QB, RB, WR FROM fullTeamPointsAgainst WHERE Team =?', ([str(results[j]).upper()])):
                    QBrow = str(row[:1]).replace('(','').replace(',','').replace(')','')
                    print QBrow
                    RBrow = str(row[1:2]).replace('(','').replace(',','').replace(')','')
                    print RBrow
                    WRrow = str(row[2:3]).replace('(','').replace(',','').replace(')','')
                    print WRrow
                    c.execute('INSERT INTO ' + teams[i] + ' VALUES (?,?,?,?,?)',
                              (j + 8
                               , results[j], QBrow, RBrow, WRrow))
                j+=1
        elif len(results) == 11:
            while j<10:
                for row in c.execute('SELECT QB, RB, WR FROM fullTeamPointsAgainst WHERE Team =?', ([str(results[j]).upper()])):
                    QBrow = str(row[:1]).replace('(','').replace(',','').replace(')','')
                    print QBrow
                    RBrow = str(row[1:2]).replace('(','').replace(',','').replace(')','')
                    print RBrow
                    WRrow = str(row[2:3]).replace('(','').replace(',','').replace(')','')
                    print WRrow
                    c.execute('INSERT INTO ' + teams[i] + ' VALUES (?,?,?,?,?)',
                              (j + 7
                               , results[j], QBrow, RBrow, WRrow))
                j+=1
                
        j=1
        i+=1
        conn.commit()



def rtd():   #read team difficulty of schedule
    i = 0
    
    while i <31:
        QB = []
        RB = []
        WR = []
        print teams[i]
        for row in c.execute('SELECT QB FROM ' + teams[i] + ' WHERE ID >7'):
            QBrow = str(row).replace('(','').replace(',','').replace(')','')
            QB.append(QBrow)
        for row in c.execute('SELECT RB FROM ' + teams[i] + ' WHERE ID >7'):
            RBrow = str(row).replace('(','').replace(',','').replace(')','')
            RB.append(RBrow)     
        for row in c.execute('SELECT WR FROM ' + teams[i] + ' WHERE ID >7'):
            WRrow = str(row).replace('(','').replace(',','').replace(')','')
            WR.append(WRrow)
                            
            
        QBsum = sum(float(i) for i in QB)
        RBsum = sum(float(j) for j in RB)
        WRsum = sum(float(i) for i in WR)
        
        c.execute('INSERT INTO playoffs VALUES (?,?,?,?)',
                  (teams[i], QBsum, RBsum, WRsum))
        
        
        print QBsum
        print RBsum
        print WRsum
        i+=1
        conn.commit()
    

def deleteTeams(): #deletes all team tables
    j = 0
    i=0
    while True:
        try:
            
            while i<32:
                c.execute('drop table ' + teams[i])
                i+=1
        except:
            i+=1
        

def wfpa(): #writes each teams fullPointsAgainst
    i = 0
    while i < 32:
        for row in c.execute('SELECT QB FROM QBpoints WHERE Team="%s"' % (teamCities[i])):
            QBrow = str(row).replace('(','').replace(',','').replace(')','')
            
        for row in c.execute('SELECT RB FROM RBpoints WHERE Team="%s"' % (teamCities[i])):
            RBrow = str(row).replace('(','').replace(',','').replace(')','')
            
        for row in c.execute('SELECT WR FROM WRpoints WHERE Team="%s"' % (teamCities[i])):
            WRrow = str(row).replace('(','').replace(',','').replace(')','')
            
        print teamCities[i] + ' QB ' + QBrow + ',' + ' RB ' + RBrow + ',' + ' WR ' + WRrow
        
        c.execute('INSERT INTO fullTeamPointsAgainst VALUES (?,?,?,?)',
                  (teams[i], QBrow, RBrow, WRrow))
        i+=1
    conn.commit()
        
            
         
        
    


    
    

    
    

    
              
              
    

'''
j = 0
while j < 15:
    url2 = urllib2.urlopen('http://www.nfl.com/schedules/2016/REG/' + week17Away[j])
    htmltext2 = url2.read()
    regex2 = '<span class="team-name home ">(.+?)</span>'
    pattern2 = re.compile(regex2)
    results2 = re.findall(pattern2,htmltext2)
    print results2
    j+=1



#gathers data
url = urllib2.urlopen('http://fantasy.nfl.com/research/pointsagainst?position=1&statCategory=pointsAgainst&statSeason=2016&statType=seasonPointsAgainst&statWeek=8')
url2 = urllib2.urlopen('http://fantasy.nfl.com/research/pointsagainst?position=2&statCategory=pointsAgainst&statSeason=2016&statType=seasonPointsAgainst&statWeek=8')
url3 = urllib2.urlopen('http://fantasy.nfl.com/research/pointsagainst?position=3&statCategory=pointsAgainst&statSeason=2015&statType=seasonPointsAgainst&statWeek=1')
htmltext = url.read()
htmltext2 = url2.read()
htmltext3 = url3.read()
regex = '<div class="c c-no"><b></b>(.+?) Defense<br/><em>vs QB</em></div></td><td class="stat numeric sorted"><span class="nflTeamStat pointsAgainstStatId-pts nflTeamId-[0-9]?[0-9]">?@[A-Z]{1,3}</span></td<td class="stat numeric sorted"><span class = "nflTeamStat pointsAgainstStatID-pts nflTeamId-[0-9]?[0-9]">(.+?)</span>'
regex2 = '<div class="c c-[a-z][a-z]?[a-z]"><b></b>(.+?) Defense<br/><em>vs RB</em></div></td><td class="playerOpponent"><span class="nflTeamStat pointsAgainstStatId-opponent nflTeamId-[0-9]?[0-9]">@?[A-Za-z]{1,3}</span></td><td class="stat numeric sorted"><span class="nflTeamStat pointsAgainstStatId-pts nflTeamId-[0-9]?[0-9]">([1-2][0-9].[0-9][0-9])</span></td><td class="stat numeric">'
regex3 = 'class="c c-[a-z][a-z]?[a-z]"><b></b>(.+?) Defense<br/><em>vs WR</em></div></td><td class="stat numeric sorted"><span class="nflTeamStat pointsAgainstStatId-pts nflTeamId-[0-9]?[0-9]">(.+?)</span>'
pattern = re.compile(regex)
pattern2 = re.compile(regex2)
pattern3 = re.compile(regex3)
results = re.findall(pattern,htmltext)
results2 = re.findall(pattern2,htmltext2)
results3 = re.findall(pattern3,htmltext3)
results.sort()
results2.sort()
results3.sort()
results2 = results2
results3 = results3
#print htmltext2
print results2
'''




teamCities = ['Arizona Cardinals','Atlanta Falcons','Baltimore Ravens','Buffalo Bills','Carolina Panthers','Chicago Bears','Cincinnati Bengals',
              'Cleveland Browns','Dallas Cowboys','Denver Broncos','Detroit Lions','Green Bay Packers','Houston Texans','Indianapolis Colts',
              'Jacksonville Jaguars','Kansas City Chiefs','Los Angeles Rams','Miami Dolphins','Minnesota Vikings','New England Patriots',
              'New Orleans Saints','New York Giants','New York Jets','Oakland Raiders','Philadelphia Eagles','Pittsburgh Steelers','San Diego Chargers',
              'San Francisco 49ers','Seattle Seahawks','Tampa Bay Buccaneers','Tennessee Titans','Washington Redskins']

teams = ['CARDINALS','FALCONS','RAVENS','BILLS','PANTHERS','BEARS',
         'BENGALS','BROWNS','COWBOYS','BRONCOS','LIONS','PACKERS',
         'TEXANS','COLTS','JAGUARS','CHIEFS','RAMS','DOLPHINS',
         'VIKINGS','PATRIOTS','SAINTS','GIANTS','JETS','RAIDERS',
         'EAGLES','STEELERS','CHARGERS','SEAHAWKS',
         'BUCCANEERS','TITANS','REDSKINS']









# create tables for each team except 49ers
def cut():      #create unique table
    i = 0

    while i < 1:
        c.execute('CREATE TABLE playoffs (Team TEXT, QB REAL, RB REAL, WR REAL)')
    

        i+=1

def createTables():
    i = 0
    while True:
        try:
            while i < 32:
                c.execute('CREATE TABLE ' + teams[i] + '(ID INT, Team TEXT, QB REAL, RB REAL, WR REAL)')
            
                i+=1
        except:
            i+=1
    
import pygame

def r():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/Steven/Downloads/It's a Trap!.mp3")
    pygame.mixer.music.play()

def t():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/Users/Steven/Downloads/Admiral Ackbar - It's A Trap!.mp3")
    pygame.mixer.music.play()
