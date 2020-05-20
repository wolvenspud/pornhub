import discord
from discord.ext import commands
import random
import requests
import asyncio
import time
import re
import json
import sys


print("Loading Users... --Data")
users = dict()
try:
    with open("users.txt", "r") as f:
        users = json.load(f)
    time.sleep(2)
except Exception as e:
    print("DB EMPTY")
print("Loading Clans... --Data")
clans = dict()
try:
    with open("clans.txt", "r") as f:
        clans = json.load(f)
except Exception as e:
    print("DB EMPTY")
print("Loading Notifs... --Data")
clan_pending = dict()
try:
    with open("clanp.txt", "r") as f:
        clan_pending = json.load(f)
except Exception as e:
    print("DB EMPTY")
print("Loading Inventory... --Data")
inventory = dict()
try:
    with open("inv.txt", "r") as f:
        inventory = json.load(f)
except Exception as e:
    print("DB EMPTY")
print("Loading Adjectives... --Generator")
adj = list()
#f = open("adj.txt", "r")
#for i in f.readlines():
  #if len(i.strip())>0: adj.append(i.strip())
#f.close()
print("Loading Nouns... --Generator")
noun = list()
f = open("nouns.txt", "r")
for i in f.readlines():
  if len(i.strip())>0: noun.append(i.strip())
f.close()
'''print("Loading Pets... --Data")
pets = dict()
try:
    with open("pets.txt", "r") as f:
        pets = json.load(f)
except Exception as e:
    print("DB EMPTY")'''
print("Loading Actions... --Generator")
acts = ["eats their family",
        "eats their imouto",
        "captures loli in their van",
        "touches Kizuna Ai",
        "plays too much overwatch",
        "enslaves pokemon everday",
        "feeds Donald Trump",
        "is lurking around and watching you",
        "is hiding in your shadow",
        "wants to hit the person above this message",
        "wants some friends",
        "wants a harem",
        "has too many girlfriends",
        "is responsible for the death of Kanna Kamui",
        "is responsible for the death of Sasuke",
        "likes to eat akino",
        "has a questionable existence",
        "wants to be friends with shinobu",
        "wants a loli harem",
        "thinks they are a ninja",
        "is actually Jeff Kaplan in disguise",
        "watches Ore no Imouto ga Konnani Kawaii Wake ga nai",
        "watches eromanga sensei as a part time job",
        "feeds on akino's sorrow",
        "has no dreams",
        "gently embraces Kizuna Ai",
        "wants to punch you",
        "watch star wars all day",
        "wants to run for president of the U.S.",
        "sings anime OST lyrics all day",
        "is secretly a bieber admirer",
        "was responsible for the death of kim jong",
        "was a product of Sasuke and Naruto doujins",
        "is actually Hideo Kojima in disguise",
        "likes to watch 50 shades of grey",
        "wants to watch animu",
        "met abraham lincoln just before his assassination",
        "assassinated abraham lincoln",
        "killed Curious George with a lawn mower",
        "stole everyone's meme",
        "stole christmas",
        "was made from sugar, spice and everything nice",
        "is secretly a big fan of mlp",
        "loves Kizuna Ai and wants to marry her",
        "exorcises demons in problematic girls",
        "has a crush on a girl cursed by a crab god",
        "is secretly a succubus",
        "secretly washes your dishes at night",
        "can transform into a white cat human to relieve stress",
        "wants to get in bed with Koyomi onii-chan",
        "is about to have a good toothbrushing session",
        "katy perry likes listening to",
        "roasts your harem for no reason",
        "searches through your room for ero magazines",
        "has a fear of men with mustache",
        "will eventually destroy the universe with fart",
        "eats big bazuso in hunger",
        "watches Oreimo season 2 repititively",
        "slaps you all the time but lowkey loves you",
        "was cursed by a snake god",
        "turned into a snake god to kill the fam",
        "follows trump into loli heaven",
        "ate your homework and your dog",
        "wants to capture your loli asap",
        "will guide you to Inori's backyard",
        "won't stop licking you",
        "dresses up as a magical girl",
        "cosplays boku no pico all day",
        "wants to take over korea",
        "listens to too much kpop",
        "smuggles yu-gi-oh cards through borders",
        "is trying to build a hugeeeee wall",
        "wants to eat chairo for breakfast",
        "supports abolishment of pokeman slavery",
        "wants to hunt endangered lolis",
        "is creating a weapon of mass destruction",
        "was once Araragi's math partner",
        "reads manga in the bathroom",
        "has a crush on their shut-in sister",
        "listens to renai circulation all day",
        "is platinum mad",
        "dresses up as their waifu",
        "uses fidget spinners as beyblades",
        "fuses their daughter with pet dog",
        "is secretly your child",
        "enjoys making memes",
        "show love to your body pillow",
        "might be a 600 year old loli vampire",
        "is responsible for global warming",
        "thinks the world is round",
        "thinks the world  is flat",
        "has many husbandos",
        "collects anime figures",
        "will eventually date Senjougahara",
        "will become the president of North Korea",
        "will destroy this discord server with the power of lewd",
        "is actually a demon butler that wants to eat your soul",
        "trapped in a virtual reality death game",
        "has a harem in a VR game"
        ]

    
    
