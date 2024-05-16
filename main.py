import discord
from discord.ext import commands
import pymongo
import random
import re
import json


bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

client = pymongo.MongoClient(
    "Insert you mongoDB connection here"
)
db = client.DND
character_collections = db.Characters


@bot.event
async def on_ready():
    if bot.user:
        print(f'Logged in as {bot.user.name}')
        # roll_or_die = bot.get_channel(*discord channel ID goes here*)
        # if roll_or_die:
            # await roll_or_die.send("Your God has awakened")


@bot.command()
async def cheatsheet(ctx):
    await ctx.send(
        f"""**Available cheatsheets:**
        \tSetting Stats: setcommands
        \tSetting Saving Throws: svcommands
        \tAvailable Saving Throws: stcommands
        \tAvailable Checks: chcommands
        \tOther commands: othercommands"""
    )

@bot.command()
async def setcommands(ctx):
    set_list = []
    for command in bot.commands:
        if command.brief:
            if "save" in command.brief:
                continue
            elif "Sets" in command.brief:
                set_list.append(f"**{command.name}**: {command.brief}")
    set_message = "\n".join(set_list)
    await ctx.send(f"**Available set commands:**\n{set_message}")

@bot.command()
async def svcommands(ctx):
    save_list = []
    for command in bot.commands:
        if command.brief:
            if "save" in command.brief:
                save_list.append(f"**{command.name}**: {command.brief}")
    save_message = "\n".join(save_list)
    await ctx.send(f"**Available set-save commands:**\n{save_message}")

@bot.command()
async def stcommands(ctx):
    saving_throws = []
    for command in bot.commands:
        if command.brief:
            if "Saving Throw" in command.brief:
                saving_throws.append(f"**{command.name}**: {command.brief}")
    st_message = "\n".join(saving_throws)
    await ctx.send(f"**Available saving throws:**\n{st_message}")

@bot.command()
async def chcommands(ctx):
    check_list = []
    for command in bot.commands:
        if command.brief:
            if "Check" in command.brief:
                check_list.append(f"**{command.name}**: {command.brief}")
    check_message = "\n".join(check_list)
    await ctx.send(f"**Available checks:**\n{check_message}")

@bot.command()
async def othercommands(ctx):
    command_list = []
    for command in bot.commands:
        if command.brief:
            if not "Sets" in command.brief and not "Check" in command.brief and not "Saving Throw" in command.brief:
                command_list.append(f"**{command.name}**: {command.brief}")
    help_message = "\n".join(command_list)
    await ctx.send(f"**Other commands:**\n{help_message}")


@bot.command(brief="Creates a character\n\tInputs: name\n\tThis will not work if there is already a character with the given name")
async def createcharacter(ctx, name):
    if not name:
        await ctx.send("Please give your character a name")
        return

    character = character_collections.find_one({"name": name})
    if character:
        await ctx.send(f"Character with name '{name}' already exists")
        return

    character_data = {
        "name": name,
        "level": 1,
        "strength": 0,
        "dex": 0,
        "con": 0,
        "int": 0,
        "wisdom": 0,
        "charisma": 0,
        "pb": 0,
        "strength_save": 0,
        "dex_save": 0,
        "con_save": 0,
        "intelligence_save": 0,
        "wisdom_save": 0,
        "charisma_save": 0,
        "acrobatics": 0,
        "animal_handling": 0,
        "arcana": 0,
        "athletics": 0,
        "deception": 0,
        "history": 0,
        "insight": 0,
        "intimidation": 0,
        "investigation": 0,
        "medicine": 0,
        "nature": 0,
        "perception": 0,
        "performance": 0,
        "persuasion": 0,
        "religion": 0,
        "slight_of_hand": 0,
        "stealth": 0,
        "survival": 0,
    }
    character_collections.insert_one(character_data)
    await ctx.send(f"{name} has been created")

def save_player_data(player_data):
    with open("player_data.json", 'w') as file:
        json.dump(player_data, file)

