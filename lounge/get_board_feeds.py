import requests
from typing import List
from enum import Enum


class BoardType(Enum):
    NOTIF = 1
    UPDATE = 2
    UPDATE_GRAPHIC = 3
    CHARACTER = 12
    PERSONA = 13


class BoardResult:
    def __init__(self, feed_id: int, board_type: BoardType):
        self.feed_id = feed_id
        self.board_type = board_type


def get_board_feeds_by_id(board_id: BoardType) -> List[BoardResult]:
    '''
        지정한 게시판에 추가된
        글 리스트를 불러오는 코드
    '''
    content_url = f"https://comm-api.game.naver.com/nng_main/v1/community/lounge/P5X/feed?boardId={board_id.value}&limit=3&offset=0&order=NEW"
    resp = requests.get(content_url)

    if resp.status_code != 200:
        raise ConnectionError
    
    resp_json = resp.json()
    
    boards: List[BoardResult] = []
    for feed in resp_json['content']['feeds']:
        new_feed = BoardResult(feed['feedId'], board_id)
        boards.append(new_feed)

    return boards


if __name__ == "__main__":
    print(get_board_feeds_by_id(1))