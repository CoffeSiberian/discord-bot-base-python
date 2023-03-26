from discord.ext import commands
import discord
from functions.types.settings_types import Settings

# Slach Commands
from bot.commands_grup import TestCommands

class Bot(commands.Bot):
    
    def __init__(self, cfg: Settings):
        # command_prefix is only used to get the bot running, all commands must be slach /
        self.__cfg = cfg
        commands.Bot.__init__(self, command_prefix='/*', intents=discord.Intents.all())
    
    # To keep listening for buttons
    async def setup_hook(self):
        #self.add_view(view())
        pass

    # Startup Information
    async def on_ready(self):
        print(f'Connected to bot: {self.user.name}')
        await self.change_presence(
            activity=discord.Activity(
            type=discord.ActivityType.listening, name=self.__cfg.github))
        await self.adds()
        
    async def adds(self):
        # remove help
        self.remove_command('help')

        # slach commands

        await self.tree.sync()