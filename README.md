# malWhere
discord bot remote access tool with a whole multitude of features from trolling to cyber security training


SETUP:

i recommend using pyinstaller to turn this into an exe if you are using standalone however if embedding download code into another application leaving as a python file is perfectly fine. i will probably create a separate tool to automate the whole setup and or creating exe process so stay tuned for that :)

1. create a discord server using the template https://discord.new/ZdhafKFHpkKN
2. copy all the channel/guild ids into their respective placements
3. go to https://beeceptor.com/ and create an mock api with path "/"
4. go to https://www.base64encode.org/ and encode it once.
5. go to http://ipinfo.io to setup the geolocation api
6. get a discord bot token
7. go back to https://www.base64encode.org/ and encode it 5 times.
8. go back to https://beeceptor.com/ and edit the api resonse body to be {"token":"yourtoken"}.
9. enter the encrypted api url into main.py
10. Enjoy
