MAX_KEYBOARD = 88
ALL_NOTE = {'C':3,'C♯':4,'D♭':4,'D':5,'D♯':6,'E♭':6,'E':7,'F':8,'F♯':9,'G♭':9,
'G':10,'G♯':11,'A♭':11,'A':0,'A♯':1,'B♭':1,'B':2}
interval = {'P1':0,'m2':1,'M2':2,'m3':3,'M3':4,'P4':5,'A4':6,'d5':6,'P5':7,'m6':8,'M6':9,'m7':10,'M7':11,'P8':12,
'm9':13,'M9':14,'m10':15,'M10':16,'P11':17,'d12':18,'A11':18,'P12':19,'m13':20,'M13':21,'m14':22,'M14':23,'P15':24}
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
def find_notes(root,p_intervals):
    """find note start with rootnote and the sequence of pitches interval

    >>> chord_c = Chord(['do','mi','so'],'C')
    >>> chord_c7 = Chord7th(['do','mi','so','si'],'C7')
    >>> ischord(chord_c)
    True
    >>> ischord(chord_c7)
    True
    >>> ischord('C')
    False
    """
def make_component(notes):
    """find the component of notes return component list

    >>> chord_c = Chord(['do','mi','so'],'C')
    >>> chord_c7 = Chord7th(['do','mi','so','si'],'C7')
    >>> ischord(chord_c)
    True
    >>> ischord(chord_c7)
    True
    >>> ischord('C')
    False
    """
