import re
import urllib2
import sqlite3

week17Home = ['JETS','DOLPHINS','EAGLES','REDSKINS','BENGALS','STEELERS','VIKINGS',
              'LIONS','TITANS','COLTS','FALCONS','BUCCANEERS','BRONCOS','CHARGERS',
              'RAMS','49ERS']
week17Away = ['BILLS','PATRIOTS','COWBOYS','GIANTS','RAVENS','BROWNS','BEARS',
              'PACKERS','TEXANS','JAGUARS','SAINTS','PANTHERS','RAIDERS','CHIEFS',
              'CARDINALS','SEAHAWKS']
week1Home = ['BRONCOS','FALCONS','TITANS','EAGLES','JETS','SAINTS','CHIEFS',
             'RAVENS','TEXANS','JAGUARS','SEAHAWKS','COWBOYS','COLTS','CARDINALS',
             'REDSKINS','49ERS']
week1Away = ['PANTHERS','BUCCANEERS','VIKINGS','BROWNS','BENGALS','RAIDERS',
             'CHARGERS','BILLS','BEARS','PACKERS','DOLPHINS','GIANTS','LIONS',
             'PATRIOTS','STEELERS','RAMS']
i = 0
'''while i < 16:
    url = urllib2.urlopen('http://www.nfl.com/schedules/2016/REG/' + week17Home[i])
    htmltext = url.read()
    regex = '<span class="team-name home ">(.+?)</span>'
    pattern = re.compile(regex)
    results = re.findall(pattern,htmltext)
    # print results
    i+=1
'''
conn = sqlite3.connect('teamSchedules.db')
c = conn.cursor()


def createTablesHome():
    i = 0
    while i < 16:
        c.execute('CREATE TABLE ' + week17Home[i] + '(Teams TEXT, QB REAL, RB REAL, WR REAL)')
    
        i+=1

def createTablesAway():
    i = 0
    while i < 16:
        c.execute('CREATE TABLE ' + week17Away[i] + '(Teams TEXT, QB REAL, RB REAL, WR REAL)')
    
        i+=1      
        





'''regex2 = '<span class="team-name away ">(.+?)</span>'
pattern2 = re.compile(regex2)
results2 = re.findall(pattern2,htmltext)
print results2[:8]

results3 = results + results2
'''
