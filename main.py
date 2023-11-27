import discord
from discord.ext import commands
import pymongo
import random
import re
import uuid

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

client = pymongo.MongoClient(
    "mongodb+srv://<username>:<password>@cluster0.pb7fxj4.mongodb.net/?retryWrites=true&w=majority"
)
db = client.DND
character_collections = db.Characters


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    roll_or_die = bot.get_channel(1171843834699845632)
    if roll_or_die:
        await roll_or_die.send("Your God has awakened")


@bot.command()
async def cheatsheet(ctx):
    command_list = []
    for command in bot.commands:
        if command.brief:
            command_list.append(f"**{command.name}**: {command.brief}")
    help_message = "\n\n".join(command_list)
    await ctx.send(f"Available commands:\n{help_message}")


@bot.command(brief="Creates a character\nInputs: name level strength dex con intelligence wisdom charisma sanity proficiency bonus")
async def createcharacter(ctx, name, level, strength, dex, con, intel, wisdom, rizz, san, probo):
    if not level or not name or not strength or not dex or not con or not intel or not wisdom or not rizz or not san or not probo:
        await ctx.send(
            "Please provide all the required information: `!createcharacter [name] [strength] [dex] [constitution] [intelligence] [wisdom] [charisma] [sanity] [proficiency bonus]`"
        )
        return

    character_id = str(uuid.uuid4())
    character_data = {
        "_id": character_id,
        "name": name,
        "level": level,
        "strength": strength,
        "dex": dex,
        "con": con,
        "int": intel,
        "wisdom": wisdom,
        "charisma": rizz,
        "sanity": san,
        "pb": probo,
        "strength_save": '0',
        "dex_save": '0',
        "con_save": '0',
        "intelligence_save": '0',
        "wisdom_save": '0',
        "charisma_save": '0',
        "sanity_save": '0',
        "acrobatics": '0',
        "animal_handling": '0',
        "arcana": '0',
        "athletics": '0',
        "deception": '0',
        "history": '0',
        "insight": '0',
        "intimidation": '0',
        "investigation": '0',
        "medicine": '0',
        "nature": '0',
        "perception": '0',
        "performance": '0',
        "persuasion": '0',
        "religion": '0',
        "slight_of_hand": '0',
        "stealth": '0',
        "survival": '0',
        "marshall": '0',
    }

    result = db.insert_one(character_data)
    await ctx.send(f"Character {name} created with ID: {result.character_id}")


@bot.command(brief="Sets a character saving throws\nInput: character id strength dex con intelligence wisdom charisma sanity")
async def setsavingthrows(ctx, character_id, strength, dex, con, intelligence, wisdom, charisma, sanity):
    if not character_id or not strength or not dex or not con or not intelligence or not wisdom or not charisma or not sanity:
        await ctx.send(
            "Please provide all required information: `[character id] [strength save] [dex save] [con save] [intelligence save] [wisdom save] [charisma save] [sanity save]"
        )
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        character_collections.update_one({"_id": character_id}, {"strength save": strength})
        character_collections.update_one({"_id": character_id}, {"dex save": dex})
        character_collections.update_one({"_id": character_id}, {"con save": con})
        character_collections.update_one({"_id": character_id}, {"int save": intelligence})
        character_collections.update_one({"_id": character_id}, {"wisdom save": wisdom})
        character_collections.update_one({"_id": character_id}, {"charisma save": charisma})
        character_collections.update_one({"_id": character_id}, {"sanity save": sanity})
    else:
        await ctx.send(
            "Character not found. Use the `!getcharacterid [character name]` command to get the id's of all the characters with that name."
        )


