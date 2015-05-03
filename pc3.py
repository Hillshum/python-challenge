#!/usr/bin/env python3


# This is for PythonChallenge.com #3

import re, urllib

import PythonChallenge

REGEX = r'(?<=[^A-Z][A-Z]{3})[a-z](?=[A-Z]{3}[^A-Z])'

URL = 'http://www.pythonchallenge.com/pc/def/equality.html'


class PC3Solver(PythonChallenge.Solver):
    
    def __init__(self):
        self.url = URL


    def get_clue(self):
        r = re.compile(r'(?<=!--)[\S\s]*(?=-->)')
        self.clue = r.search(self.page.read().decode()).group()
        self.current_work = self.clue

    def parse_clue(self):
        r = re.compile(REGEX)
        self.matches = r.findall(self.clue)
        self.result = ''.join(self.matches)
        self.current_work = self.result




    def solve(self):
        self.fetch_page()
        self.get_clue()
        self.parse_clue()
        return self.result

        
