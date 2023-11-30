import json

with open("tokens.json", "r") as tokens:
    tokenList = json.load(tokens)

discordToken = tokenList['BOT_TOKEN']
giphyApiKey = tokenList['GIPHY_API_KEY']
