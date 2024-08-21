from lounge.get_board_feeds import BoardType, BoardResult, get_board_feeds_by_id
from lounge.get_feed import get_feed_by_id
from youtube.get_new_videos import get_new_videos, VideoResult
from datetime import datetime
from typing import Dict, List
import asyncio
import random

async def check_new_content():
    from bot.post import post_feed, post_video
    
    new_feeds: Dict[int, BoardResult] = {}
    new_videos: Dict[str, VideoResult] = {}
    while True:
        print("[API] checking", datetime.now())
        feeds_list = get_new_feeds()
        video_feeds = get_new_videos()

        if not new_feeds:
            for feed in feeds_list:
                new_feeds[feed.feed_id] = feed
            
            for video in video_feeds:
                new_videos[video.video_id] = video
        
        else:
            for feed in feeds_list:
                if feed.feed_id not in new_feeds:
                    content = get_feed_by_id(feed.feed_id)
                    print(f"새 글 발견! {content.title}")
                    await post_feed(feed, content)
                    new_feeds[feed.feed_id] = feed

            for video in video_feeds:
                if video.video_id not in new_videos:
                    print(f"새 동영상 발견! {video.title}")
                    await post_video(video)
                    new_videos[video.video_id] = video

        await asyncio.sleep(55 + random.random() * 10)


def get_new_feeds() -> List[BoardResult]:
    notif_feeds = get_board_feeds_by_id(BoardType.NOTIF)
    update_feeds = get_board_feeds_by_id(BoardType.UPDATE)
    update_graphic_feeds = get_board_feeds_by_id(BoardType.UPDATE_GRAPHIC)
    character_feeds = get_board_feeds_by_id(BoardType.CHARACTER)
    persona_feeds = get_board_feeds_by_id(BoardType.PERSONA)

    return [*notif_feeds, 
            *update_feeds, 
            *update_graphic_feeds, 
            *character_feeds, 
            *persona_feeds]


if __name__ == "__main__":
    print(get_new_feeds())