# DND_Bot
DND_bot that provides most of the functionality needed to play dnd online, if needed

Ensure you have at python installed and run the following pip commands:

pip install -r requirements.txt

I use a couple match statements to make sure you have python 3.10 or newer installed or you could just convert the match statement to an if/else chain. This is so that if you have more than 4 PC's, you can easily expand the players be able to easily switch between characters. If you want the "Your god has awaken" message to be sent to your discord channel, all you have to do is copy the discord channel id and paste it into the on_ready() function.

This uses MongoDB to store your characters info so make sure to create a mongodb account, otherwise this won't work. Then you should click the connect button you see next to whatever you named your cluster, then you click the top option "drivers" and copy the text given in step three into the part of the code that says "Insert you mongoDB connection here". Afterwards you should put in your password to the connection and you are now connected to your database, which after you run the bot will automatically create a DND\Characters collection.

You also need to create a discord bot for this and copy the bot token into the last line of code in the file. When you first create a character, make sure to switch to said character that way the player_data.json file gets created. In order to switch between characters, you need to paste your discord id into the match or if/else statements as otherwise you won't be able to switch to the new character you just created.
