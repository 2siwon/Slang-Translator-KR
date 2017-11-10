import random
from konlpy.tag import Mecab
from requests import put

YAMIN_DICT = {
    '명': '띵',
    '대': '머',
    '귀': '커',
    '피': '끠',
    '포': '쪼',
    '비': '네',
    '유': '윾',
    '며': '띠',
    '광': '팡',
    '명': '띵',
    '오우야': '퍄',
    '교': '꼬',
    '식': '싀',
    '왕': '앟',
    '진짜': '레알',
}

ADMIT_LIST = [
    'ㅇㅈ? 어 ㅇㅈ',
    "ㅇㅈ하는 부분? 어 ㅇㅈ",
    "ㅇㅈ? ㅇㅇㅈ 씹ㅇㅈ",
    "ㅇㅈ하는 부분이구요",
    "ㅇㅈ할껀 ㅇㅈ하자...",
    "admit? uh admit",
    "ㅇㅈㄱ? ㅇㅆㅇㅈ",
]

LENGTH_ADMIT_LIST = len(ADMIT_LIST)

def append_admit(li, morpheme, word):
    """
    인정 구문을 추가하는 함수
    :param li: 인정 구문을 추가하려고 하는 대상 list
    :param morpheme: 형태소 종류
    :param word: 현재 단어
    :return:
    """
    if morpheme == 'XSA' or morpheme == 'VX+EP':
        li.append(f'{word[0]} ')
    else:
        li.append("은 부분 ")
    li.append(ADMIT_LIST[random.randint(0, LENGTH_ADMIT_LIST - 1)])

def jong_sung_check(char):
    pass

def make_hangul_unicode(cho, jung, jong):
    unicode = 0xAC00 + ((cho * 21) + jung) * 28 + jong
    return chr(unicode)

def string_to_yamin(str):
    """
    string을 받아 야민정음 dictionary에 해당 string의 char가 있을경우 변경하여 '야민화'된 string을 반환
    :param str:
    :return:
    """
    li = []
    for char in str:
        yamin_char = YAMIN_DICT.get(char)
        if yamin_char:
            li.append(yamin_char)
        else:
            li.append(char)
    return "".join(li)

def convert(string):
    """
    string을 받아 급식체로 번역된 string을 반환
    :param string:
    :return:
    """
    # 한국어 형태소 분석기 mecab-ko
    mecab = Mecab()

    # 전달받은 string을 (<단어>, <품사>) Tuple 단위로 쪼개어 list를 반환
    word_class_list = mecab.pos(string)
    # print(word_class_list)

    # 번역 문장 생성
    translated_words = []
    for i, word in enumerate(word_class_list):
        if word[1] == 'EF' and random.random() < 0.5:
            append_admit(translated_words, word_class_list[i-1][1], word)
        else:
            translated_words.append(word[0])

    # 번역 문장 concatenate
    translated_string = "".join(translated_words)

    # 띄어쓰기 http://freesearch.pe.kr/archives/4647 API 사용
    translated_string_spaced = put('http://35.201.156.140:8080/spacing',
                      data={'sent': translated_string}).json()['sent']

    # 야민정음에 따라 글자 변경
    yamin_string = string_to_yamin(translated_string_spaced)

    return yamin_string


if __name__ == "__main__":
    string_1 = "영등포구청역에 있는 맛집 좀 알려주세요."
    print(string_1)
    print(convert(string_1))

    string_2 = "서든어택, 리그 오브 레전드에서 많이 볼 수 있다!"
    print(string_2)
    # 서든, 롤에서 많이 볼 수 있는 부분? 어 ㅇㅈ 씹ㅇㅈ하는 부분이구연~
    print((convert(string_2)))

    string_3 = " 특히 롤에서 픽 싸움 났을 때 칼락인을 박는 경우가 많고, 게임 실력도 대부분 딱히 좋지는 않다. 정작 자신들이 패배하면 대부분 정신승리를 " \
               "강행하는 것도 하나같이 똑같다. 그리고 가끔가다 실력에 대해 지적을 하다보면 탈주를 하는 일이 빈번하다.롤 안하는 학생들은 뭔 뜻인지도 " \
               "모르는데 어깨 맞닿은 놈들이 쓰는 거 들으면서 살아야 한다. 실력 좋아도 쓰는 놈들 많다."
    # 특히 리그 오브 레전드에선 마스터 이, 제드, 야스오, 리 신, 베인, 티모, 블크 등 충이 꼬이는 챔피언에서 오질나게 나오는거 오지게 인정하는 부분?
    # 어 ㅇㅈ 사스가 급식충 오지구연~ 기모띠 앙 기모띠!
    print(string_3)
    print(convert(string_3))

    string_4 = "그리고 요즘은 어디서 일베 말투를 주워 들어서 허구한 날 사용하는 경우도 굉장히 많아졌다. (특히 인터넷 상에서)"
    print(string_4)
    print(convert(string_4))