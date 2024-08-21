from lounge.get_feed import FeedResult
from lounge.get_board_feeds import BoardType, BoardResult
from bot.bot import p5xbot
from utils.send_long_text import send_long_text
from youtube.get_new_videos import VideoResult
import discord


async def post_feed(board_result: BoardResult, feed: FeedResult):
    main_text = get_right_text(board_result, feed)
    channel = get_right_channel(board_result.board_type)

    await send_long_text(channel, main_text)
    if feed.img_path:
        await channel.send(feed.img_path)


def get_right_channel(board_type: BoardType) -> discord.TextChannel:
    if board_type == BoardType.NOTIF:
        return p5xbot.get_channel(1274913413285543956)
    elif board_type == BoardType.UPDATE or board_type == BoardType.UPDATE_GRAPHIC:
        return p5xbot.get_channel(1275343391772643359)
    elif board_type == BoardType.CHARACTER:
        return p5xbot.get_channel(1273919278252294144)
    elif board_type == BoardType.PERSONA:
        return p5xbot.get_channel(1273919179086626836)
    else:
        raise ValueError
    

def get_right_text(board_result: BoardResult, feed: FeedResult):
    main_text = ''
    if board_result.board_type not in [BoardType.CHARACTER, BoardType.PERSONA]:
        main_text += "<@&1274971218801332245>\n"
    main_text += f"## {feed.title}\n{feed.content}"
    return main_text


async def post_video(feed: VideoResult):
    channel = p5xbot.get_channel(1275642835793612800)
    embed = discord.Embed(title=feed.title,
                          description=feed.desc, 
                          color=0xFF0000, 
                          url=f'https://youtu.be/{feed.video_id}')
    embed.set_image(url=feed.thumb_url)
    await channel.send("<@&1274971218801332245> 새로운 영상이 공개되었어요!", embed=embed)