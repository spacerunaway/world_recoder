from utils import *

def link_chords(chordprogression):
    """
    Chord progression is a sequences of chords.
    Make a LinkedList for chords.

    >>> c_p1 = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> l1 = link_chords(c_p1)
    >>> l1
    start -> C -> Am -> F -> G -> C -> Am -> F -> G7 -> end
    >>> l2 = link_chords(c_p2)
    >>> l2
    {'start': {'C': 1}, 'C': {'Am': 2, 'D': 1}, 'Am': {'F': 2}, 'F': {'G': 2}, 'G': {'C': 1, 'Em': 1, 'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    >>> c_p3 = [C_Major,C_Major,START,'C',END,START,START,END,'F',G_Major]
    >>> l3 = link_chords(c_p3)
    >>> l3
    {'start': {'C': 1, 'start': 1, 'end': 1}, 'C': {'end': 1}, 'end': {'start': 1, 'F': 1}}
    """
    key = None
    prev = LinkedChord(None,key,START)
    for item in chordprogression:
        if type(item) is Key:
            key = item
        else:
            chord = LinkedChord(CHORD[item],key,item)
            prev.append(chord)
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
