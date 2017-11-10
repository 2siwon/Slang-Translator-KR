import datetime
import time
import urllib.request
import urllib.parse

import os

from django.conf import settings
from django.shortcuts import render


def send_to_naver(request):
    client_id = "Gae4R9qRa3pBYxPxh8rx"
    client_secret = "7Zw7eh7BUG"

    if request.method == 'POST':

        text = request.POST.get('content')
        print(f'급식체로 변환된 텍스트 : {text}')
        encText = urllib.parse.quote(text)

        # speaker, speed, 입력한 텍스트
        data = "speaker=mijin&speed=0.1&text=" + encText
        url = "https://openapi.naver.com/v1/voice/tts.bin"

        # request 만들기
        send_to_naver_request = urllib.request.Request(url)
        # header에 cliend_id, cliend_secret 추가
        send_to_naver_request.add_header("X-Naver-Client-Id", client_id)
        send_to_naver_request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(send_to_naver_request, data=data.encode('utf-8'))
        rescode = response.getcode()

        if rescode == 200:
            response_body = response.read()

            now = datetime.datetime.now()
            nowDate = now.strftime('%Y-%m-%d')
            nowTime = now.strftime('%H-%M-%S')

            if not os.path.isdir(nowDate):
                os.mkdir(nowDate)
            filename = f'{nowDate}/{nowTime}.mp3'

            with open(filename, 'wb') as f:
                f.write(response_body)

            file_path = os.path.join(settings.BASE_DIR, filename)
            print(f'file_path : {file_path}')

            context = {
                'file_path': file_path,
            }
            return render(request, 'index.html', context)
        else:
            print(f"Error Code: {rescode}")
    else:
        return render(request, 'index.html')
