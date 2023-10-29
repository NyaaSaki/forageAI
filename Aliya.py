import discord
from discord.ext import commands
client = commands.Bot(command_prefix="alia ",intents=discord.Intents.all())

import gpt

awaitingMessage = [0]
def waitfor(member,ctx):
    global awaitingMessage
    awaitingMessage = [member,ctx]
    print(member)


@client.event
async def on_ready():
    print("goodmorning!")
    awaitingMessage = 0
    print("-------------------------------------")
    
@client.event
async def on_message(message):
    global awaitingMessage
    targQuery = awaitingMessage[0]
    #print("got message")
    if(message.author == targQuery):
        async with awaitingMessage[1].typing():
            resp = gpt.req(message.content)
            await message.reply(resp[0])
            print(resp)
            awaitingMessage = [0]
            
    #print("ended this")
    await client.process_commands(message)
        

    
@client.command()
async def hello(ctx):
    await ctx.send("Hi! im Alia the forager! you can ask me about wild plants!")
    
@client.command()
async def listen(ctx,mod= " ", mod1=" "):
    await ctx.reply("I am now listening to you.")
    waitfor(ctx.author,ctx)
    if mod.lower() in ["close","closely","carefully"]:       
        await ctx.send(''.join([mod.lower(),"."]))
        
@client.command()
async def chat(ctx,msg = "X"):
    if msg == "X":
        await ctx.reply("Do tell.")
        waitfor(ctx.author,ctx)
        return
    resp = gpt.req(ctx.message.content[9:])
    await ctx.reply(resp[0])
    print(resp)

@client.command()
async def dump(ctx):
    await ctx.send(gpt.gptlog)
    
@client.command()
async def waiting(ctx):
    await ctx.send(awaitingMessage[0])
    
        
    
client.run(open("token","r").read())