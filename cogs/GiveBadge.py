import discord 
from discord import app_commands as commands
from discord.ext import commands
from discord.ext.commands import Context
from typing import Literal


# Here we name the cog and create a new class for the cog.
class Givebadge(commands.Cog, name="givebadge"):
    def __init__(self, bot) -> None:
        self.bot = bot

    
    @commands.hybrid_command(name="give_badge", description="Create 102 disable automods, wait 12h to get the badge")
    @commands.describe(create_servers="if True it will create 12 servers, if False the automod will be create in the actual servers ")
    async def give_badge(self, ctx: Context,create_servers:Literal['True','False']):
        await ctx.defer()
        count = 0  
        if create_servers == 'False':
            guilds = self.bot.guilds
            for guild in guilds:
                if count>100:
                    embed = discord.Embed(title="Finish 🥇 !", description=" You created {count} disabled Automod rules, wait 12h to get it.\nDon't delete its or you'll loose rhe badge :( ")
                    await ctx.send(embed=embed)
                    return
                bot = guild.get_member(self.bot.user.id)
                if not bot.guild_permissions.manage_guild:
                	continue
                actions = [discord.AutoModRuleAction(custom_message="Yo got EZ be automod lmao, big NIGGAAA")]
                try:  #mention spam filter
                    name = "Givebadge | type : mention spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.mention_spam)
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by FistashkinBot"
                )
    
                    print(f"Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    count=count+1
                except Exception as e:
                    print(f"error: {e}")
    #-------------------------SPAM FILTER----------------------------
                try:  # spam filter
                    name = "Givebadge | type : spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.spam)
                    actions = actions
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by NIGGGGAAAAAAA",
                )
                
                    count = count+1
                    print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    
                except Exception as e:
                    print(f"error: {e}")
    
    #-------------------------keyword_preset----------------------------
                try:  # spam filter
                    name = "Givebadge | type : spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.keyword_preset)
                    actions = actions
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by Nigga!!!",
                )
                
                    count = count+1
                    print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    
                except Exception as e:
                    print(f"error: {e}")
    
    #-------------------------ban words----------------------------
              
                i = 0
                while i < 6:
                    i = i + 1
                    try:
                        name = "Givebadge | type : ban word"
                        event_type = discord.AutoModRuleEventType.message_send
                        trigger = discord.AutoModTrigger(type=discord.AutoModRuleTriggerType.keyword)
                        actions = actions
        
                        automod_rule = await guild.create_automod_rule(
                        name=name,
                        event_type=event_type,
                        trigger=trigger,
                        actions=actions,
                        enabled=False,
                        exempt_roles=[],
                        exempt_channels=[],
                        reason="Automod by NIGGAAA",
                    )
                        count = count + 1 
                        print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    except Exception as e:
                        print(f"error: {e}")


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        
        else:
            while count < 101:
                guild = await create_guild(code='https://discord.new/jKVvPBBCfjEZ')
                bot = guild.get_member(self.bot.user.id)
                if not bot.guild_permissions.manage_guild:
                	continue
                actions = [discord.AutoModRuleAction(custom_message="Yo got EZ be automod lmao, big NIGGAAA")]
                try:  #mention spam filter
                    name = "Givebadge | type : mention spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.mention_spam)
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by FistashkinBot"
                )
    
                    print(f"Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    count=count+1
                except Exception as e:
                    print(f"error: {e}")
    #-------------------------SPAM FILTER----------------------------
                try:  # spam filter
                    name = "Givebadge | type : spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.spam)
                    actions = actions
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by NIGGGGAAAAAAA",
                )
                
                    count = count+1
                    print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    
                except Exception as e:
                    print(f"error: {e}")
    
    #-------------------------keyword_preset----------------------------
                try:  # spam filter
                    name = "Givebadge | type : spam filter"
                    event_type = discord.AutoModRuleEventType.message_send
                    trigger = discord.AutoModTrigger(type = discord.AutoModRuleTriggerType.keyword_preset)
                    actions = actions
    
                    automod_rule = await guild.create_automod_rule(
                    name=name,
                    event_type=event_type,
                    trigger=trigger,
                    actions=actions,
                    enabled=False,
                    exempt_roles=[],
                    exempt_channels=[],
                    reason="Automod by Nigga!!!",
                )
                
                    count = count+1
                    print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    
                except Exception as e:
                    print(f"error: {e}")
    
    #-------------------------ban words----------------------------
              
                i = 0
                while i < 6:
                    i = i + 1
                    try:
                        name = "Givebadge | type : ban word"
                        event_type = discord.AutoModRuleEventType.message_send
                        trigger = discord.AutoModTrigger(type=discord.AutoModRuleTriggerType.keyword)
                        actions = actions
        
                        automod_rule = await guild.create_automod_rule(
                        name=name,
                        event_type=event_type,
                        trigger=trigger,
                        actions=actions,
                        enabled=False,
                        exempt_roles=[],
                        exempt_channels=[],
                        reason="Automod by NIGGAAA",
                    )
                        count = count + 1 
                        print(f"{count} Automod rule '{automod_rule.name}' on server {guild.name} succesfully created!")
                    except Exception as e:
                        print(f"error: {e}")
            embed = discord.Embed(title="Finish 🥇 !", description=" You created {count} disabled Automod rules, wait 12h to get it.\nDon't delete its or you'll loose rhe badge :( ")
            await ctx.send(embed=embed)
        
                
                
           
            
                
async def setup(bot) -> None:
    await bot.add_cog(Givebadge(bot))
