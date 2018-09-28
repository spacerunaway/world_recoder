from utils import *

class Linked_Chord(object):
    def __init__(self,chord, key, p=None, n=None):
        self.chord = chord
        self.key = key
        self.prev = p
        self.next = n
        # self.prediction = f(p,n) #for ML
    def appendChord(self,chord):

    def insertChord(self,chord,start=0):

    def deleteChord(self,chord,start=0):

    def size(self):

    def find(self,num):

    def clear(self):
    """ Memories clear not necessary in python? """

    def display(self):
    """ View of Linked_Chord """

def link_chords(chordprogression):
    key = None
    prev = Linked_Chord(None,key)
    for item in chordprogression:
        if type(item) is Key:
            key = item
        else:
            chord = Linked_Chord(CHORD[item],key)
            prev.appendChord(chord)
            prev = chord

def parse_chordprogression(chordprogression):
    link_chords(chordprogression)
    cpd(chordprogression)

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
