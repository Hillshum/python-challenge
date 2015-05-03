#!/usr/bin/env python3

# This is for pythonchallenge.com #6

import zipfile
from urllib import request
import re
from time import sleep

import PythonChallenge

PAGEURL = 'http://www.pythonchallenge.com/pc/def/channel.zip'
NOTHING_COUNT = 40000
NOTHING_REGEX = r'(?<=g\sis\s)[0-9]+'
SLEEPTIME = 0

r = re.compile(NOTHING_REGEX)


class PC6Solver(PythonChallenge.Solver):
    def __init__(self, url=PAGEURL):
        self.url = PAGEURL
        self.nothings = []
        self.comments = []
        super().__init__()

    def fetch_zip(self):
        local_filename, headers = request.urlretrieve(self.url)
        self.zfile = zipfile.ZipFile(local_filename)

    def parse_nothing(self):
        r = re.compile(r'(?<=nothing=)\d+(?=")')
        m = r.search(self.textfile.read().decode())
        self.next_nothing = m.group(0)

    def parse_readme(self, text):
        r = re.compile(r'(?<=start from )\d+(?=$)', re.MULTILINE)
        m = r.search(text)
        self.current_work = self.next_nothing = m.group(0)

    def get_nothing(self, nothing, r=r):

        textfile = self.zfile.open(nothing + ".txt")
        text = ''
        for i in textfile.readlines():
            text += i.decode()
        self.current_text = self.current_work = text

    def process_text(self):
        match = r.search(self.current_text)
        self.next_nothing = match.group(0)
        self.current_work = self.next_nothing

    def is_solved(self):

        return False
        checkre = re.compile(r'[A-Za-z]+.html$')
        match = checkre.match(self.current_text)
        if match:
            self.current_work = match.group()
            self.solved = True
            return True
        else:
            return False

    def process_nothings(self, count=NOTHING_COUNT):

        while True:
            self.nothings.append((self.next_nothing, self.current_text))
            self.comments.append(self.zfile.getinfo(
                self.next_nothing+'.txt').comment.decode())
            print(self.current_text, self.next_nothing)
            sleep(SLEEPTIME)
            self.get_nothing(self.next_nothing)
            try:
                self.process_text()
            except Exception:
                self.current_work = ''.join(self.comments)
                return

    def solve(self):
        self.fetch_zip()
        self.get_nothing('readme')
        self.current_work = self.current_text
        self.parse_readme(self.current_text)
        self.process_nothings()

        print(self.current_work)


if __name__ == '__main__':
    PC6Solver().solve()
