import discord

prefix = "!"
TOKEN = "<token goes here>"
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user.display_name)
    
@client.event
async def on_message(message):
    if message.startswith(prefix):
        args = message.content.split(" ")
        #command manager
    else:
        #update balance
        #update user info
        pass

client.run(TOKEN, bot=True)
