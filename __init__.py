#!/usr/bin/env python3

from urllib import request

BASE_URL = 'http://www.pythonchallenge.com/pc/def/'

class Solver(object):
    def __init__(self):
        self.solved = False

    def fetch_page(self):

        self.page = request.urlopen(self.url)
        #TODO: Network error handling
        self.current_work = self.page
        print('Download Successful')
        return True

    def parse_page(self,regex):
        """
        This method accepts a regex string and parses the page
        source for initial clues.

        The regex should match the clue and use lookarounds for
        context
        """
        page_text = self.page.read().decode()
        clue = re.compile(regex).search(page_text).group()
        self.initial_clue = (clue)
        self.current_work = self.initial_clue


        """
    def solve(self):
        This method should generally be customized by subclasses,
        but will provide a base skeleton for use in development
        self.
        """



