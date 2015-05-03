#!/usr/bin/evn python3

from urllib import request

from PythonChallenge import Solver, BASE_URL

URL = 'http://www.pythonchallenge.com/pc/def/oxygen.html'
BASE_URL = 'http://www.pythonchallenge.com/pc/def/'
INITIAL_REGEX = r'(?<=img src=")\w+\.\w+(?=")'


class PC7Solver(Solver):
    def __init__(self):
        self.url = URL

    def fetch_image(self):
        self.image = request.urlopen(self.url)
        print('Download Successful')
        return True