serverConfig = dict()
description = "memes"

#configure bot/prefix
bot = commands.Bot(command_prefix='porn!', description=description)
default_prefix = '-'

values = {"PLEB": {"am": 3, "cost": 160}, "AKINO": {"am": 2, "cost": 100}, "MEEMO": {"am": 1, "cost": 65}, "INORI": {"am": 4, "cost": 90},
          "SHINOBU": {"am": 5, "cost": 70}, "HARAMBE": {"am": 9, "cost": 188}, "JEFF": {"am": 8, "cost": 151},
          "PEPE": {"am": 15, "cost": 260}, "FAKE_TAXI": {"am": 11, "cost": 218}, "KIZUNA_AI": {"am": 80, "cost": 3400}}



@bot.command()
async def leave(ctx, *person):
    if str(ctx.message.author.id) == "197696131285647360":
        await ctx.send("goodbye")
        await bot.logout()
        await bot.close()
        sys.exit()

@bot.command()
async def e(ctx, *args):
    if str(ctx.message.author.id) == "197696131285647360":
        try:
            proc = " ".join(args)
            ret = eval(proc)
            await ctx.send(str(ret))
        except Exception as e:
            await ctx.send(str(e))
    else:
        await ctx.send(":^ ) wat")

@bot.command(pass_context = True)
async def stats(ctx):
    author = str(ctx.message.author.id)
    name = str(ctx.message.author)
    if author in users:
        level = users[author]["level"]
        tonxtlvl = users[author]["reqmp"]
        inventory = users[author]["inventory"]
        instring = ""
        for x in inventory:
            instring = instring + " " + x + "(*" + str(inventory[x]) + "*)"
        mp = users[author]["mp"]
        if mp >= 1000000000000:
            mp_format = '{:.4e}'.format(mp)
        else:
            mp_format = '{:,}'.format(mp)
        if tonxtlvl >= 1000000000000:
            tonxtlvl_format = '{:.4e}'.format(tonxtlvl)
        else:
            tonxtlvl_format = '{:,}'.format(tonxtlvl)
        generation = 0
        for y in inventory:
            generation = generation + (users[author]["inventory"][y] * users[author]["val"][y]["am"])
        if generation >= 1000000000000:
            generation = '{:.4e}'.format(generation)
        else:
            generation = '{:,}'.format(generation)
        await ctx.send("Yahallo **" + name + "** **LEVEL**: " + str(int(level)) + " | **Net Worth**: :lollipop: **" +
                      str(mp_format) + "** | **To Next LEVEL**: " + str(tonxtlvl_format) + "\nGeneration per 25 seconds: **"+str(generation)+ "** :chart_with_upwards_trend:\n**:arrow_up: Active Items**:" + instring)
    else:
        await ctx.send("You have to register to my database first with *'`register'*")

@bot.command()
async def me(ctx):
    author = str(ctx.message.author)
    n = random.choice(noun)
    n_list = list(n)
    n_t = [":regional_indicator_"+i.lower()+":" if i != "-" else i for i in n_list]
    await ctx.send("**"+author + "** is a " + " ".join(n_t))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def echo(ctx, *m: str):
    await ctx.guild.system_channel.send(" ".join(m))


@bot.command()
async def test(ctx):
    if str(ctx.message.author.id) == "444462879769493536":
        await ctx.send("hi owner :3")
    else:
        await ctx.send("zzzzz")

#non-command push event processing
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #update presence
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,
                                                    name = "with Rilaaa",
                                                    state = "Sleeping",
                                                    details = "Competitive",
                                                    party = {"id":"ae488379-351d-4a4f-ad32-2b9b01c91657",
                                                             "size":[1,1]},
                                                    assets = {"large_image":"choco",
                                                              "large_text":"zzzz",
                                                              "small_image":"chocobig",
                                                              "small_text":"let me sleep"}
                                                    ))
    
#secret token (never push to pornhub **github)
choco_token = "token here"

bot.run(choco_token)
