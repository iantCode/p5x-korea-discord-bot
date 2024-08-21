async def send_long_text(channel, text:str):
    '''
        2000자 이상인 글 ex) 업데이트 패치 노트 를 다루기 위하여 1900자 쯤에서
        새로운 텍스트로 작성하는 코드
    '''

    temp_text = ''
    for split in text.split('\n'):
        if len(temp_text) + len(split) > 1900:
            text_to_send = temp_text.replace('\n\n', '\n').strip()
            await channel.send(text_to_send)
            temp_text = ''
        temp_text += '\n' + split
    text_to_send = temp_text.replace('\n\n', '\n').strip()
    if len(text_to_send) != 0:
        await channel.send(text_to_send)