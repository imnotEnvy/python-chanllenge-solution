"""
page: http://www.pythonchallenge.com/pc/def/0.html
hint: Hint: try to change the URL address.
"""

def solution():
    url = "http://www.pythonchallenge.com/pc/def/0.html"
    return url.replace('0', str(pow(2, 38)))

if __name__ == "__main__":
    print(solution())