"""
page: http://www.pythonchallenge.com/pc/def/ocr.html

recognize the characters. maybe they are in the book,
but MAYBE they are in the page source.


General tips:
Use the hints. They are helpful, most of the times.
Investigate the data given to you.
Avoid looking for spoilers.

Forums: Python Challenge Forums, read before you post.
IRC: irc.freenode.net #pythonchallenge

To see the solutions to the previous level, replace pc with pcc, i.e. go to: http://www.pythonchallenge.com/pcc/def/ocr.html
"""

from urllib.request import urlopen
import re

def solution():
    text = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode('utf-8')
    comment_area = re.findall(r'<!--\n(.*?)\n-->', text, re.S)[1]
    answer = ''.join(re.findall(r'[a-zA-Z]', comment_area))
    return "http://www.pythonchallenge.com/pc/def/{}.html".format(answer)


if __name__ == '__main__':
    print(solution())