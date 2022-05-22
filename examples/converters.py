# This example requires the 'members' privileged intent to use the Member converter.

import typing

import runzcord
from runzcord.ext import commands

intents = runzcord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(commands.when_mentioned_or("!"), intents=intents)


@bot.command()
async def userinfo(ctx: commands.Context, user: runzcord.User):
    # In the command signature above, you can see that the `user`
    # parameter is typehinted to `runzcord.User`. This means that
    # during command invocation we will attempt to convert
    # the value passed as `user` to a `runzcord.User` instance.
    # The documentation notes what can be converted, in the case of `runzcord.User`
    # you pass an ID, mention or username (discrim optional)
    # E.g. 80088516616269824, @Danny or Danny#0007

    # NOTE: typehinting acts as a converter within the `commands` framework only.
    # In standard Python, it is use for documentation and IDE assistance purposes.

    # If the conversion is successful, we will have a `runzcord.User` instance
    # and can do the following:
    user_id = user.id
    username = user.name
    avatar = user.display_avatar.url
    await ctx.send(f"User found: {user_id} -- {username}\n{avatar}")


@userinfo.error
async def userinfo_error(ctx: commands.Context, error: commands.CommandError):
    # if the conversion above fails for any reason, it will raise `commands.BadArgument`
    # so we handle this in this error handler:
    if isinstance(error, commands.BadArgument):
        return await ctx.send("Couldn't find that user.")


@bot.command()
async def ignore(ctx: commands.Context, target: typing.Union[runzcord.Member, runzcord.TextChannel]):
    # This command signature utilises the `typing.Union` typehint.
    # The `commands` framework attempts a conversion of each type in this Union *in order*.
    # So, it will attempt to convert whatever is passed to `target` to a `runzcord.Member` instance.
    # If that fails, it will attempt to convert it to a `runzcord.TextChannel` instance.
    # See: https://docs.runzcord.dev/en/latest/ext/commands/commands.html#typing-union
    # NOTE: If a Union typehint converter fails it will raise `commands.BadUnionArgument`
    # instead of `commands.BadArgument`.

    # To check the resulting type, `isinstance` is used
    if isinstance(target, runzcord.Member):
        await ctx.send(f"Member found: {target.mention}, adding them to the ignore list.")
    elif isinstance(
        target, runzcord.TextChannel
    ):  # this could be an `else` but for completeness' sake.
        await ctx.send(f"Channel found: {target.mention}, adding it to the ignore list.")


# Built-in type converters.
@bot.command()
async def multiply(ctx: commands.Context, number: int, maybe: bool):
    # We want an `int` and a `bool` parameter here.
    # `bool` is a slightly special case, as shown here:
    # See: https://docs.runzcord.dev/en/latest/ext/commands/commands.html#bool

    if maybe is True:
        return await ctx.send(number * 2)
    await ctx.send(number * 5)


bot.run("token")
