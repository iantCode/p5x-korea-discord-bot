import requests
from typing import List
from const.keys import GOOGLE_CLOUD_KEY

class VideoResult:
    def __init__(self, video_id: str, title: str, desc: str, thumb_url: str):
        self.video_id = video_id
        self.title = title
        self.desc = desc
        self.thumb_url = thumb_url

def get_new_videos() -> List[VideoResult]:
    '''
        새 영상을 불러와 List[VideoResult] 형태로 저장
    '''
    resp = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", {
        "key": GOOGLE_CLOUD_KEY,
        "playlistId": "UULFJVvGWkPHv-jHxijkAyk2Og",
        'part': "snippet"
    })

    if resp.status_code != 200:
        raise ConnectionError

    resp_json = resp.json()
    
    result: List[VideoResult] = []

    for item in resp_json['items']:
        video_id = item['snippet']['resourceId']['videoId']
        title = item['snippet']['title']
        desc = item['snippet']['description']
        thumb_url = item['snippet']['thumbnails']['maxres']['url']
        new_video = VideoResult(video_id, title, desc, thumb_url)
        result.append(new_video)
    
    return result

get_new_videos()