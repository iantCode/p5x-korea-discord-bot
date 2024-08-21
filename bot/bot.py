import discord
from discord.ext import commands
from api.check_new_content import check_new_content

intents = discord.Intents.default()
intents.message_content = True
p5xbot = commands.Bot(command_prefix="!",intents=intents)

@p5xbot.event
async def on_ready():
    import bot.embed
    
    print("Bot is ready.")
    await p5xbot.change_presence(activity=discord.Game(name="페르소나5: 더 팬텀 X"))
    await p5xbot.tree.sync()
    await check_new_content()