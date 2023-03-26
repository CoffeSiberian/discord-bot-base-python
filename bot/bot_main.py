from discord.ext import commands
import discord

# Slach Commands

class Bot(commands.Bot):
    
    def __init__(self, command_prefix):
        self.prefix = command_prefix
        commands.Bot.__init__(self, command_prefix=command_prefix, intents=discord.Intents.all())
    
    # To keep listening for buttons
    async def setup_hook(self):
        #self.add_view(view())
        pass

    # Startup Information
    async def on_ready(self):
        print(f'Connected to bot: {self.user.name}')
        await self.change_presence(
            activity=discord.Activity(
            type=discord.ActivityType.listening, name=f'github.com/CoffeSiberian'))
        await self.adds()
        
    async def adds(self):
        # remove help
        self.remove_command('help')

        # slach commands

        await self.tree.sync()