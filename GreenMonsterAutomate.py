
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify Baseball Reference URL
quote_page = 'https://www.baseball-reference.com/previews/'

# Call BeautifulSoup web parser


page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

# Pull all data related to games
all_games = soup.find('div', class_='game_summaries')
current_games = all_games.findAll('td')

# Declare global variables
stringGameList = []
mlbGameList = []
alGames = []
nlGames = []
finalAL = []
finalNL = []
redSoxGame = []
count = 0;
nlTeams = ['NYM', 'PHI', 'MIA', 'WSN', 'CHC', 'PIT', 'SFG', 'CIN', 'COL', 'ATL', 'MIL', 'STL', 'ARI', 'SDP', 'LAD']
now = datetime.datetime.now()

print("\nScoreboard Set-Up for " + str(now.month) + "/" + str(now.day) + "/" + str(now.year) + "\n")

# Define MLBGame class
class MLBGame:

    def __init__(self, startTime, awayTeam, awayNumb, homeTeam, homeNumb):
        self.awayTeam = awayTeam
        self.homeTeam = homeTeam
        self.awayNumb = awayNumb
        self.homeNumb = homeNumb
        self.startTime = startTime

    def isBostonGame(self):
    	return (self.homeTeam == 'BOS')

    def isNLColumn(self):
        return self.homeTeam in nlTeams

    def gameData(self):
    	parseStartTime = self.startTime.split(':')
    	return (parseStartTime[0] + parseStartTime[1] + "\n" + "#" + self.awayNumb + " " + self.awayTeam + "\n" + "#" + self.homeNumb + " " + self.homeTeam + "\n")

    def gameTime(self):
    	parseStartTime = self.startTime.split(':')
    	return int(parseStartTime[0] + parseStartTime[1])


# Parse thru data to create MLBGame object

i = 0
while i < len(current_games):

    startTime = ""
    teamName = ""
    pitchingNumber = ""

    current_line = str(current_games[i])

    # get startTime
    if 'PM' in current_line:
        start = current_line.find('right">') + 7
        end = current_line.find("PM", start)
        startTime = current_line[start:end]
        if 'MLB Debut' not in startTime:
            stringGameList.append(startTime)
            count += 1
    # get teamName
    if '<strong>' in current_line:
        start = current_line.find('<strong>') + 8
        end = current_line.find("</strong>", start - 5)
        teamName = current_line[start:end]
        if 'MLB Debut' not in teamName:
            stringGameList.append(teamName)
            count += 1
    # get pitchingNumber
    if '(#' in current_line:
        start = current_line.find('br/>(#') + 6
        end = current_line.find("HP", start)
        pitchingParse = current_line[start:end]
        pitchingNumber = pitchingParse[:2]
        if 'MLB Debut' not in teamName:
            stringGameList.append(pitchingNumber)
            count += 1

    # MLB Debut
    if 'MLB Debut' in current_line:
        stringGameList.append('MLB Debut - Check Pitching Number - Team: ')

    i += 1


# Define each game
j = 0
while j < len(stringGameList) - 4:

#Create each MLBGame object and place into appropriate league list
	x = MLBGame(stringGameList[j], stringGameList[j + 1], stringGameList[j + 2], stringGameList[j + 3], stringGameList[j + 4])
	mlbGameList.append(x)
	if x.homeTeam not in nlTeams and len(alGames) < 7:
		alGames.append(x)
	else:
		nlGames.append(x)
	j = j + 5

print("---- Games for American League Side ---- \n")
for game in alGames:
	if(game.homeTeam == 'BOS'):
		redSoxGame.append(game)
		continue
	else:
		print(game.gameData())

print("---- Games for National League Side ----\n")
for game in nlGames:
	print(game.gameData())

print('---- Red Sox Game ----\n')
print(redSoxGame[0].gameData())




















