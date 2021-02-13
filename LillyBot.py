#!/usr/bin/env python3
import discord
from discord.ext import commands
from discord.role import Role

realCode = ''
channelName = ''
readTheRulesRole = 0
token = ''

description = '''A bot to gatekeep the permissions of a discord server.'''

bot = commands.Bot(command_prefix='_', description=description)

@bot.event
async def on_ready():
    print('Starting Lillybot')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='RuleCode', aliases=list(('rulecode', 'Rulecode', 'ruleCode')), description='Read the rules to figure out the rule code.')
async def rulecode(ctx, *code: str):
    if ctx.channel.name == channelName:
        if ctx.author.bot == False:
            if ctx.guild.get_role(readTheRulesRole) not in ctx.author.roles:
                testCode = ' '.join([str(x) for x in code])
                if testCode == realCode:
                    role = ctx.guild.get_role(readTheRulesRole)
                    await ctx.message.delete()
                    await ctx.channel.send('Thank you, {0}, for reading the rules!'.format(ctx.author.display_name), delete_after=10)
                    await ctx.author.add_roles(role, reason='{0} read the rules.'.format(ctx.author.display_name))
                elif testCode == '':
                    await ctx.message.delete()
                    await ctx.channel.send('You have to supply a code: `_RuleCode [code]`', delete_after=10)
                else:
                    await ctx.message.delete()
                    await ctx.channel.send('Sorry that was not the right code.', delete_after=10)
            else:
                await ctx.message.delete()
        else:
            await ctx.message.delete()
    else:
        await ctx.message.delete()

bot.run(token)
