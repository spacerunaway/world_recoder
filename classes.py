MAX_KEYBOARD = 88
ALL_NOTE = {'C':3,'C♯':4,'D♭':4,'D':5,'D♯':6,'E♭':6,'E':7,'F':8,'F♯':9,'G♭':9,
'G':10,'G♯':11,'A♭':11,'A':0,'A♯':1,'B♭':1,'B':2}
R = pow(2,1.0/12.0)

class ChordProgression:
    def __init__(self,key,chord_list=[]):
        self.key = key
        self.chord_list = [chord for chord in chord_list if ischord(chord)]
    def __repr__(self):
        return 'key:{0} 和音進行:{1}'.format(self.key,self.chord_list)
    def add_chord(self,chords):
        append_list = [chord for chord in chords if ischord(chord)]
        self.chord_list += append_list

class Music(object):
    def __init__(self,title,composer,key,metre,arranger=''):
        self.title = title
        self.composer = composer
        self.arranger = arranger
        self.key = key
        self.metre = metre

    def add_subtitle(self,subtitle):
        self.subtitle = subtitle
    def add_chordprogression(self,chordprogression):
        assert type(chordprogression) == ChordProgression
        self.chordprogression = chordprogression
    def add_chord_dict(self,chord_dict):
        assert type(chord_dict) == dict
        self.chord_dict = chord_dict
    def add_category(self,categorys):
        assert type(categorys) == list
        self.categorys = categorys

def ischord(chord):
    """check chord classes

    >>> chord_c = Chord(['do','mi','so'],'C')
    >>> chord_c7 = Chord7th(['do','mi','so','si'],'C7')
    >>> ischord(chord_c)
    True
    >>> ischord(chord_c7)
    True
    >>> ischord('C')
    False
    """
    return type(chord) == Chord or type(chord) == Chord7th

def find_note(notename,pitch=0):
    """find notename and pitch in PIANO return Note

    >>> find_note('C',4)
    C4
    >>> find_note('A♯',0).num
    2
    >>> find_note('C').num
    4
    """
    if pitch > 0:
        pitch -=1
    num = ALL_NOTE[notename] + 12 * pitch
    return PIANO[num]
