import sys
sys.path.append('../utils')
from utils import *
from doubly_linkedlist import *

def link_chords(chordprogression):
    """
    Chord progression is a sequences of chords.
    A valid linked_chords can be one of the following:
    1: the chord name(str) in CHORD dict
    2: the key(type Key)
    and a music have to a signal of start and end.
    
    >>> c_p1 = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> l1 = link_chords(c_p1)
    >>> l1
    start - C - Am - F - G - C - Am - F - G7 - end
    >>> l2 = link_chords(c_p2)
    >>> l2
    start - C - Am - F - G - C - Am - F - G - Em - C - D - D7 - G - end
    >>> l2[8].key is C_Major
    True
    >>> l2[8].chord == CHORD['G']
    True
    >>> l2[9].key is G_Major
    True
    >>> l2[9].chord == CHORD['Em']
    True
    >>> c_p3 = [C_Major,C_Major,START,'C',END,START,START,END,'F',G_Major]
    >>> l3 = link_chords(c_p3)
    >>> l3
    start - C - end - start - start - end - F
    """
    key = None
    res = LinkedList()
    for item in chordprogression:
        if type(item) is Major_Scale or type(item) is minor_Scale:
            key = item
        else:
            if item not in CHORD:
                chord = item
            else:
                chord = CHORD[item]
            node = LinkedChord(chord,key,item)
            res.append(node)
    return res
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