@bot.command(brief="Sets the character skills\nInputs: character id acrobatics animal handling arcana ... alphabetical order")
async def setskills(ctx, character_id, acro, animal, arc, athl, dece, hist, insi, inti, inve, medi, natu, perc, perf,
                    pers, reli, soh, stea, surv, marsh):
    if not character_id or not acro or not animal or not arc or not athl or not dece or not hist or not insi or not inti or not inve or not medi or not natu or not perc or not perf or not pers or not reli or not soh or not stea or not surv or not marsh:
        ctx.send(
            "Please provide all required information: `[character id] [acrobatics] [animal handling] [arcana] [athletics] [deception] [history] [insight] [intimidation] [investigation] [medicine] [nature] [perception] [performance] [persuasion] [religion] [slight of hand] [stealth] [survival]`"
        )
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        character_collections.update_one({"_id": character_id}, {"acrobatics": acro})
        character_collections.update_one({"_id": character_id}, {"animal handling": animal})
        character_collections.update_one({"_id": character_id}, {"arcana": arc})
        character_collections.update_one({"_id": character_id}, {"athletics": athl})
        character_collections.update_one({"_id": character_id}, {"deception": dece})
        character_collections.update_one({"_id": character_id}, {"history": hist})
        character_collections.update_one({"_id": character_id}, {"insight": insi})
        character_collections.update_one({"_id": character_id}, {"intimidation": inti})
        character_collections.update_one({"_id": character_id}, {"investigation": inve})
        character_collections.update_one({"_id": character_id}, {"medicine": medi})
        character_collections.update_one({"_id": character_id}, {"nature": natu})
        character_collections.update_one({"_id": character_id}, {"perception": perc})
        character_collections.update_one({"_id": character_id}, {"performance": perf})
        character_collections.update_one({"_id": character_id}, {"persuasion": pers})
        character_collections.update_one({"_id": character_id}, {"religion": reli})
        character_collections.update_one({"_id": character_id}, {"slight of hand": soh})
        character_collections.update_one({"_id": character_id}, {"stealth": stea})
        character_collections.update_one({"_id": character_id}, {"survival": surv})
        character_collections.update_one({"_id": character_id}, {"marshall": marsh})
    else:
        await ctx.send(
            "Character not found. Use the `!getcharacterid [character name]` command to get the id's of all the characters with that name."
        )


@bot.command(brief="Gets a characters id by name\nInputs: character name")
async def getcharacterid(ctx, character_name):
    characters = character_collections.find({'name': character_name})
    for character in characters:
        await ctx.send(f"The ID for {character_name} is: {character['_id']}")
    if characters.count() == 0:
        await ctx.send(f"No characters found with the name: {character_name}")


@bot.command(brief="Gets a character's stats.\nInput: character id")
async def getstats(ctx, character_id):
    character = character_collections.find_one({"_id": character_id})
    if character:
        formatted_stats = "\n".join([f"{key}: {value}" for key, value in character.items()])
        await ctx.send(f"Stats for character with ID `{character_id}`:\n{formatted_stats}")
    else:
        await ctx.send(f"No character found with ID: {character_id}")


@bot.command(brief="Updates a character's stats.\nInput: character id, stat name, new value")
async def updatestat(ctx, character_id, stat, value):
    if not character_id or not stat or not value:
        await ctx.send(
            "Please provide all the required information: `!updatestat [character id] [name] [stat] [value]`"
        )
        return

    try:
        value = int(value)
    except ValueError:
        await ctx.send("Invalid stat value")
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        if stat in character:
            character[stat] = value
            character_collections.update_one({"_id": character_id}, {"$set": {stat: value}})
            await ctx.send(f"Updated {stat} for character {character['name']} to {value}")
        else:
            await ctx.send(f"Stat {stat} does not exist for this character.")
    else:
        await ctx.send(
            "Character not found. Use the `!getcharacterid [character name]` command to get the id's of all the characters with that name."
        )


@bot.command(brief="Shatters the glass blade")
async def shatter(ctx):
    shatter_roll = random.randint(1, 12)
    await ctx.send(f"The shatter roll is: {shatter_roll}")


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


@bot.command(brief="Input: plus to hit\nIf no bonus to hit, don't put anything")
async def tohit(ctx, bonus=0):
    random_number = random.randint(1, 20) + int(bonus)
    if random_number - int(bonus) == 20:
        await ctx.send("Your God has chosen to be gracious")
    if random_number - int(bonus) == 2:
        await ctx.send("Your God has chosen to be merciful")
    if random_number - int(bonus) == 1:
        await ctx.send("Your God has chosen to smite you")
    await ctx.send(f"The initial roll is: {random_number - int(bonus)}\nThe attack roll is: {random_number}")


