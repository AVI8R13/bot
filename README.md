# Introduction

I made this bot to develop and demonstrate my programming skills. It is by no means perfect, and there is definately room for improvement.

## Getting Started

To use this bot, you'll need to create a bot application on the Discord Developer Portal and obtain a bot token. Here's how to set it up:

1. Create a Discord Bot Application:

   - Go to the [Discord Developer Portal](https://discord.com/developers/applications) and log in or create an account if you don't have one already.
   - Click on "New Application" to create a new application. Make sure to give it an appropriate name.
   - Go to the "Bot" tab on the left sidebar and click "Add Bot" to create a bot user.
   - Go to the "OAuth2" tab on the left sidebar and click "URL Generator".

2. Invite the bot to a server

   - Select "Bot" as a scope and select the required permissions. It must have the "Send Messages" permission as a minimum.
   - For moderation commands to work, you must select "Kick Members" and "Ban Members" permissions. I will hopefully add more in the future.
   - Copy the URl under the scopes menue, paste it into a browser and select the server you want the bot to join.

3. Obtain the Bot Token:

   - Under the "Token" section in the bot settings, click "Reset Token". You may have to enter your password or 2FA code to do this.
   - Once your token has been revealed, click "Copy Token" to copy it to your clipboard.

4. Replace the Token Variable:

   - In your project code, find the variable `BOT_TOKEN` and replace it with your bot's token.
   - Alternatively, you can create a `.env` file in your project directory with the following content:
     `BOT_TOKEN="your_token"`, which is much more secure than storing it in the `client.py` file.

5. Run the bot:
   - Create a `data` folder in your project directory.
   - Run the `client.py` file in your ide/text editor of choice
   - If you've set up the bot correctly, you should see 'Client is running!' in your terminal and the bot will be online.

## Prerequisites

Before running the bot, make sure you have the necessary libraries installed. You can install them using pip:

```bash
pip install discord.py
```
