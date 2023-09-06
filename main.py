import discord
import os
from map_data import add_new_info, authenticate_me, get_my_info, get_creative_map
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="lord ", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.tree.sync()


@bot.command()
async def random_creative(ctx):
    print("Yes")
    await ctx.send("Creative Maps")

@bot.command()
async def save_me(ctx, user, pwd):
    await ctx.message.delete()
    add_new_info(ctx.message.author.id, user, pwd)
    await ctx.send("Stored successfully")

@bot.command()
async def login(ctx):
    result = get_my_info(ctx.message.author.id)
    if result == {}:
        await ctx.send("Please Register your Details")
    else:
        username = result["username"]
        password = result["password"]
        authenticate_me(username, password)
        await ctx.send("Successfully Logged In")

@bot.command()
async def creative(ctx):
    get_creative_map()

token = os.environ.get("TOKEN")

# @bot.event
# async def on_message(message):
#     if message.content.startswith('lord save_me'):
#         await message.delete()
#         await asyncio.sleep(0.001)
#         # add_new_info(message.author.id, message.content.split(" ")[2], message.content.split(" ") [3])


# Run the bot
bot.run(token)  # Replace with your bot's token
