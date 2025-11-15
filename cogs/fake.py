# This is cogs/fake.py
import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional

class Fake(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="appeal", description="Appeal a confession ban")
    @app_commands.default_permissions(manage_guild=True)
    async def appeal(self, interaction: discord.Interaction):
        await interaction.response.send_message("This command is not active.", ephemeral=True)

    @app_commands.command(name="checklogs", description="Check confession logs for a user")
    @app_commands.default_permissions(manage_guild=True)
    async def checklogs(self, interaction: discord.Interaction):
        await interaction.response.send_message("This command is not active.", ephemeral=True)
        
    @app_commands.command(name="confessban", description="Ban a user from confessing")
    @app_commands.describe(clear="[Fake option]")
    @app_commands.default_permissions(manage_guild=True)
    async def confessban(self, interaction: discord.Interaction, clear: Optional[bool] = None):
        await interaction.response.send_message("This command is not active.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Fake(bot))