from functions.get_settings import loadSettings
import functions.logs
from bot.bot_main import Bot

cfg = loadSettings()

bot = Bot(cfg)
bot.run(cfg.bot_token)