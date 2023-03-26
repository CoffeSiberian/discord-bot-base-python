# **discord-bot-base-python**
The source code you see here is just an example of use to start programming a larger system.

###### For correct operation I recommend using a virtual environment
```bash
python3 -m venv dc-venv
```

------------


###### To activate the virtual environment
Linux - Mac
```bash
source dc-venv/bin/activate
```
Windows
```bash
dc-venv\Scripts\activate
```

------------


###### Upgrade pip
```bash
pip install --upgrade pip
```

------------


###### After having the virtual environment activated, it is necessary to install the dependencies

Using requirements.txt
```bash
pip install -r requirements.txt
```
Direct installation from pypi *(recommended)*
```bash
pip install discord.py PyNaCl pydantic
```

------------
###### Once the dependencies are installed, you need to edit settings.json>bot_token with your bot token
```json
{
    "bot_token":"your_discord_bot_token",
    ....
}
```

------------

###### And now you can run the bot using the following command with the virtual environment enabled
```bash
python3 main.py
```

------------

**Now you are free to use the bot, I remind you that all the official documentation of the discord.py library can be found at: https://discordpy.readthedocs.io/en/stable**