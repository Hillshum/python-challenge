#!/usr/bin/env python3

# This is for pythonchallenge.com #4


import urllib.request, urllib.parse, urllib.error, re

import PythonChallenge

PAGEURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
BASEURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
NOTHING_COUNT = 400
NOTHING_REGEX = r'(?<=g\sis\s)[0-9]+'

r = re.compile(NOTHING_REGEX)


	


class PC4Solver(PythonChallenge.Solver):
    
    def __init__(self,url=PAGEURL):
        self.url=PAGEURL
        self.nothings = []
        super().__init__()


    def parse_page(self):
        r = re.compile(r'(?<=nothing=)\d+(?=")')
        m = r.search(self.page.read().decode())
        self.next_nothing = m.group(0)

        

    def fetch_nothing(self, nothing='44827',r=r):
        nothingUrl= urllib.request.urlopen(BASEURL+nothing)
        text = nothingUrl.read().decode()

        self.current_text = text
        self.current_work = text
        print(text)


    def check_for_division(self):
        # This one checks for an obnoxious little clause in the nothings
        # TODO: When the nothing comes that tells to divide, go back and do so
        # That will involve creating a record of all past nothings
        
        if re.compile(r'Divide').search(self.current_text):
            self.next_nothing = str(int(self.nothings[-1])/2)[:-2]
            return True
        """
        if self.next_nothing == '16044':
            self.next_nothing = str(int(self.next_nothing)/2)
            print("Dividing by 2 for 16044')
            """

    
    def process_text(self):
        match = r.search(self.current_text)
        if not  self.check_for_division():
            self.next_nothing = match.group(0)
        self.current_work = self.next_nothing

    def is_solved(self):

        checkre = re.compile(r'[A-Za-z]+.html$')
        match = checkre.match(self.current_text)
        if match:
            self.current_work = match.group()
            self.solved = True
            return True
        else:
            return False


    def process_nothings(self,count=NOTHING_COUNT):
	
        for i in range(count):
            self.nothings.append(self.next_nothing) 
            print(i)
            self.fetch_nothing(self.next_nothing)
            if self.is_solved():
                return True
            self.process_text()


    def solve(self):
        self.fetch_page()
        self.parse_page()
        self.process_nothings()

        print(self.current_work)



if __name__ == '__main__':
    PC4Solver().solve()
