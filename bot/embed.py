from bot.bot import p5xbot
from discord.ext import commands
import discord


@p5xbot.hybrid_command(name="embed",description="텍스트를 임베디드로 바꿔주는 커맨드")
@commands.has_permissions(manage_messages=True)
@discord.app_commands.describe(text="텍스트", color='색상을 hex로 작성해주세요. ex) ff0000')
async def make_embed(ctx: commands.Context, color: str, *, text: str):
    try:
        color_hex = int(color, base=16)
    except ValueError:
        await ctx.send(f'{color}는 정확한 색상 코드가 아닙니다.')
        return
    
    # /embed를 위한 예외 처리
    try:
        await ctx.message.delete()
    except:
        pass
    
    embed = discord.Embed(description=text, color=color_hex)
    await ctx.send(embed=embed)


@make_embed.error
async def make_embed_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("색상 또는 텍스트가 작성되지 않았습니다.")