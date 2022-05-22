from typing import List

import runzcord
from runzcord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned)

# Defines a simple paginator of buttons for the embed.
class Menu(runzcord.ui.View):
    def __init__(self, embeds: List[runzcord.Embed]):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.embed_count = 0

        self.first_page.disabled = True
        self.prev_page.disabled = True

        # Sets the footer of the embeds with their respective page numbers.
        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Page {i + 1} of {len(self.embeds)}")

    @runzcord.ui.button(emoji="⏪", style=runzcord.ButtonStyle.blurple)
    async def first_page(self, button: runzcord.ui.Button, interaction: runzcord.MessageInteraction):
        self.embed_count = 0
        embed = self.embeds[self.embed_count]
        embed.set_footer(text=f"Page 1 of {len(self.embeds)}")

        self.first_page.disabled = True
        self.prev_page.disabled = True
        self.next_page.disabled = False
        self.last_page.disabled = False
        await interaction.response.edit_message(embed=embed, view=self)

    @runzcord.ui.button(emoji="◀", style=runzcord.ButtonStyle.secondary)
    async def prev_page(self, button: runzcord.ui.Button, interaction: runzcord.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False
        self.last_page.disabled = False
        if self.embed_count == 0:
            self.first_page.disabled = True
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @runzcord.ui.button(emoji="❌", style=runzcord.ButtonStyle.red)
    async def remove(self, button: runzcord.ui.Button, interaction: runzcord.MessageInteraction):
        await interaction.response.edit_message(view=None)

    @runzcord.ui.button(emoji="▶", style=runzcord.ButtonStyle.secondary)
    async def next_page(self, button: runzcord.ui.Button, interaction: runzcord.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True
            self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)

    @runzcord.ui.button(emoji="⏩", style=runzcord.ButtonStyle.blurple)
    async def last_page(self, button: runzcord.ui.Button, interaction: runzcord.MessageInteraction):
        self.embed_count = len(self.embeds) - 1
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        self.next_page.disabled = True
        self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)


@bot.command()
async def paginator(ctx: commands.Context):

    # Creates the embeds as a list.
    embeds = [
        runzcord.Embed(
            title="Paginator example",
            description="This is the first embed.",
            colour=runzcord.Colour.random(),
        ),
        runzcord.Embed(
            title="Paginator example",
            description="This is the second embed.",
            colour=runzcord.Color.random(),
        ),
        runzcord.Embed(
            title="Paginator example",
            description="This is the third embed.",
            colour=runzcord.Color.random(),
        ),
    ]

    # Sends first embed with the buttons, it also passes the embeds list into the View class.
    await ctx.send(embed=embeds[0], view=Menu(embeds))


bot.run("token")
