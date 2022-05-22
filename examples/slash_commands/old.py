"""
An example of old-style options.
Not the most convenient syntax.
"""
import runzcord
from runzcord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)


@bot.slash_command(
    name="slash_command",
    description="A Simple Slash Command",
    options=[
        runzcord.Option("string", description="A string to send", required=True),
        runzcord.Option(
            "channel", description="The destination channel", type=runzcord.OptionType.channel
        ),
        runzcord.Option(
            "number", description="The number of repetitions", type=runzcord.OptionType.integer
        ),
    ],
)
async def command(inter, string, channel=None, number=1):
    channel = channel or inter.channel
    await inter.response.send_message(
        f"Sending {string} {number}x to {channel.mention}", ephemeral=True
    )
    await channel.send(string * number)
