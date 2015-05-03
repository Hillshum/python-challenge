#!/usr/bin/env python3

# This is for PythonChallenge 2


import urllib.request, re, operator


URL = "http://www.pythonchallenge.com/pc/def/ocr.html"
REGEX = r'in the mess below:\n*-->\n*<!--([\S\s]*)-->'


class PC2Solver:
    
    def __init__(self, url=URL, regex = REGEX):
        self.r = re.compile(regex)
        self.url = url
        self.current_work = url

    def fetch_page(self, url=URL):
        
        self.page = urllib.request.urlopen(url)
        #TODO: Network error handling
        self.current_work = self.page
        print('Download Successful')
        return True


    def parse_for_clue(self):

        self.page_text = self.page.read().decode()

        self.matched_text = self.r.search(self.page_text).groups(1)[0]
        self.current_work = self.matched_text

    def process_clue(self):

        # First get a dictionary of the frequency of each character
        # TODO: replace with collections.Counter
        frequency_table = {}
        for i in self.matched_text:
            if i in frequency_table:
                frequency_table[i] += 1 
            else:
                frequency_table[i] = 1

        # Will assume anything appearing less than 1000 times is meaningful
        # TODO: allow for overriding of that constant or eliminate the need
        self.significant_chars = []
        for k,v in list(frequency_table.items()):
            if v < 1000:
                self.significant_chars.append(k)

        self.current_work = self.significant_chars


    def find_anagram(self):
        try:
            self.anagram_finder
        except AttributeError:
            self.anagram_finder = AnagramFinder()
        self.anagrams = self.anagram_finder.find(self.significant_chars)
        self.current_work = self.anagrams
        
        


    
    def solve(self):
        self.fetch_page()
        self.parse_for_clue()
        self.process_clue()
        self.find_anagram()

        self.solution = self.anagrams

        print(self.anagrams)
        



class AnagramFinder:
    
    def  __init__(self):
        #TODO: Don't hardcode the following path.
        word_file = open('/home/hillshum/Dropbox/Code/PythonChallenge/enable1.txt')
        self.word_dict = {}
        for line in word_file:
            self.word_dict[line.rstrip()] = sorted(line.rstrip())

    def find(self, word):
        sorted_word = sorted(word)
        anagram_list = []
        for k,v in self.word_dict.items():
            if sorted_word == v:
                anagram_list.append(k)
        return anagram_list

        










