import discord
from logging import getLogger
from discord import app_commands

def getPermission(interaction: discord.Interaction) -> bool:
    return interaction.permissions.manage_guild

def getNSFW(interaction: discord.Interaction) -> bool:
    return interaction.channel.nsfw

async def getLetter(interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return [ app_commands.Choice(name=r, value=r) for r in type if current.lower() in r.lower() ]

class TestCommands(app_commands.Group):
    def __init__(self, *, name: str = 'test_grup', description: str = 'test'):
        # NSFW not working in commands group
        # If you need to check an NSFW channel use the getNSFW function with the @app_commands.check decorator
        super().__init__(name=name, description=description, guild_only=True, nsfw=False)
        self.loggin_discord = getLogger('discord')

    @app_commands.command(name='hello', description='Hello World!')
    @app_commands.check(getPermission)
    @discord.app_commands.checks.cooldown(rate=1, per=10)
    @app_commands.describe(name='User to whom the hello world will be sent')
    async def getHello(self, interaction: discord.Interaction, name: discord.Member) -> None:
        await interaction.response.send_message(f'Hello {name.mention}!')

    @app_commands.command(name='nsfw', description='nsfw command')
    @app_commands.check(getNSFW)
    @app_commands.describe(msj='test message')
    async def getNsfw(self, interaction: discord.Interaction, msj: str) -> None:
        await interaction.response.send_message(f'NSFW message: {msj}')

    @app_commands.command(name='letters', description='select a letter of the alphabet')
    @app_commands.describe(letter='select a letter')
    @app_commands.autocomplete(letter=getLetter)
    async def getLetters(self, interaction: discord.Interaction, letter: str) -> None:
        '''
        Commands with autocompletion are useful for searching and selecting values.
        '''
        await interaction.response.send_message(f'You selected the letter: {letter}')

    async def on_error(self, interaction: discord.Interaction, error) -> None:
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f'You have to wait {int(error.retry_after)} seconds to use the command again {interaction.user.mention}', 
                ephemeral=True)
        if isinstance(error, discord.app_commands.CheckFailure):
            await interaction.response.send_message(
                f'You do not have permission to use this command {interaction.user.mention}', 
                ephemeral=True)
        self.loggin_discord.error(error)