import asyncio

import discord
from discord.ext import commands
from discord import app_commands

from utils.constants import Colours
from utils.log import get_logger

log = get_logger("bot")


async def setup(bot):
    await bot.add_cog(BaseCog(bot))


class BaseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help",
                          description="Affiche l'aide du bot")
    async def help(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"", ephemeral=True)

        # affichage de l'aide
        try:
            with open('resources/help.md', 'r') as file:
                help_text = file.read()
        except FileNotFoundError:
            log.error("help file not found")

        originalMsg = await interaction.original_response()
        await originalMsg.edit(embed=help_text, color=Colours.bright_green)
