import discord
from discord import app_commands

class AdmCommands(app_commands.Group):
    def __init__(self, *, name: str = 'test grup', description: str = 'test'):
        super().__init__(name=name, description=description)

    @app_commands.command(name='hello', description='Hello World!')
    #@app_commands.check(getPermission)
    @discord.app_commands.checks.cooldown(rate=1, per=12)
    @app_commands.describe(name='User to whom the hello world will be sent')
    async def hello(self, interaction: discord.Interaction, name: discord.Member):
        await interaction.response.send_message(f'Hello {name.mention}!')

    async def on_error(self, interaction: discord.Interaction, error):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(
                f'{interaction.user.mention} el comando lo podras usar dentro de: {int(error.retry_after)} segundos', 
                ephemeral=True)