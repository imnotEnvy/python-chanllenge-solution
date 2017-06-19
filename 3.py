"""
page: http://www.pythonchallenge.com/pc/def/equality.html

One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.


To see the solutions to the previous level, replace pc with pcc, i.e. go to: http://www.pythonchallenge.com/pcc/def/equality.html

Join us on IRC: irc.freenode.net #pythonchallenge
"""

from urllib.request import urlopen
import re


def solution():
    text = urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
    comment_area = re.findall(r'<!--\n(.*?)\n-->', text, re.DOTALL)[-1]

    # solve
    answer = ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', comment_area))
    return "http://www.pythonchallenge.com/pc/def/{}.html".format(answer)


if __name__ == '__main__':
    print(solution())
