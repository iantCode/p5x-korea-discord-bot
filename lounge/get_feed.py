import requests
from bs4 import BeautifulSoup

class FeedResult:
    def __init__(self, title:str, content: str, img_path: str):
        self.title = title
        self.content = content
        self.img_path = img_path


def get_feed_by_id(feed_id: int) -> FeedResult:
    feed_url = f"https://comm-api.game.naver.com/nng_main/v1/community/lounge/P5X/feed/{feed_id}"
    resp = requests.get(feed_url)
    
    if resp.status_code != 200:
        raise ConnectionError

    resp_json = resp.json()
    title = resp_json['content']['feed']['title']
    img_path = resp_json['content']['feed']['repImageUrl']

    content_html = resp_json['content']['feed']['contents']
    content = compile_text_from_html(content_html)
    

    return FeedResult(title, content, img_path)


def compile_text_from_html(content_html: str) -> str:
    '''
        그냥 soup.get_text()를 하는 경우 span 태그가 띄어쓰기되어
        원하는 형태가 나오지 않으므로 직접 코드를 작성했습니다.
    '''
    soup = BeautifulSoup(content_html, 'html.parser')
    content = ''
    for p in soup.select('p'):
        if len(p.select('span')) > 0:
            content += '\n'
            for span in p.select('span'):
                span_text = span.get_text()
                content += span_text
        else:
            content += '\n' + p.get_text('\n', strip=True)
    
    return content.strip()


if __name__ == "__main__":
    print(get_feed_by_id(4637065).content)