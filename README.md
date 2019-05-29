# GreenMonsterMash

Small personal project -- the goal was to automate the informational retrieval that I do each day at Fenway Park as one of the Green Monster Scoreboard Operators.

Each game, we need to set up the scoreboard with the appropriate AL and NL games, and their respective pitching numbers. This Python script allows me to get all of the necessary information needed with the click of a button.

In order to get the information, it uses a Web Scraper library called BeautifulSoup. Using BeautifulSoup, I am able to get the HTML from BaseballReference's Probable Pitchers webpage. I then parse that HTML into a readable output so I can easily see the needed information to set up the scoreboard.

Please be aware that this script should be run using a version of Python 3.7, as well as with certain dependencies installed locally.

Go Sox!

-------------------------

Here is a sample output of the program from September 28th, 2018:

```
Scoreboard Set-Up for 9/28/2018

7:10
#61 BOS
#34 NYY

---- Games for American League Side ---- 

2:10
#40 CHW
#17 MIN

7:05
#45 HOU
#41 BAL

7:10
#45 TOR
#20 TBR

8:10
#27 CHW
#61 MIN

8:15
#52 CLE
#31 KCR

10:07
#50 OAK
#51 LAA

---- Games for National League Side ----

2:20
#50 STL
#28 CHC

6:40
#49 PIT
#28 CIN

7:05
#26 ATL
#48 PHI

7:10
#62 MIA
#55 NYM

8:10
#27 DET
#27 MIL

8:10
#41 WSN
#21 COL

10:10
#46 ARI
#46 SDP

10:10
#33 TEX
#49 SEA

10:15
#99 LAD
#40 SFG
```
