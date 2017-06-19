"""
page: http://www.pythonchallenge.com/pc/def/map.html


General tips:
Use the hints. They are helpful, most of the times.
Investigate the data given to you.
Avoid looking for spoilers.

Forums: Python Challenge Forums
"""


def solution():
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    translated_text = translate(text)

    # now apply on url
    url = 'map'
    answer = translate(url)

    return 'http://www.pythonchallenge.com/pc/def/' + answer + '.html'
    # i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.


def translate(text):
    return ''.join(letter_map(l) for l in text)


def letter_map(letter):
    if letter >= 'a' and letter <= 'z':
        letter_space_size = 26
        translated_ltr = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
        return translated_ltr
    else:
        return letter

if __name__ == '__main__':
    print(solution())
