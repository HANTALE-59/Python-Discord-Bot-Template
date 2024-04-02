import discord
from discord.ext import commands
from discord.ext.commands import Context
from typing import Literal
from assets.data import Data


class Minecraft(commands.Cog, name="minecraft"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_group(
        name="minecraft",
        description="Manage the minecraft news on your server.",
    )
    @commands.has_permissions(manage_messages=True)
    async def minecraft(self, context: Context) -> None:
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                description="Please specify a subcommand.\n\n**Subcommands:**\n`snapshot` - Adds a snapshot newsletter to the servers",
                color=0xE02B2B)
            await context.send(embed=embed)

    @minecraft.command(
        name="snapshot",
        description="Adds a snapshot newsletter to the servers")
    @commands.has_permissions(manage_messages=True)
    async def snapshot(self, ctx, edition:Literal['Java','Bedrock','Both'],channel:discord.TextChannel) -> None:
        if channel is None:
            await ctx.send("Insufficient Arguments")
        else:
            if str(ctx.guild.id) not in Data.server_data:
                Data.server_data[str(ctx.guild.id)] = Data.create_new_data()

            if edition == 'Java':

                Data.server_data[str(ctx.guild.id)]["snapshot_java"].append(str(channel.id))
                await ctx.send(f"Added {channel.mention} to the java snapshot newsletter")            
            
            elif edition == 'Bedrock':

                Data.server_data[str(ctx.guild.id)]["snapshot_bedrock"].append(str(channel.id))
                await ctx.send(f"Added {channel.mention} to the bedrock snapshot newsletter")
            
            elif edition == 'Both':
                Data.server_data[str(ctx.guild.id)]["snapshot_bedrock"].append(str(channel.id))
                Data.server_data[str(ctx.guild.id)]["snapshot_java"].append(str(channel.id))
                await ctx.send(f"Added {channel.mention} to the java and bedrock snapshot newsletter")
            

            
            # Call auto_update_data to save changes to data.json
            await Data.auto_update_data()


async def setup(bot) -> None:
    await bot.add_cog(Minecraft(bot))
