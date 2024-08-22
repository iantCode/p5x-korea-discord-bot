import imaplib
import email
from bs4 import BeautifulSoup
from datetime import datetime
from const.keys import EMAIL_PASSWORD

class EmailResult:
    def __init__(self, timestamp: int, code: str):
        self.timestamp = timestamp
        self.code = code

def download_email_code(user: str, password: str) -> EmailResult:
    imap = imaplib.IMAP4_SSL("iant.kr")
    try:
        imap.login(user, password)
    except:
        print("Wrong Email or Password")
        raise ConnectionAbortedError

    imap.select("INBOX")

    _, messages = imap.uid('search', None, '(FROM "p5xkr@mail.perfectworldgames.com")')
    messages = messages[0].split()
    recent = messages[-1]
    _, msg = imap.uid('fetch', recent, "(RFC822)")

    raw = msg[0][1].decode('utf-8')

    email_message = email.message_from_string(raw)
    body = email_message.get_payload(decode=True).decode()

    soup = BeautifulSoup(body, 'html.parser')
    code_tag = soup.select_one("td > div")
    code = code_tag.get_text(strip=True)
    time = datetime.strptime(email_message["Date"], "%a, %d %b %Y %H:%M:%S %z")
    timestamp = int(time.timestamp())

    return EmailResult(timestamp, code)


def get_email_code():
    recent_code = EmailResult(0, "")
    for i in range(1, 6):
        new_code = download_email_code(f"test{i}@iant.kr", EMAIL_PASSWORD)
        if recent_code.timestamp < new_code.timestamp:
            recent_code = new_code

    return recent_code.code

if __name__ == "__main__":
    get_email_code()