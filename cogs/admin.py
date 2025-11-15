# This is cogs/admin.py
import discord
from discord.ext import commands
import database as db

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="count")
    @commands.has_permissions(manage_guild=True)
    async def set_count(self, ctx, number: int):
        """Sets the next confession number."""
        if number <= 0:
            return await ctx.send("Number must be positive.")
        
        # Add 'await' back
        await db.set_confession_index(self.bot.db, ctx.guild.id, number)
        await ctx.send(f"✅ The next confession index has been set to **{number}**.")

    @commands.command(name="guild")
    @commands.has_permissions(administrator=True) 
    async def set_guild_log(self, ctx, guild_id: int, channel_id: int):
        """Sets the target guild and channel for confession logs."""
        
        # Add 'await' back
        await db.set_log_channel(self.bot.db, ctx.guild.id, guild_id, channel_id)
        await ctx.send(f"✅ Confession logs will now be sent to channel `{channel_id}` in guild `{guild_id}`.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))