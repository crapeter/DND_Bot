import discord
from discord.ext import commands
import pymongo
import random
import re

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

client = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.pb7fxj4.mongodb.net/?retryWrites=true&w=majority"
)
db = client.DND
character_collections = db.Characters


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # roll_or_die = bot.get_channel(discord channel id)
    # if roll_or_die:
        # await roll_or_die.send("Your God has awakened")


@bot.command()
async def cheatsheet(ctx):
    set_list = []
    save_list = []
    command_list = []
    for command in bot.commands:
        if command.brief:
            if "save" in command.brief:
                save_list.append(f"**{command.name}**: {command.brief}")
            elif "Sets" in command.brief:
                set_list.append(f"**{command.name}**: {command.brief}")
            else:
                command_list.append(f"**{command.name}**: {command.brief}")
    set_message = "\n".join(set_list)
    save_message = "\n".join(save_list)
    help_message = "\n".join(command_list)
    await ctx.send(f"**Available set commands:**\n{set_message}")
    await ctx.send(f"**Available set-save commands:**\n{save_message}")
    await ctx.send(f"**Other commands:**\n{help_message}")


@bot.command(brief="Creates a character\nInputs: name")
async def createcharacter(ctx, name):
    if not name:
        await ctx.send("Please give your character a name")

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

@bot.command(brief="Switches to the character you want to play as")
async def switch(ctx, name):
    user = ctx.message.author.name

    match user:
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Human name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Human name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Human name switched to {name}")
        case "discord name":
            player_data[user] = name
            await ctx.send(f"Human name switched to {name}")
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

@bot.command(brief="Sets your acrobatics stat\n\tInput: save value")
async def setacro(ctx, save = 0):
    await set_stat(ctx, "acrobatics", "acrobatics", save)

@bot.command(brief="Sets your animal handling stat\n\tInput: save value")
async def setah(ctx, save = 0):
    await set_stat(ctx, "animal_handling", "animal handling", save)

@bot.command(brief="Sets your arcana stat\n\tInput: save value")
async def setarc(ctx, save = 0):
    await set_stat(ctx, "arcana", "arcana", save)

@bot.command(brief="Sets your athletics stat\n\tInput: save value")
async def setath(ctx, save = 0):
    await set_stat(ctx, "athletics", "athletics", save)

@bot.command(brief="Sets your deception stat\n\tInput: save value")
async def setdec(ctx, save = 0):
    await set_stat(ctx, "deception", "deception", save)

@bot.command(brief="Sets your history stat\n\tInput: save value")
async def sethis(ctx, save = 0):
    await set_stat(ctx, "history", "history", save)

@bot.command(brief="Sets your insight stat\n\tInput: save value")
async def setins(ctx, save = 0):
    await set_stat(ctx, "insight", "insight", save)

@bot.command(brief="Sets your intimidation stat\n\tInput: save value")
async def setintim(ctx, save = 0):
    await set_stat(ctx, "intimidation", "intimidation", save)

@bot.command(brief="Sets your investigation stat\n\tInput: save value")
async def setinv(ctx, save = 0):
    await set_stat(ctx, "investigation", "investigation", save)

@bot.command(brief="Sets your medicine stat\n\tInput: save value")
async def setmed(ctx, save = 0):
    await set_stat(ctx, "medicine", "medicine", save)

@bot.command(brief="Sets your nature stat\n\tInput: save value")
async def setnat(ctx, save = 0):
    await set_stat(ctx, "nature", "nature", save)

@bot.command(brief="Sets your perception stat\n\tInput: save value")
async def setperc(ctx, save = 0):
    await set_stat(ctx, "perception", "perception", save)

@bot.command(brief="Sets your persuasion stat\n\tInput: save value")
async def setpers(ctx, save = 0):
    await set_stat(ctx, "persuasion", "persuasion", save)

@bot.command(brief="Sets your performance stat\n\tInput: save value")
async def setperf(ctx, save = 0):
    await set_stat(ctx, "performance", "performance", save)

@bot.command(brief="Sets your religion stat\n\tInput: save value")
async def setrel(ctx, save = 0):
    await set_stat(ctx, "religion", "religion", save)

@bot.command(brief="Sets your slight of hand stat\n\tInput: save value")
async def setsoh(ctx, save = 0):
    await set_stat(ctx, "slight_of_hand", "slight of hand", save)

