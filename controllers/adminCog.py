import asyncio
import os

import discord
from discord.ext import commands
from discord import app_commands
from utils.log import get_logger

log = get_logger("bot")
OWNERS = os.getenv("OWNERS", None).split(",")

async def setup(bot):
    await bot.add_cog(AdminCog(bot))


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="createuser",
                          description="[ADMIN] Créer un utilisateur")
    @app_commands.describe(member="utilisateur discord")
    @app_commands.describe(x="coordonné X du spawn du joueur")
    @app_commands.describe(y="coordonné Y du spawn du joueur")
    async def addUser(self,
                      interaction: discord.Interaction,
                      member: discord.Member,
                      x: int = None,
                      y: int = None):
        if interaction.user.id not in OWNERS:
            return await interaction.response.send_message("You are not the owner of the bot", ephemeral=True)

        await interaction.response.send_message(
            f"Utilisateur {member} en cours de création...", ephemeral=True)

        # init de la planet
        if x is None or y is None:
            planet = foundPlanet(member.id)
        else:
            planet = foundPlanet(member.id, x, y)

        # init user
        User.initNewUser(User(member.id), planet)

        originalMsg = await interaction.original_response()
        await originalMsg.edit(
            content=f"Utilisateur {member} crée avec succès!")

    @app_commands.command(name="testbot",
                          description="[ADMIN] test du bot")
    @app_commands.describe(member="utilisateur discord")
    async def testbot(self,
                      interaction: discord.Interaction,
                      member: discord.Member):
        if interaction.user.id not in OWNERS:
            return await interaction.response.send_message("You are not the owner of the bot", ephemeral=True)

        await interaction.response.send_message(
            f"testing ...", ephemeral=True)

        originalMsg = await interaction.original_response()
        await originalMsg.edit(
            content=f"Utilisateur {member} crée avec succès!")