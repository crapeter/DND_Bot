# DND_Bot
DND_bot that provides most of the functionality needed to play dnd online, if needed

Ensure you have at python installed and run the following pip commands:

pip install -r requirements.txt

I use a couple match statements to make sure you have python 3.10 or newer installed or you could just convert the match statement to an if/else chain

This uses MongoDB to store your characters info so make sure to create a mongodb account, otherwise this won't work. You also need to create a discord bot for this and copy the bot token into the last line of code in the file. When you first create a character, make sure to switch to said character that way the player_data.json file gets created
