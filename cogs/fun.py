""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""

import random

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context


class Choice(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.value = None

    @discord.ui.button(label="Heads", style=discord.ButtonStyle.blurple)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        self.value = "heads"
        self.stop()

    @discord.ui.button(label="Tails", style=discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction) -> None:
        self.value = "tails"
        self.stop()


class MagarcaneSelect(discord.ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(
                label="Découvre Magarcane", description="Un résumé te fera du bien", emoji="📑"),
            discord.SelectOption(
                label="Personnage", description="Besoin d'une info sur un personnage?", emoji="<:1:1217749947139751966>"),
            discord.SelectOption(
                label="Random fact", description="Petit fait croustillant?", emoji="🕵🏼"),
        ]
        super().__init__(
            placeholder="Choisis...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction) -> None:
        selected_option = self.values[0]  # Récupère la première (et seule) option sélectionnée
		bot = ctx.guild.get_member(self.bot.user.id)
		
        if selected_option == "Découvre Magarcane":
	    	embrep = discord.Embed(title=selected_option,description=resumeMagarcane,color=bot.color)
            await interaction.response.send_message("Option 1 choisis", ephemeral=True)
        elif selected_option == "Personnage":
			embrep = discord.Embed(title=selected_option,description=random.choice(liste_personnage))
            await interaction.response.send_message("Option 2 choisis", ephemeral=True)
        elif selected_option == "Random fact":
			embrep = discord.Embed(title=selected_option,description=random.choice(liste_anecdote))
            await interaction.response.send_message("Option 3 choisis", ephemeral=True)

		await ctx.send(embed=embrep)

class RockPaperScissorsView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__()
        self.add_item(RockPaperScissors())


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot) -> None:
        self.bot = bot


    @commands.hybrid_command(name="rps", description="Play the rock paper scissors game against the bot.")
    async def rock_paper_scissors(self, ctx: Context) -> None:
		bot = ctx.guild.get_member(self.bot.user.id)
        view = RockPaperScissorsView()
		embed = discord.Embed(title="Salut! Chevalier de Magarcane. Que veux tu apprendre aujourd'hui?",description="",color=bot.color)
        await ctx.send("Choisis une option", view=view)


async def setup(bot) -> None:
    await bot.add_cog(Fun(bot))