@bot.command(brief="Input: character id, type of roll")
async def advantage(ctx, character_id, roll_type):
    if not character_id or not roll_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        await ctx.send(f"{character['name']}")
        match roll_type:
            case 'strength_save':
                modifier = int(character['strength_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'dex_save':
                modifier = int(character['dex_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'con_save':
                modifier = int(character['con_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'int_save':
                modifier = int(character['intelligence_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'wisdom_save':
                modifier = int(character['wisdom_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'charisma_save':
                modifier = int(character['charisma_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'sanity_save':
                modifier = int(character['sanity_save'])
                await roll_adv_dis(ctx, modifier, True)
            case 'strength':
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
            case 'wisdom':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'charisma':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'sanity':
                modifier = (int(character['sanity']) - 10) // 2
                await roll_adv_dis(ctx, modifier, True)
            case 'acrobatics':
                await roll_adv_dis(ctx, character['acrobatics'], True)
            case 'animal_handling':
                await roll_adv_dis(ctx, character['animal_handling'], True)
            case 'arcana':
                await roll_adv_dis(ctx, character['arcana'], True)
            case 'athletics':
                await roll_adv_dis(ctx, character['athletics'], True)
            case 'deception':
                await roll_adv_dis(ctx, character['deception'], True)
            case 'history':
                await roll_adv_dis(ctx, character['history'], True)
            case 'insight':
                await roll_adv_dis(ctx, character['insight'], True)
            case 'intimidation':
                await roll_adv_dis(ctx, character['intimidation'], True)
            case 'investigation':
                await roll_adv_dis(ctx, character['investigation'], True)
            case 'medicine':
                await roll_adv_dis(ctx, character['medicine'], True)
            case 'nature':
                await roll_adv_dis(ctx, character['nature'], True)
            case 'perception':
                await roll_adv_dis(ctx, character['perception'], True)
            case 'performance':
                await roll_adv_dis(ctx, character['performance'], True)
            case 'persuasion':
                await roll_adv_dis(ctx, character['persuasion'], True)
            case 'religion':
                await roll_adv_dis(ctx, character['religion'], True)
            case 'slight_of_hand':
                await roll_adv_dis(ctx, character['slight_of_hand'], True)
            case 'stealth':
                await roll_adv_dis(ctx, character['stealth'], True)
            case 'survival':
                await roll_adv_dis(ctx, character['survival'], True)
            case 'marshall':
                await roll_adv_dis(ctx, character['marshall'], True)
            case _:
                await ctx.send("Types of saves/checks are: 'strength_save' 'dex_save' 'con_save' 'int_save' 'wisdom_save' 'charisma_save' 'sanity_save' 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'sanity' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival' 'marshall'")
    else:
        await ctx.send(f"No character found with ID: {character_id}")


@bot.command(brief="Input: character id, type of roll")
async def disadvantage(ctx, character_id, roll_type):
    if not character_id or not roll_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        await ctx.send(f"{character['name']}")
        match roll_type:
            case 'strength_save':
                modifier = int(character['strength_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'dex_save':
                modifier = int(character['dex_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'con_save':
                modifier = int(character['con_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'int_save':
                modifier = int(character['intelligence_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'wisdom_save':
                modifier = int(character['wisdom_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'charisma_save':
                modifier = int(character['charisma_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'sanity_save':
                modifier = int(character['sanity_save'])
                await roll_adv_dis(ctx, modifier, False)
            case 'strength':
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
            case 'wisdom':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'charisma':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'sanity':
                modifier = (int(character['sanity']) - 10) // 2
                await roll_adv_dis(ctx, modifier, False)
            case 'acrobatics':
                await roll_adv_dis(ctx, character['acrobatics'], False)
            case 'animal_handling':
                await roll_adv_dis(ctx, character['animal_handling'], False)
            case 'arcana':
                await roll_adv_dis(ctx, character['arcana'], False)
            case 'athletics':
                await roll_adv_dis(ctx, character['athletics'], False)
            case 'deception':
                await roll_adv_dis(ctx, character['deception'], False)
            case 'history':
                await roll_adv_dis(ctx, character['history'], False)
            case 'insight':
                await roll_adv_dis(ctx, character['insight'], False)
            case 'intimidation':
                await roll_adv_dis(ctx, character['intimidation'], False)
            case 'investigation':
                await roll_adv_dis(ctx, character['investigation'], False)
            case 'medicine':
                await roll_adv_dis(ctx, character['medicine'], False)
            case 'nature':
                await roll_adv_dis(ctx, character['nature'], False)
            case 'perception':
                await roll_adv_dis(ctx, character['perception'], False)
            case 'performance':
                await roll_adv_dis(ctx, character['performance'], False)
            case 'persuasion':
                await roll_adv_dis(ctx, character['persuasion'], False)
            case 'religion':
                await roll_adv_dis(ctx, character['religion'], False)
            case 'slight_of_hand':
                await roll_adv_dis(ctx, character['slight_of_hand'], False)
            case 'stealth':
                await roll_adv_dis(ctx, character['stealth'], False)
            case 'survival':
                await roll_adv_dis(ctx, character['survival'], False)
            case 'marshall':
                await roll_adv_dis(ctx, character['marshall'], False)
            case _:
                await ctx.send(
                    "Types of saves/checks are: 'strength' 'dex_save' 'con_save' 'int_save' 'wisdom_save' 'charisma_save' 'sanity_save' 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'sanity' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival' 'marshall'")
    else:
        await ctx.send(f"No character found with ID: {character_id}")


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
async def save(ctx, character_id, save_type):
    if not character_id or not save_type:
        await ctx.send("Please provide all required information: `[character_id] [type of save]`")
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        await ctx.send(f"{character['name']}")
        match save_type:
            case 'strength':
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
            case 'wisdom':
                modifier = int(character['wisdom_save'])
                await roll_check(ctx, 'wisdom save', modifier)
            case 'charisma':
                modifier = int(character['charisma_save'])
                await roll_check(ctx, 'charisma save', modifier)
            case 'sanity':
                modifier = int(character['sanity_save'])
                await roll_check(ctx, 'sanity save', modifier)
            case _:
                await ctx.send("Types of save are: 'strength', 'dex', 'con', 'int', 'wisdom', 'charisma' or 'sanity'")
    else:
        await ctx.send(f"No character found with ID: {character_id}")


@bot.command(brief="Rolls a check.\nInput character id and type of check")
async def check(ctx, character_id, check_type):
    if not character_id or not check_type:
        await ctx.send("Please provide all required information: `[character_id] [type of check]`")
        return

    character = character_collections.find_one({"_id": character_id})
    if character:
        await ctx.send(f"{character['name']}")
        match check_type:
            case 'strength':
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
            case 'wisdom':
                modifier = (int(character['wisdom']) - 10) // 2
                await roll_check(ctx, 'wisdom', modifier)
            case 'charisma':
                modifier = (int(character['charisma']) - 10) // 2
                await roll_check(ctx, 'charisma', modifier)
            case 'sanity':
                modifier = (int(character['sanity']) - 10) // 2
                await roll_check(ctx, 'sanity', modifier)
            case 'acrobatics':
                await roll_check(ctx, 'acrobatics', character['acrobatics'])
            case 'animal_handling':
                await roll_check(ctx, 'animal handling', character['animal_handling'])
            case 'arcana':
                await roll_check(ctx, 'arcana', character['arcana'])
            case 'athletics':
                await roll_check(ctx, 'athletics', character['athletics'])
            case 'deception':
                await roll_check(ctx, 'deception', character['deception'])
            case 'history':
                await roll_check(ctx, 'history', character['history'])
            case 'insight':
                await roll_check(ctx, 'insight', character['insight'])
            case 'intimidation':
                await roll_check(ctx, 'intimidation', character['intimidation'])
            case 'investigation':
                await roll_check(ctx, 'investigation', character['investigation'])
            case 'medicine':
                await roll_check(ctx, 'medicine', character['medicine'])
            case 'nature':
                await roll_check(ctx, 'nature', character['nature'])
            case 'perception':
                await roll_check(ctx, 'perception', character['perception'])
            case 'performance':
                await roll_check(ctx, 'performance', character['performance'])
            case 'persuasion':
                await roll_check(ctx, 'persuasion', character['persuasion'])
            case 'religion':
                await roll_check(ctx, 'religion', character['religion'])
            case 'slight_of_hand':
                await roll_check(ctx, 'slight of hand', character['slight_of_hand'])
            case 'stealth':
                await roll_check(ctx, 'stealth', character['stealth'])
            case 'survival':
                await roll_check(ctx, 'survival', character['survival'])
            case 'marshall':
                await roll_check(ctx, 'marshall', character['marshall'])
            case _:
                await ctx.send("Types of checks are: 'strength' 'dex' 'con' 'int' 'wisdom' 'charisma' 'sanity' 'acrobatics' 'animal_handling' 'arcana' 'athletics' 'deception' 'history' 'insight' 'intimidation' 'investigation' 'medicine' 'nature' 'perception' 'performance' 'persuasion' 'religion' 'slight_of_hand' 'stealth' 'survival' 'marshall'")
    else:
        await ctx.send(f"No character found with ID: {character_id}")


bot.run('//bot_token_here')
