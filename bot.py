


import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

@bot.command(name="version")  
async def version(context):
        
        myembed1 = discord.Embed(title="MY VERSION", description="THE VERSION IS 5.0", color=0x87)
        myembed1.add_field(name="VERSION CATEGORY", value="MODRATIVE", inline=False)
        myembed1.add_field(name="VERSION CODE", value="v5.3.0", inline=False)
        myembed1.add_field(name="DATE REALEASED", value="JULY 18TH, 2021", inline=False)
        myembed1.add_field(name="INTRODUCTION", value="I AM DOCKY I CAN DO ANYTHING LIKE A ADMIN")
        myembed1.set_footer(text="VERSION AND INTRO")
        myembed1.set_author(name="SCARL EYE GAMING")
        await context.message.channel.send(embed=myembed1)
        await context.send("THANKS FOR JOINING SERVER CHECK THIS VIDEO TO LEARN ABOUT OUR SERVER", file=discord.File("images.jpg/dev.mp4"))
       



@bot.event
async def on_ready():

   general = bot.get_channel(932500994066112612) 
   await general.send("CONNECTED!")

    
    
@bot.event
async def on_message(message):

    general = bot.get_channel(932500994066112612)
    if message.content == "hello":
        await general.send("Hello sir")
    elif message.content == "i am here":
        await general.send("Ok Sir You Can Continue")
    elif message.content == "please introduce":
            myembed1 = discord.Embed(title="MY VERSION", description="THE VERSION IS 5.0", color=0x87)
            myembed1.add_field(name="VERSION CATEGORY", description="MODERATIVE")
            myembed1.add_field(name="VERSION CODE", value="v5.3.0", inline=False)
            myembed1.add_field(name="DATE REALEASED", value="JULY 18TH, 2021", inline=False)
            myembed1.add_field(name="INTRODUCTION", value="I AM DOCKY I CAN DO ANYTHING LIKE A ADMIN")
            myembed1.set_footer(text="VERSION AND INTRO")
            myembed1.set_author(name="SCARL EYE GAMING")
            await general.send(embed=myembed1)
    
    await bot.process_commands(message)
        
@bot.event
async def on_disconnect():

    general_chennel = bot.get_channel(932500994066112612)
   
    general_chennel.send("bye")
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="RULE INFOLLOWED"
    myembed2 = discord.Embed(title="USER KICK", description="ONE MEMBER KICKED", color=0x87)
    myembed2.add_field(name="NAME OF MEMBER", value="{member.mention}", inline=False)
    myembed2.add_field(name="TYPE OF KICK", value="BOT KICKED", inline=False)
    myembed2.add_field(name="REASON", value=reason, inline=False)
    myembed2.set_footer(text="FROM : DOCKY")
    myembed2.set_author(name="DOCKY")
    await ctx.guild.kick(member)
    await ctx.send(myembed2)


@bot.event
async def on_member_join(member):
    await member.send("A NEW MEMBER JOINED OUR TEAM" + " WELCOME! {member.mention}")

@bot.command()
async def message(ctx, user: discord.Member, *, message=None):
    message = "WELCOME TO OUR SERVER!"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)
    await ctx.send("THANKS FOR JOINING SERVER CHECK THIS VIDEO TO LEARN ABOUT OUR SERVER", file=discord.File("images.jpg/dev.mp4"))


bot.run("OTMyNDkyMzA1MzQ3MjUyMjI0.YeTxIg.DqZOr8bjhTpO14zT5rbHh2DnLF0")