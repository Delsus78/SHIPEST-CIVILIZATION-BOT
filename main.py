import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.log import get_logger

load_dotenv()
log = get_logger("main")

# env variable
BOT_TOKEN = os.getenv("BOT_TOKEN", None)

if not BOT_TOKEN:
    message = (
        "Couldn't find the `BOT_TOKEN` environment variable. "
        "Make sure to add it to your `.env` file like this: `BOT_TOKEN=value_of_your_bot_token`"
    )
    log.warning(message)
    raise ValueError(message)


intents = discord.Intents.all()

client = commands.Bot(command_prefix='Î',
                      intents=intents,
                      allowed_mentions=discord.AllowedMentions(everyone=False))

@client.event
async def on_ready():
    log.debug(f'We have logged in as {client.user}')
    try:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="/start"))
        synced = await client.tree.sync()
        log.debug(f"Synced {len(synced)} commandes.")

        log.debug("Bot started.")
    except Exception as e:
        log.debug(e)
        await client.close()
@client.event
async def setup_hook():
    await client.load_extension("controllers.adminCog")

client.run(BOT_TOKEN)
