# This is main.py
import os
import discord
import motor.motor_asyncio  # Use the async library 'motor'
import asyncio
from discord.ext import commands

# --- Bot Setup ---
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

class ConfessionBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # --- Connect using 'motor' ---
        try:
            self.mongo_client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGO_URI'])
            self.db = self.mongo_client["confession_bot_db"]
            print("Successfully connected to MongoDB (async).")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            exit()
    
    async def setup_hook(self):
        print("Loading cogs...")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"Loaded cog: {filename}")
                except Exception as e:
                    print(f"Failed to load cog {filename}: {e}")
        
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        
        try:
            # Sync slash commands
            synced = await self.tree.sync() 
            print(f"Synced {len(synced)} slash commands.")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
            
        print('-----------------------------------------')

# Create the bot instance
bot = ConfessionBot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=intents,
    help_command=None
)

async def main():
    async with bot:
        await bot.start(os.environ['DISCORD_TOKEN'])

if __name__ == "__main__":
    asyncio.run(main())