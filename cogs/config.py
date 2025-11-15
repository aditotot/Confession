# This is cogs/config.py
import discord
from discord.ext import commands
from discord import app_commands
import database as db

class Config(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="config", description="Set the confessions channel")
    @app_commands.describe(channel="The channel where confessions will be sent")
    @app_commands.default_permissions(manage_guild=True) # Only admins
    async def config(self, interaction: discord.Interaction, channel: discord.TextChannel):
        
        await interaction.response.defer(ephemeral=True)
        
        try:
            # Add 'await' back
            await db.set_confession_channel(self.bot.db, interaction.guild.id, channel.id)
            
            await interaction.followup.send(
                f"✅ Confessions channel has been set to {channel.mention}"
            )
            
        except Exception as e:
            print(f"[DEBUG /config] AN ERROR OCCURRED: {e}")
            await interaction.followup.send(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Config(bot))