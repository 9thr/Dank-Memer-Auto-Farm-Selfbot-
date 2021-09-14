import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import json
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "$$"

#use the .env feature to hide your token

keep_alive()
with open("TOKEN.json") as f:
    config = json.load(f)
    token = config.get("TOKEN")
#---------------#

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Dank Memer Selfbot || Credits: thr#8159", color=1111, description=f"**{prefix}autodank**\nSends various messages to exploit/autofarm Dank Memers currency.\n\n**{prefix}stopautodank**\nStops the Selfbot for Dank Memer.")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/800567178579017779/887176699719065610/w97hcmd1yyv61.png")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autodank(ctx):
	await ctx.message.delete()
	await ctx.send('Dank Memer Selfbot is now **ENABLED**. (Cool down every 69 seconds.) ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://cdn.discordapp.com/attachments/800567178579017779/887185338475360301/depositphotos_85197786-stock-photo-young-man-with-thums-up.png')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(5)
			await ctx.send('pls beg')
			print(f"{Fore.GREEN}Succesfully begged. [DANK MEMER] || (All commands Logged Succesfully!)")
			await ctx.send('pls dig')
			print(f"{Fore.GREEN}Succesfully digged. [DANK MEMER] || (All commands Logged Succesfully!)")
			await ctx.send('$$autodank')
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}Succesfully hunted. [DANK MEMER] || (All commands Logged Succesfully!)")
			await asyncio.sleep(69)
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}Succesfully fished. [DANK MEMER] || (All commands Logged Succesfully!)")
			await ctx.send('pls pm')
			await ctx.send('F')
			await ctx.send('$$autodank')
      

@bot.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	await ctx.send('Dank Memer Selfbot is now **DISABLED**. ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||https://cdn.discordapp.com/attachments/800567178579017779/887185338475360301/depositphotos_85197786-stock-photo-young-man-with-thums-up.png')
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="Dank Memer Auto Farm || thr#8159", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}

▀▀█▀▀ ▒█░▒█ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
░▒█░░ ▒█▀▀█ ▒█▄▄▀ ░▀▀▀▄▄ 　 ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
░▒█░░ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ 　 ▒█▄▄█ ▒█▄▄▄█ ░▒█░░
{Fore.RED}    

{Fore.GREEN}
▀▀█▀▀ ▒█░▒█ ▒█▀▀█ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
░▒█░░ ▒█▀▀█ ▒█▄▄▀ ░▀▀▀▄▄ 　 ▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
░▒█░░ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█ 　 ▒█▄▄█ ▒█▄▄▄█ ░▒█░░

▒█▀▀▄ █▀▀█ █▀▀▄ █░█ 　 █▀▄▀█ █▀▀ █▀▄▀█ █▀▀ █▀▀█ 
▒█░▒█ █▄▄█ █░░█ █▀▄ 　 █░▀░█ █▀▀ █░▀░█ █▀▀ █▄▄▀ 
▒█▄▄▀ ▀░░▀ ▀░░▀ ▀░▀ 　 ▀░░░▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░▀▀
selfbot is ready!
''')

bot.run(token, bot=False)

