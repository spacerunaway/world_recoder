from chord import *

class Music(object):
    melody = []
    chordprogression = []
    rhythm = []
    def __init__(self,title,composer,key_signature,metre,arranger=''):
        self.title = title
        self.composer = composer
        self.arranger = arranger
        self.key = key
        self.metre = metre

    def add_subtitle(self,subtitle):
        self.subtitle = subtitle
    def add_chordprogression(self,chordprogression):
        self.chordprogression = chordprogression
    def add_category(self,categorys):
        self.categorys = categorys
