import discord
from discord.ext import commands

happy = commands.Bot(command_prefix= '.')

happy.event
async def on_read():
    print("Happy is ready")

happy.event
async def on_member_join(member):
    print(f'{member} Welcome to the server.')

happy.event
async def on_member_remove(member):
    print(f'{member} Left from the server.')
    
happy.command()
async def hi(ctx):
    await ctx.send('Hey')

happy.command(aliases = ['Hello','Hey','Hi','hey','hello'])
async def _Hi(ctx):
    await ctx.send('Hey')

happy.run('Njk2MDA4NzY5NjExNDk3NDcy.Xoie2A.xC-tqG52q1ugm8TcHoMNGbBPR4A')