def load_player_data():
    try:
        with open('player_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

player_data = load_player_data()

@bot.command(brief="Switches to the character you want to play as\n\tInput: character's name")
async def switch(ctx, name):
    user = ctx.message.author.name

    match user:
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Name switched to {name}")
        case _:
            return

    save_player_data(player_data)


async def get_character(ctx):
    user = ctx.message.author.name

    match user:
        case "discord name":
            character = character_collections.find_one({"name": player_data.get(user)})
        case "discord name":
            character = character_collections.find_one({"name": player_data.get(user)})
        case "discord name":
            character = character_collections.find_one({"name": player_data.get(user)})
        case "discord name":
            character = character_collections.find_one({"name": player_data.get(user)})
        case _:
            return

    return character

async def set_stat(ctx, stat, stat_name, value):
    character = await get_character(ctx)
    if character:
        character_collections.update_one({"name": character['name']}, {"$set": {stat: value}})
        await ctx.send(f"{character['name']}'s {stat_name} updated")
    else:
        await ctx.send(f"{ctx.message.author.name} does not have an active PC")

@bot.command(brief="Sets your character level\n\tInput: level")
async def setlvl(ctx, save = 0):
    await set_stat(ctx, "level", "level", save)

@bot.command(brief="Sets your strength\n\tInput: stat value")
async def setstr(ctx, save = 0):
    await set_stat(ctx, "strength", "strength", save)

@bot.command(brief="Sets your dex\n\tInput: stat value")
async def setdex(ctx, save = 0):
    await set_stat(ctx, "dex", "dex", save)

@bot.command(brief="Sets your con\n\tInput: stat value")
async def setcon(ctx, save = 0):
    await set_stat(ctx, "con", "con", save)

@bot.command(brief="Sets your intelligence\n\tInput: stat value")
async def setint(ctx, save = 0):
    await set_stat(ctx, "int", "intelligence", save)

@bot.command(brief="Sets your wisdom\n\tInput: stat value")
async def setwis(ctx, save = 0):
    await set_stat(ctx, "wisdom", "wisdom", save)

@bot.command(brief="Sets your charisma\n\tInput: stat value")
async def setcha(ctx, save = 0):
    await set_stat(ctx, "charisma", "charisma", save)

@bot.command(brief="Sets your proficiency bonus\n\tInput: stat value")
async def setpro(ctx, save = 0):
    await set_stat(ctx, "pb", "proficiency bonus", save)

@bot.command(brief="Sets your strength save\n\tInput: save value")
async def setstrsave(ctx, save = 0):
    await set_stat(ctx, "strength_save", "strength save", save)

@bot.command(brief="Sets your dex save\n\tInput: save value")
async def setdexsave(ctx, save = 0):
    await set_stat(ctx, "dex_save", "dex save", save)

@bot.command(brief="Sets your con save\n\tInput: save value")
async def setconsave(ctx, save = 0):
    await set_stat(ctx, "con_save", "con save", save)

@bot.command(brief="Sets your int save\n\tInput: save value")
async def setintsave(ctx, save = 0):
    await set_stat(ctx, "intelligence_save", "intelligence save", save)

@bot.command(brief="Sets your wisdom save\n\tInput: save value")
async def setwissave(ctx, save = 0):
    await set_stat(ctx, "wisdom_save", "wisdom save", save)

@bot.command(brief="Sets your charisma save\n\tInput: save value")
async def setchasave(ctx, save = 0):
    await set_stat(ctx, "charisma_save", "charisma save", save)

@bot.command(brief="Sets your acrobatics stat\n\tInput: stat value")
async def setacro(ctx, save = 0):
    await set_stat(ctx, "acrobatics", "acrobatics", save)

@bot.command(brief="Sets your animal handling stat\n\tInput: stat value")
async def setah(ctx, save = 0):
    await set_stat(ctx, "animal_handling", "animal handling", save)

@bot.command(brief="Sets your arcana stat\n\tInput: stat value")
async def setarc(ctx, save = 0):
    await set_stat(ctx, "arcana", "arcana", save)

@bot.command(brief="Sets your athletics stat\n\tInput: stat value")
async def setath(ctx, save = 0):
    await set_stat(ctx, "athletics", "athletics", save)

@bot.command(brief="Sets your deception stat\n\tInput: stat value")
async def setdec(ctx, save = 0):
    await set_stat(ctx, "deception", "deception", save)

@bot.command(brief="Sets your history stat\n\tInput: stat value")
async def sethis(ctx, save = 0):
    await set_stat(ctx, "history", "history", save)

@bot.command(brief="Sets your insight stat\n\tInput: stat value")
async def setins(ctx, save = 0):
    await set_stat(ctx, "insight", "insight", save)

@bot.command(brief="Sets your intimidation stat\n\tInput: stat value")
async def setintim(ctx, save = 0):
    await set_stat(ctx, "intimidation", "intimidation", save)

@bot.command(brief="Sets your investigation stat\n\tInput: stat value")
async def setinv(ctx, save = 0):
    await set_stat(ctx, "investigation", "investigation", save)

@bot.command(brief="Sets your medicine stat\n\tInput: stat value")
async def setmed(ctx, save = 0):
    await set_stat(ctx, "medicine", "medicine", save)

@bot.command(brief="Sets your nature stat\n\tInput: stat value")
async def setnat(ctx, save = 0):
    await set_stat(ctx, "nature", "nature", save)

@bot.command(brief="Sets your perception stat\n\tInput: stat value")
async def setperc(ctx, save = 0):
    await set_stat(ctx, "perception", "perception", save)

@bot.command(brief="Sets your persuasion stat\n\tInput: stat value")
async def setpers(ctx, save = 0):
    await set_stat(ctx, "persuasion", "persuasion", save)

@bot.command(brief="Sets your performance stat\n\tInput: stat value")
async def setperf(ctx, save = 0):
    await set_stat(ctx, "performance", "performance", save)

@bot.command(brief="Sets your religion stat\n\tInput: stat value")
async def setrel(ctx, save = 0):
    await set_stat(ctx, "religion", "religion", save)

@bot.command(brief="Sets your slight of hand stat\n\tInput: stat value")
async def setsoh(ctx, save = 0):
    await set_stat(ctx, "slight_of_hand", "slight of hand", save)

@bot.command(brief="Sets your stealth stat\n\tInput: stat value")
async def setste(ctx, save = 0):
    await set_stat(ctx, "stealth", "stealth", save)

@bot.command(brief="Sets your survival stat\n\tInput: stat value")
async def setsur(ctx, save = 0):
    await set_stat(ctx, "survival", "survival", save)


@bot.command(brief="Rolls a dice\n\tInputs: 3d8/100d20 bonus(+2)\n\tIf no bonus, don't put anything\n\tThe bonus will be added to the sum of the dice, not each individual dice")
async def roll(ctx, dice_value, bonus_dmg=0):
    if not bonus_dmg:
        bonus_dmg = 0
    match = re.match(r'^(\d+)d(\d+)$', dice_value)
    if not match:
        await ctx.send("Invalid roll format. Use [number]d[sides]")
        return

    num_dice = int(match.group(1))
    num_sides = int(match.group(2))

    if num_dice < 1 or num_sides < 2:
        await ctx.send("Invalid dice config. Number of dice must be positive and sides must be greater than 2")
        return

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total_roll = sum(rolls)
    if num_dice == 1 and num_sides == 20:
        if rolls[0] == 20:
            await ctx.send("Your God has chosen to be gracious")
        if rolls[0] == 2:
            await ctx.send("Your God has chosen to be merciful")
        if rolls[0] == 1:
            await ctx.send("Your God has chosen to smite you")
    await ctx.send(f"Rolling {dice_value}: {', '.join(map(str, rolls))}.\nTotal: {total_roll + int(bonus_dmg)}")

@bot.command(brief="Rolls damage dice\n\tInputs: 2d20 15\n\t15 will be added to each roll")
async def rdmg(ctx, dice_value, bonus_dmg=0):
    match = re.match(r'^(\d+)d(\d+)$', dice_value)
    if not match:
        await ctx.send("Invalid roll format. Use [number]d[sides]")
        return

    num_dice = int(match.group(1))
    num_sides = int(match.group(2))

    if num_dice < 1 or num_sides < 2:
        await ctx.send("Invalid dice config. Number of dice must be positive and sides must be greater than 2")
        return

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    final_rolls = [idx + bonus_dmg for idx in rolls]
    total_roll = sum(final_rolls)
    await ctx.send(f"Rolling {dice_value}: {', '.join(map(str, rolls))}.\nDice with bonus damage: {', '.join(map(str, final_rolls))}\nTotal: {total_roll}")


@bot.command(brief="Roll for the number of attacks in one turn + modifier + if you have adv (greater than 0 for adv, less than 0 for disadv)\n\tAdvantage: 8d20 16 1\n\tStraight: 2d20 15\n\tStraight: 2d20 15 -1\n\tNo Modifier: 8d20 0 1\n\tModifier will be added to each unique roll")
async def ratk(ctx, dice_value, bonus=0, adv=0):
    match = re.match(r'^(\d+)d(\d+)$', dice_value)
    if not match:
        await ctx.send("Invalid roll format. Use [number]d[sides]")
        return
    num_dice = int(match.group(1))
    num_sides = int(match.group(2))

    if num_dice < 1 or num_sides < 2:
        await ctx.send("Invalid dice config. Number of dice must be positive and sides must be greater than 2")
        return

    first_rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    second_rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    if adv > 0:
        final_rolls = [max(roll1, roll2) + bonus for roll1, roll2 in zip(first_rolls, second_rolls)]
        await ctx.send(f"First Set of Rolls:\t\t {first_rolls}\nSecond Set of Rolls:\t{second_rolls}\nFinal Rolls with bonuses:\t{final_rolls}")
    elif adv < 0:
        final_rolls = [min(roll1, roll2) + bonus for roll1, roll2 in zip(first_rolls, second_rolls)]
        await ctx.send(f"First Set of Rolls:\t\t {first_rolls}\nSecond Set of Rolls:\t{second_rolls}\nFinal Rolls with bonuses:\t{final_rolls}")
    else:
        final_rolls = [idx + bonus for idx in first_rolls]
        await ctx.send(f"Initial Rolls:\t {first_rolls}\nFinal Rolls with bonuses:\t {final_rolls}")


async def rollstats(ctx, dc_type, adv=0):
    user = ctx.message.author.name
    base_stats = ['strength', 'dex', 'con', 'int', 'wisdom', 'charisma']
    character = await get_character(ctx)
    if character:
        if dc_type in base_stats:
            modifier = (int(character[dc_type]) - 10) // 2
        else:
            modifier = int(character[dc_type])

        roll1 = random.randint(1, 20) + modifier
        roll2 = random.randint(1, 20) + modifier

        if adv > 0:
            final_roll = roll1 if roll1 > roll2 else roll2
        elif adv < 0:
            final_roll = roll2 if roll1 > roll2 else roll1
        else:
            final_roll = roll1
            await ctx.send(f"The Initial roll is: {roll1 - modifier}")
            await ctx.send(f"The final roll is: {roll1}")

        if adv != 0:
            await ctx.send(f"The first roll is: {roll1 - modifier}")
            await ctx.send(f"The second roll is: {roll2 - modifier}")
            await ctx.send(f"The final roll is: {final_roll}")

    else:
        await ctx.send(f"{user} does not have a current PC")


# Saving Throw Commands
@bot.command(brief="Strength Saving Throw")
async def strsave(ctx, adv=0):
    await rollstats(ctx, 'strength_save', adv)

@bot.command(brief="Dex Saving Throw")
async def dexsave(ctx, adv=0):
    await rollstats(ctx, 'dex_save', adv)

@bot.command(brief="Con Saving Throw")
async def consave(ctx, adv=0):
    await rollstats(ctx, 'con_save', adv)

@bot.command(brief="Intelligence Saving Throw")
async def intsave(ctx, adv=0):
    await rollstats(ctx, 'intelligence_save', adv)

@bot.command(brief="Wisdom Saving Throw")
async def wissave(ctx, adv=0):
    await rollstats(ctx, 'wisdom_save', adv)

@bot.command(brief="Charisma Saving Throw")
async def chasave(ctx, adv=0):
    await rollstats(ctx, 'charisma_save', adv)

# _ Check commands
@bot.command(brief="Strength Check")
async def strcheck(ctx, adv=0):
    await rollstats(ctx, 'strength', adv)

@bot.command(brief="Dex Check")
async def dexcheck(ctx, adv=0):
    await rollstats(ctx, 'dex', adv)

@bot.command(brief="Con Check")
async def concheck(ctx, adv=0):
    await rollstats(ctx, 'con', adv)

@bot.command(brief="Intelligence Check")
async def intcheck(ctx, adv=0):
    await rollstats(ctx, 'int', adv)

@bot.command(brief="Wisdom Check")
async def wischeck(ctx, adv=0):
    await rollstats(ctx, 'wisdom', adv)

@bot.command(brief="Charisma Check")
async def chacheck(ctx, adv=0):
    await rollstats(ctx, 'charisma', adv)

@bot.command(brief="Acrobatics Check")
async def acrocheck(ctx, adv=0):
    await rollstats(ctx, 'acrobatics', adv)

@bot.command(brief="Animal Handling Check")
async def ahcheck(ctx, adv=0):
    await rollstats(ctx, 'animal_handling', adv)

@bot.command(brief="Arcana Check")
async def arccheck(ctx, adv=0):
    await rollstats(ctx, 'arcana', adv)

@bot.command(brief="Athletics Check")
async def athcheck(ctx, adv=0):
    await rollstats(ctx, 'athletics', adv)

@bot.command(brief="Deception Check")
async def deccheck(ctx, adv=0):
    await rollstats(ctx, 'deception', adv)

@bot.command(brief="History Check")
async def hischeck(ctx, adv=0):
    await rollstats(ctx, 'history', adv)

@bot.command(brief="Insight Check")
async def inscheck(ctx, adv=0):
    await rollstats(ctx, 'insight', adv)

@bot.command(brief="Intimidation Check")
async def intimcheck(ctx, adv=0):
    await rollstats(ctx, 'intimidation', adv)

@bot.command(brief="Investigation Check")
async def invcheck(ctx, adv=0):
    await rollstats(ctx, 'investigation', adv)

@bot.command(brief="Medicine Check")
async def medcheck(ctx, adv=0):
    await rollstats(ctx, 'medicine', adv)

@bot.command(brief="Nature Check")
async def natcheck(ctx, adv=0):
    await rollstats(ctx, 'nature', adv)

@bot.command(brief="Perception Check")
async def perccheck(ctx, adv=0):
    await rollstats(ctx, 'perception', adv)

@bot.command(brief="Performance Check")
async def perfcheck(ctx, adv=0):
    await rollstats(ctx, 'performance', adv)

@bot.command(brief="Persuasion Check")
async def perscheck(ctx, adv=0):
    await rollstats(ctx, 'persuasion', adv)

@bot.command(brief="Religion Check")
async def relcheck(ctx, adv=0):
    await rollstats(ctx, 'religion', adv)

@bot.command(brief="Slight of Hand Check")
async def sohcheck(ctx, adv=0):
    await rollstats(ctx, 'slight_of_hand', adv)

@bot.command(brief="Stealth Check")
async def stealthcheck(ctx, adv=0):
    await rollstats(ctx, 'stealth', adv)

@bot.command(brief="Survival Check")
async def surcheck(ctx, adv=0):
    await rollstats(ctx, 'survival', adv)

@bot.command(brief="For the person who is running the bot/the person who owns the DB only")
async def newcampaign(ctx, password):
    if password != "password goes here":
        await ctx.send("No deleting stuff for you")
    else:
        character_collections.delete_many({})

bot.run('discord bot token goes here')
