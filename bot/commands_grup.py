import discord
from discord import app_commands

def getPermission(interaction: discord.Interaction) -> bool:
    return interaction.permissions.manage_guild

def getNSFW(interaction: discord.Interaction) -> bool:
    return interaction.channel.is_nsfw()

class TestCommands(app_commands.Group):
    def __init__(self, *, name: str = 'test grup', description: str = 'test'):
        # NSFW not working in commands group
        # If you need to check an NSFW channel use the getNSFW function with the @app_commands.check decorator
        super().__init__(name=name, description=description, guild_only=True, nsfw=False)

    @app_commands.command(name='hello', description='Hello World!')
    @app_commands.check(getPermission)
    @discord.app_commands.checks.cooldown(rate=1, per=10)
    @app_commands.describe(name='User to whom the hello world will be sent')
    async def hello(self, interaction: discord.Interaction, name: discord.Member) -> None:
        await interaction.response.send_message(f'Hello {name.mention}!')

    @app_commands.command(name='nsfw', description='nsfw command')
    @app_commands.check(getNSFW)
    @app_commands.describe(name='User to whom the hello world will be sent')
    async def hello(self, interaction: discord.Interaction, name: discord.Member) -> None:
        await interaction.response.send_message(f'Hello {name.mention}!')

    async def on_error(self, interaction: discord.Interaction, error) -> None:
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f'You have to wait {int(error.retry_after)} seconds to use the command again {interaction.user.mention}', 
                ephemeral=True)