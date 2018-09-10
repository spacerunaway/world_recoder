MAX_KEYBOARD = 88
ALL_NOTE = {'C':3,'C♯':4,'D♭':4,'D':5,'D♯':6,'E♭':6,'E':7,'F':8,'F♯':9,'G♭':9,
'G':10,'G♯':11,'A♭':11,'A':0,'A♯':1,'B♭':1,'B':2}
interval = {'P1':0,'m2':1,'M2':2,'m3':3,'M3':4,'P4':5,'A4':6,'d5':6,'P5':7,'m6':8,'M6':9,'m7':10,'M7':11,'P8':12,
'm9':13,'M9':14,'m10':15,'M10':16,'P11':17,'d12':18,'A11':18,'P12':19,'m13':20,'M13':21,'m14':22,'M14':23,'P15':24}
R = pow(2,1.0/12.0)

class Note(object):
    def __init__(self,name,pitch,num=0,hz=0):
        self.name = name
        self.pitch = pitch
        self.num = num
        self.Hz = hz
    def __repr__(self):
        return '{0}{1}'.format(self.name,self.pitch)

def make_piano():
    """make piano's keyboard use Note class

    >>> n = make_piano()[-1]
    >>> n.num
    88
    >>> n.pitch
    8
    >>> n
    C8
    >>> n.Hz < 4186.010 and n.Hz > 4186.009
    True
    """
    names,pitch,hz = ['A'],0,27.5
    piano = []
    for i in range(MAX_KEYBOARD):
        piano.append(Note(names,pitch,i+1,hz))
        names = [note for note in ALL_NOTE if ALL_NOTE[note] == (i+1) % 12]
        pitch = (i + 10) // 12
        hz = hz * R
    return piano

PIANO = make_piano()

class Scale(object):
    name = 'UnknowScale'
    def __init__(self,interval_keys):
        self.intervals = self.find_intervals(interval_keys)
    def __repr__(self):
        return '{0}: {1}'.format(self.name, self.intervals)
    def find_intervals(self,keys):
        return [interval[i] for i in interval if i in keys]
class Major_Scale(Scale):
    name = 'MajorScale'
    interval_keys = ['P1','M2','M3','P4','P5','M6','M7','P8']
    def __init__(self,roots):
        Scale.__init__(self,self.interval_keys)
        self.roots = roots
    def start_with(self,note,instrument):
        assert note in self.roots and note in instrument
        index = instrument.index(note)
        self.members = [instrument[index+i] for i in self.intervals]

class Key(object):
    def __init__(self,name,scale,relationkeys={}):
        self.name = name
        self.scale = scale
        self.rootkey = scale[0]
        self.relationkeys = relationkeys
    def cul_relationkeys(self):
        self.domi_key = transposition(self,7,1)
        self.subd_key = transposition(self,-7,1)
        self.rela_key = transposition(self,-3,-1)
        self.para_key = transposition(self,0,-1)

class Chord(object):
    c_type = 'triad'
    def __init__(self,name,rootnote,p_intervals):
        self.name = name
        self.root = rootnote
        self.bass = rootnote
        self.p_intervals = [p_i for p_i in p_intervals if type(p_i) == int]
        self.notes = find_notes(rootnote,p_intervals)
        self.component = make_component(self.notes)
    def __repr__(self):
        return '{0}'.format(self.name)

    def get_c_form(self,n):
        assert n < len(self.pitches)
        self.rootkey = self.pitches[n]
    def add9(self):
        n = self.root.num + 14
        while (n <= MAX_KEYBOARD):
            self.p_intervals.append(n)
            n += 12
        self.notes = find_notes(rootnote,p_intervals)
        self.component = make_component(self.notes)
class Chord7th(Chord):
    c_type = '7th'

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
