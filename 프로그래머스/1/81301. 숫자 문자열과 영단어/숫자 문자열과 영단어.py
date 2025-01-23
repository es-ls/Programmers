def solution(s):
    # 숫자에 대응하는 영단어를 딕셔너리로 정의
    digit_to_word = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    # 영단어를 숫자로 변환하기 위한 역 딕셔너리 생성
    word_to_digit = {v: k for k, v in digit_to_word.items()}

    result = ""  # 최종 결과 문자열
    temp = ""  # 영단어를 임시 저장할 변수

    i = 0
    while i < len(s):
        if s[i].isdigit():
            result += s[i]  # 숫자인 경우 그대로 추가
            i += 1
        else:
            temp += s[i]  # 영단어 부분을 하나씩 추가
            if temp in word_to_digit:
                result += word_to_digit[temp]  # 영단어를 숫자로 변환하여 추가
                temp = ""  # 임시 문자열 초기화
            i += 1

    return int(result)  # 정수형으로 변환하여 반환