@bot.command(brief="Sets your stealth stat\n\tInput: save value")
async def setste(ctx, save = 0):
    await set_stat(ctx, "stealth", "stealth", save)

@bot.command(brief="Sets your survival stat\n\tInput: save value")
async def setsur(ctx, save = 0):
    await set_stat(ctx, "survival", "survival", save)


@bot.command(brief="Rolls a dice\nInputs: 3d8/100d20 bonus(+2)\nIf no bonus, don't put anything")
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


@bot.command(brief="Roll for the number of attacks in one turn + modifier + if you have advantage (greater than 0 for adv, less than 0 for disadv)\nInput ex\n\tAdvantage: 8d20 16 1\n\tStraight: 2d20 15\n\tStraight: 2d20 15 -1")
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
        final_rolls = [max(roll1, roll2) + 16 for roll1, roll2 in zip(first_rolls, second_rolls)]
        await ctx.send(f"First Set of Rolls:\t\t {first_rolls}\nSecond Set of Rolls:\t{second_rolls}\nFinal Rolls with bonuses:\t{final_rolls}")
    elif adv < 0:
        final_rolls = [min(roll1, roll2) + 16 for roll1, roll2 in zip(first_rolls, second_rolls)]
        await ctx.send(f"First Set of Rolls:\t\t {first_rolls}\nSecond Set of Rolls:\t{second_rolls}\nFinal Rolls with bonuses:\t{final_rolls}")
    else:
        final_rolls = [idx + bonus for idx in first_rolls]
        await ctx.send(f"Initial Rolls:\t {first_rolls}\nFinal Rolls with bonuses:\t {final_rolls}")


