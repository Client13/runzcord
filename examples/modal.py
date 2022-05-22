import asyncio

import runzcord
from runzcord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)


class MyModal(runzcord.ui.Modal):
    def __init__(self) -> None:
        components = [
            runzcord.ui.TextInput(
                label="Name",
                placeholder="The name of the tag",
                custom_id="name",
                style=runzcord.TextInputStyle.short,
                max_length=50,
            ),
            runzcord.ui.TextInput(
                label="Description",
                placeholder="The description of the tag",
                custom_id="description",
                style=runzcord.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
            runzcord.ui.TextInput(
                label="Content",
                placeholder="The content of the tag",
                custom_id="content",
                style=runzcord.TextInputStyle.paragraph,
                min_length=5,
                max_length=1024,
            ),
        ]
        super().__init__(title="Create Tag", custom_id="create_tag", components=components)

    async def callback(self, inter: runzcord.ModalInteraction) -> None:
        embed = runzcord.Embed(title="Tag Creation")
        for key, value in inter.text_values.items():
            embed.add_field(name=key.capitalize(), value=value, inline=False)
        await inter.response.send_message(embed=embed)

    async def on_error(self, error: Exception, inter: runzcord.ModalInteraction) -> None:
        await inter.response.send_message("Oops, something went wrong.", ephemeral=True)


@bot.slash_command()
async def create_tag(inter: runzcord.CommandInteraction):
    # Sends a modal using a high level implementation.
    await inter.response.send_modal(modal=MyModal())


@bot.slash_command()
async def create_tag_low(inter: runzcord.CommandInteraction):
    # Works same as the above code but using a low level interface.
    # It's recommended to use this if you don't want to increase cache usage.
    await inter.response.send_modal(
        title="Create Tag",
        custom_id="create_tag_low",
        components=[
            runzcord.ui.TextInput(
                label="Name",
                placeholder="The name of the tag",
                custom_id="name",
                style=runzcord.TextInputStyle.short,
                max_length=50,
            ),
            runzcord.ui.TextInput(
                label="Description",
                placeholder="The description of the tag",
                custom_id="description",
                style=runzcord.TextInputStyle.short,
                min_length=5,
                max_length=50,
            ),
            runzcord.ui.TextInput(
                label="Content",
                placeholder="The content of the tag",
                custom_id="content",
                style=runzcord.TextInputStyle.paragraph,
                min_length=5,
                max_length=1024,
            ),
        ],
    )

    # Waits until the user submits the modal.
    try:
        modal_inter: runzcord.ModalInteraction = await bot.wait_for(
            "modal_submit",
            check=lambda i: i.custom_id == "create_tag_low" and i.author.id == inter.author.id,
            timeout=300,
        )
    except asyncio.TimeoutError:
        # The user didn't submit the modal in the specified period of time.
        # This is done since Discord doesn't dispatch any event for when a modal is closed/dismissed.
        return

    embed = runzcord.Embed(title="Tag Creation")
    for custom_id, value in modal_inter.text_values.items():
        embed.add_field(name=custom_id.capitalize(), value=value, inline=False)
    await modal_inter.response.send_message(embed=embed)


bot.run("token")
