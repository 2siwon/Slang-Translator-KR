import random

from konlpy.tag import Mecab
from konlpy.utils import pprint
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
    '교': '꼬',
    '식': '싀',
    '왕': '앟',
    '배': 'IDH',
    '망': 'ㅁ',
    '디': 'ㅁ',
    '켜': '궈',
    '두': '득',
    '답': '돤',
    '임': '읜',
    '근': 'ㄹ',
    '또': 'SE',
    '태': '래',
    '있': '잇',
    '오우야': '퍄',
    '진짜': '레알',
    '머리': '뚝배기',
}

ADMIT_LIST = [
    '인정? 어 인정',
    "인정하는 부분? 어 인정",
    "인정? 어인정 씹인정",
    "인정하는 부분이구요",
    "인정할껀 인정하자...",
    "admit? uh admit",
    "인정? 반박시 아재 인정?",
]

LENGTH_ADMIT_LIST = len(ADMIT_LIST)



def append_admit(li, previous_word, current_word):
    """
    인정 구문을 추가하는 함수
    :param li: 인정 구문을 추가하려고 하는 대상 list
    :param morpheme: 형태소 종류
    :param word: 현재 단어
    :return:
    """
    print(f'THIS IS APPEND_ADMIT: WORD : {current_word}')
    print(f'THIS IS PREVIOUS WORD : WORD : {previous_word}')
    def has_jongsong(ch):
        ch = ord(ch) - 0xAC00
        return ch % 28
    # ?
    if previous_word[1] == 'XSA' or previous_word[1] == 'VX+EP':
        li.append(f'{current_word[0]} ')
    else:
        # 만약 '다' 전에 종성이 있을 경우(예: 있다, 없다
        if has_jongsong(previous_word[0]):
            li.append("는 부분 ")
        # 종성이 없을 경우(예: 이다)
        else:
            li.append(f'{current_word[0]}. ')
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
    pprint(word_class_list)

    # 번역 문장 생성
    translated_words = []
    for i, word in enumerate(word_class_list):
        if word[1] == 'EF':
            append_admit(translated_words, word_class_list[i - 1][1], word)
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
    # mecab = Mecab()
    # string = input("번역할 string을 입력")
    # print(f'원본:   {string}')
    # pprint(f'형태소분석: {mecab.pos(string)}')
    # print(f'변환 : {convert(string)}')

    string_1 = "요즘 급식충에 대한 부정적인 이미지가 퍼지자 고학년 층에서는 사용을 자제하는 편이다. 특히 고교생들은 남학생들 끼리 장난칠 때나 컨셉잡을 때만 쓰는 듯. 그러나 모두가 그렇다는 것은 아니며, 인터넷이나 게임 같이 익명성이 보장된 곳에서는 고교생이나 그 이상도 써대는 걸 흔하게 볼 수 있다. 심지어는 방송을 하는 스트리머들 중에도 급식체를 쓰는 인간들이 있다.(...) 즉, 이들도 예외는 없다."
    print(string_1)
    print(convert(string_1))