@bot.command(brief="Input: character id, type of roll")
async def advantage(ctx, roll_type):
    user = ctx.message.author.name
    if not roll_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = await get_character(ctx)
    if character:
        await ctx.send(f"{character['name']}")
        match roll_type:
            case 'ssave':
                modifier = int(character['strength_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'dsave':
                modifier = int(character['dex_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'csave':
                modifier = int(character['con_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'isave':
                modifier = int(character['intelligence_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'wsave':
                modifier = int(character['wisdom_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'chsave':
                modifier = int(character['charisma_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'str':
                modifier = (int(character['strength']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'dex':
                modifier = (int(character['dex']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'con':
                modifier = (int(character['con']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'int':
                modifier = (int(character['int']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'wis':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'char':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'acro':
                await roll_adv_dis(ctx, character['acrobatics'], True)
            case 'animal':
                await roll_adv_dis(ctx, character['animal_handling'], True)
            case 'arc':
                await roll_adv_dis(ctx, character['arcana'], True)
            case 'ath':
                await roll_adv_dis(ctx, character['athletics'], True)
            case 'dec':
                await roll_adv_dis(ctx, character['deception'], True)
            case 'his':
                await roll_adv_dis(ctx, character['history'], True)
            case 'ins':
                await roll_adv_dis(ctx, character['insight'], True)
            case 'intimi':
                await roll_adv_dis(ctx, character['intimidation'], True)
            case 'inv':
                await roll_adv_dis(ctx, character['investigation'], True)
            case 'med':
                await roll_adv_dis(ctx, character['medicine'], True)
            case 'nat':
                await roll_adv_dis(ctx, character['nature'], True)
            case 'perc':
                await roll_adv_dis(ctx, character['perception'], True)
            case 'perf':
                await roll_adv_dis(ctx, character['performance'], True)
            case 'pers':
                await roll_adv_dis(ctx, character['persuasion'], True)
            case 'rel':
                await roll_adv_dis(ctx, character['religion'], True)
            case 'soh':
                await roll_adv_dis(ctx, character['slight_of_hand'], True)
            case 'stealth':
                await roll_adv_dis(ctx, character['stealth'], True)
            case 'sur':
                await roll_adv_dis(ctx, character['survival'], True)
            case _:
                await ctx.send("Types of saves/checks are: 'strength_save' 'dex_save' 'con_save' 'int_save' 'wisdom_save' 'charisma_save' 'sanity_save' 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'sanity' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival'")
    else:
        await ctx.send(f"{user} does not have a current PC")


@bot.command(brief="Input: character id, type of roll")
async def disadvantage(ctx, roll_type):
    user = ctx.message.author.name
    if not roll_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = await get_character(ctx)
    if character:
        await ctx.send(f"{character['name']}")
        match roll_type:
            case 'ssave':
                modifier = int(character['strength_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'dsave':
                modifier = int(character['dex_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'csave':
                modifier = int(character['con_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'isave':
                modifier = int(character['intelligence_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'wsave':
                modifier = int(character['wisdom_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'chsave':
                modifier = int(character['charisma_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'str':
                modifier = (int(character['strength']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'dex':
                modifier = (int(character['dex']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'con':
                modifier = (int(character['con']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'int':
                modifier = (int(character['int']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'wis':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'char':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'acro':
                await roll_adv_dis(ctx, character['acrobatics'], False)
            case 'animal':
                await roll_adv_dis(ctx, character['animal_handling'], False)
            case 'arc':
                await roll_adv_dis(ctx, character['arcana'], False)
            case 'ath':
                await roll_adv_dis(ctx, character['athletics'], False)
            case 'dec':
                await roll_adv_dis(ctx, character['deception'], False)
            case 'his':
                await roll_adv_dis(ctx, character['history'], False)
            case 'ins':
                await roll_adv_dis(ctx, character['insight'], False)
            case 'intimi':
                await roll_adv_dis(ctx, character['intimidation'], False)
            case 'inv':
                await roll_adv_dis(ctx, character['investigation'], False)
            case 'med':
                await roll_adv_dis(ctx, character['medicine'], False)
            case 'nat':
                await roll_adv_dis(ctx, character['nature'], False)
            case 'perc':
                await roll_adv_dis(ctx, character['perception'], False)
            case 'perf':
                await roll_adv_dis(ctx, character['performance'], False)
            case 'pers':
                await roll_adv_dis(ctx, character['persuasion'], False)
            case 'rel':
                await roll_adv_dis(ctx, character['religion'], False)
            case 'soh':
                await roll_adv_dis(ctx, character['slight_of_hand'], False)
            case 'stealth':
                await roll_adv_dis(ctx, character['stealth'], False)
            case 'sur':
                await roll_adv_dis(ctx, character['survival'], False)
            case _:
                await ctx.send(
                    "Types of saves/checks are: 'strength' 'dex_save' 'con_save' 'int_save' 'wisdom_save' 'charisma_save' 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'sanity' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival'")
    else:
        await ctx.send(f"{user} does not have a current PC")


async def roll_adv_dis(ctx, modifier, adv):
    rand1 = random.randint(1, 20) + int(modifier)
    rand2 = random.randint(1, 20) + int(modifier)
    if adv:
        if rand1 > rand2 and rand1 - int(modifier) == 20 or rand2 > rand1 and rand2 - int(modifier) == 20:
            await ctx.send("Your God has chosen to be gracious")
        if rand1 > rand2 and rand1 - int(modifier) == 2 or rand2 > rand1 and rand2 - int(modifier) == 2:
            await ctx.send("Your God has chosen to be merciful")
        if rand1 > rand2 and rand1 - int(modifier) == 1 or rand2 > rand1 and rand2 - int(modifier) == 1:
            await ctx.send("Your God has chosen to smite you")
        await ctx.send(f"\nThe first roll is: {rand1 - int(modifier)}\nThe second roll is: {rand2 - int(modifier)}\nThe final roll is: {rand1 if rand1 > rand2 else rand2}")
    else:
        if rand1 < rand2 and rand1 - int(modifier) == 20 or rand2 < rand1 and rand2 - int(modifier) == 20:
            await ctx.send("Your God has chosen to be gracious")
        if rand1 < rand2 and rand1 - int(modifier) == 2 or rand2 < rand1 and rand2 - int(modifier) == 2:
            await ctx.send("Your God has chosen to be merciful")
        if rand1 < rand2 and rand1 - int(modifier) == 1 or rand2 < rand1 and rand2 - int(modifier) == 1:
            await ctx.send("Your God has chosen to smite you")
        await ctx.send(f"\nThe first roll is: {rand1 - int(modifier)}\nThe second roll is: {rand2 - int(modifier)}\nThe final roll is: {rand1 if rand1 < rand2 else rand2}")


async def roll_check(ctx, check_type, modifier):
    roll_result = random.randint(1, 20)
    total_check = roll_result + int(modifier)
    if roll_result == 20:
        await ctx.send("Your God has chosen to be gracious")
    if roll_result == 2:
        await ctx.send("Your God has chosen to merciful")
    if roll_result == 1:
        await ctx.sent("Your God has chosen to smite you")
    await ctx.send(f"The d20 roll for {check_type} is: {roll_result}")
    await ctx.send(f"The total {check_type} check is: {total_check}")


@bot.command(brief="Rolls a saving throw.\nInput character id and type of saving throw")
async def save(ctx, save_type):
    user = ctx.message.author.name
    if not save_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = await get_character(ctx)
    if character:
        await ctx.send(f"{character['name']}")
        match save_type:
            case 'str':
                modifier = int(character['strength_save'])
                await roll_check(ctx, 'strength save', modifier)
            case 'dex':
                modifier = int(character['dex_save'])
                await roll_check(ctx, 'dexterity save', modifier)
            case 'con':
                modifier = int(character['con_save'])
                await roll_check(ctx, 'constitution save', modifier)
            case 'int':
                modifier = int(character['intelligence_save'])
                await roll_check(ctx, 'intelligence save', modifier)
            case 'wis':
                modifier = int(character['wisdom_save'])
                await roll_check(ctx, 'wisdom save', modifier)
            case 'char':
                modifier = int(character['charisma_save'])
                await roll_check(ctx, 'charisma save', modifier)
            case _:
                await ctx.send("Types of save are: 'strength', 'dex', 'con', 'int', 'wisdom', 'charisma'")
    else:
        await ctx.send(f"{user} does not have a current PC")


@bot.command(brief="Rolls a check.\nInput character id and type of check")
async def check(ctx, check_type):
    user = ctx.message.author.name
    if not check_type:
        await ctx.send("Please provide all required information: `[character_id] [type of check]`")
        return

    character = await get_character(ctx)
    if character:
        await ctx.send(f"{character['name']}")
        match check_type:
            case 'str':
                modifier = (int(character['strength']) - 10) // 2
                await roll_check(ctx, 'strength', modifier)
            case 'dex':
                modifier = (int(character['dex']) - 10) // 2
                await roll_check(ctx, 'dexterity', modifier)
            case 'con':
                modifier = (int(character['con']) - 10) // 2
                await roll_check(ctx, 'constitution', modifier)
            case 'int':
                modifier = (int(character['int']) - 10) // 2
                await roll_check(ctx, 'intelligence', modifier)
            case 'wis':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_check(ctx, 'wisdom', modifier)
            case 'char':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_check(ctx, 'charisma', modifier)
            case 'acro':
                await roll_check(ctx, 'acrobatics', character['acrobatics'])
            case 'animal':
                await roll_check(ctx, 'animal handling', character['animal_handling'])
            case 'arc':
                await roll_check(ctx, 'arcana', character['arcana'])
            case 'ath':
                await roll_check(ctx, 'athletics', character['athletics'])
            case 'dec':
                await roll_check(ctx, 'deception', character['deception'])
            case 'his':
                await roll_check(ctx, 'history', character['history'])
            case 'ins':
                await roll_check(ctx, 'insight', character['insight'])
            case 'intimi':
                await roll_check(ctx, 'intimidation', character['intimidation'])
            case 'inv':
                await roll_check(ctx, 'investigation', character['investigation'])
            case 'med':
                await roll_check(ctx, 'medicine', character['medicine'])
            case 'nat':
                await roll_check(ctx, 'nature', character['nature'])
            case 'perc':
                await roll_check(ctx, 'perception', character['perception'])
            case 'perf':
                await roll_check(ctx, 'performance', character['performance'])
            case 'pers':
                await roll_check(ctx, 'persuasion', character['persuasion'])
            case 'rel':
                await roll_check(ctx, 'religion', character['religion'])
            case 'soh':
                await roll_check(ctx, 'slight of hand', character['slight_of_hand'])
            case 'stealth':
                await roll_check(ctx, 'stealth', character['stealth'])
            case 'sur':
                await roll_check(ctx, 'survival', character['survival'])
            case _:
                await ctx.send("Types of checks are: 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival'")
    else:
        await ctx.send(f"{user} does not have a current PC")

@bot.command(brief="For MAINTAINER/BOT OPERATOR only")
async def newcampaign(ctx, password):
    if password != "random text goes here":
        await ctx.send("No deleting stuff for you")
    else:
        character_collections.delete_many({})


bot.run('discord token goes here')
