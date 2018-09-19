# GreenMonsterMash

****Needed to make edits for edge cases, so libraries and scraping may not be successful

Small personal project -- the goal was to automate the informational retrieval that I do each day at Fenway Park as one of the Green Monster Scoreboard Operators.

Each game, we need to set up the scoreboard with the appropriate AL and NL games, and their respective pitching numbers. This Python script allows me to get all of the necessary information needed with the click of a button.

In order to get the information, it uses a Web Scraper library called BeautifulSoup. Using BeautifulSoup, I am able to get the HTML from BaseballReference's Probable Pitchers webpage. I then parse that HTML into a readable output so I can easily see the needed information to set up the scoreboard.

Go Sox!
