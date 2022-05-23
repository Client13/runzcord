[![Runz Banner](https://raw.githubusercontent.com/Venomrunz/runz/master/assets/banner.png)](https://runz.dev/)

RunzCord
=======

<p align="center">
    <a href="https://discord.gg/runz"><img src="https://img.shields.io/discord/808030843078836254?style=flat-square&color=5865f2&logo=discord&logoColor=ffffff&label=discord" alt="Discord server invite" /></a>
    
</p>

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.Inspired From Disnake.

Key Features
------------

- Proper rate limit handling.
- Type-safety measures.
- [FastAPI](https://fastapi.tiangolo.com/)-like slash command syntax.

<sup>The syntax and structure of `discord.py 2.0` is preserved.</sup>

Installing
----------

**Python 3.8 or higher is required.**
**NOTE: This package is not released globally , So U need to install using the command :- ```pip install git+https://github.com/Client13/runzcord```
To install the library without full voice support, you can just run the
following command:

``` sh
# Linux/macOS
python3 -m pip install -U runzcord

# Windows
py -3 -m pip install -U runzcord
```

Installing `runzcord` with full voice support requires you to replace `runzcord` here, with `runzcord[voice]`.

(You can optionally install [PyNaCl](https://pypi.org/project/PyNaCl/) for voice support.)

Note that voice support on Linux requires installation of `libffi-dev` and `python-dev` packages, via your preferred package manager (e.g. `apt`, `dnf`, etc.) before running the following commands.

Versioning
----------
CURRENT VERSION 2.0.0.

To be on the safe side and avoid unexpected breaking changes, pin the dependency to a minor version (e.g. `runzcord==a.b.*` or `runzcord~=a.b.c`) or an exact version (e.g. `runzcord==a.b.c`).

Quick Example
-------------

### Slash Commands Example

``` py
import runzcord
from runzcord.ext import commands

bot = commands.InteractionBot(test_guilds=[12345])

@bot.slash_command()
async def ping(inter):
    await inter.response.send_message("Pong!")

bot.run("BOT_TOKEN")
```

### Context Menus Example

``` py
import runzcord
from runzcord.ext import commands

bot = commands.InteractionBot(test_guilds=[12345])

@bot.user_command()
async def avatar(inter, user):
    embed = runzcord.Embed(title=str(user))
    embed.set_image(url=user.display_avatar.url)
    await inter.response.send_message(embed=embed)

bot.run("BOT_TOKEN")
```

### Prefix Commands Example

``` py
import runzcord
from runzcord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run("BOT_TOKEN")
```



<br>
Untill The Docs Are Released , Docs Of Disnake May Be Followed.
======
<p align="center">
    <a href="https://docs.disnake.dev/">Documentation</a>
    ⁕
    <a href="https://guide.disnake.dev/">Guide</a>
    ⁕
    <a href="https://discord.gg/runz">Discord Server</a>
    ⁕
    <a href="https://discord.gg/discord-developers">Discord Developers</a>
</p>
<br>
