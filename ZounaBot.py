import discord
from Commands import *

prefix = "!"
TOKEN = "<token goes here>"
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.user.display_name)
    
@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        args = message.content.split(" ")
        command = args[0]
        command = command[len(prefix):]
        
        #8ball command
        if command.lower() == "8ball":
            response = f">>> {message.content[len(prefix)+len('8ball'):]}\n"
            response += eight_ball._8ball()
            await message.channel.send(response)
        
        #neko command group
        #TODO: add price
        elif command.lower() == "neko":
            if len(args) > 1:
            
                if args[1].lower() in ["nsfw","lewd"]:
                    if len(args) == 3:
                        try:
                            for i in range(int(args[2])):
                                neko_url = neko.get_neko(True)
                                embed = discord.Embed(url=neko_url,title = f"Lewd neko {i+1}/{args[2]}")
                                embed.set_image(url = neko_url)
                                await message.channel.send(embed=embed)
                        except Exception as e:
                            print(e)
                            await message.channel.send("There is an error with command try again")
                    else:
                        if len(args) == 2:
                            neko_url = neko.get_neko(True)
                            embed = discord.Embed(url=neko_url,title = f"Lewd neko")
                            embed.set_image(url = neko_url)
                            await message.channel.send(embed=embed)
                else:
                    if len(args) == 2:
                        try:
                            for i in range(int(args[1])):
                                neko_url = neko.get_neko(False)
                                embed = discord.Embed(url=neko_url,title = f"Neko {i+1}/{args[1]}")
                                embed.set_image(url = neko_url)
                                await message.channel.send(embed=embed)
                        except Exception as e:
                            print(e)
                            await message.channel.send("There is an error with command try again")
                    
            else:
                neko_url = neko.get_neko(False)
                embed = discord.Embed(url=neko_url,title = f"Neko")
                embed.set_image(url = neko_url)
                await message.channel.send(embed=embed)
        
        
        #classical game of minesweeper
        elif command == "minesweeper":
            if len(args) == 1:
                await message.channel.send(Minesweeper.Minesweeper())
            elif len(args) == 4:
                try:
                    await message.channel.send(Minesweeper.Minesweeper(int(args[1]),int(args[2]),int(args[3])))
                except Exception as e:
                    print (e)
                    await message.channel.send("There is an error with command, try again.")
            else:
                await message.channel.send("There is an error with command, try again.")
                
                
                
    else:
        #update balance
        #update user info
        pass

client.run(TOKEN, bot=True)
