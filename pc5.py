#!/usr/bin/python3

# This is for pythonchallenge.com #5
# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
from urllib import request
from PythonChallenge import Solver


URL = 'http://www.pythonchallenge.com/pc/def/peak.html'
BASE_URL = 'http://www.pythonchallenge.com/pc/def/'
INITIAL_REGEX = r'(?<=\<peakhell src=")\w+\.\w+(?="\/\>)'

# Ready data to parse
# p = pickle.load(open('banner.p'))


class PC5Solver(Solver):
    def __init__(self):
        self.url = URL

    def decipherLine(self):
        """
        This function takes a list as a line in the banner file and returns a
            string for that line.
        """
        resultList = []
        for i in self.current_line:
            newchars = i[0] * i[1]
            resultList.append(newchars)

        return ''.join(resultList)

    def fetch_pickle(self):
        self.p = request.urlopen(BASE_URL + self.initial_clue)
        self.current_work = self.p
        print('Download Successful')
        return True

    def load_pickle(self):
        up = pickle.Unpickler(self.p)
        self.current_work = self.unpickled = up.load()

    def parse_pickled(self):
        """The banner file contines ASCII art. Each item in the list is a line of
        the artwork. Within each line, each tuple represents a character and the
        number of times to repeat it.
        """
        message_list = []
        for line in self.unpickled:
            for char in line:
                message_list.append(char[0] * char[1])
            message_list.append("\n")
        self.current_work = self.message = ''.join(message_list)

    def solve(self):
        self.fetch_page()
        self.parse_page(INITIAL_REGEX)
        self.fetch_pickle()
        self.load_pickle()
        self.parse_pickled()

        print(self.current_work)
