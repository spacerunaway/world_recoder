from note import *

interval = {'P1':0,'m2':1,'M2':2,'m3':3,'M3':4,'P4':5,'A4':6,'d5':6,'P5':7,'A5':8,
'm6':8,'M6':9,'d7':9,'m7':10,'M7':11,'P8':12,'m9':13,'M9':14,'m10':15,'M10':16,'P11':17,
'd12':18,'A11':18,'P12':19,'m13':20,'M13':21,'m14':22,'M14':23,'P15':24}

class Scale(object):
    name = 'UnknowScale'
    interval_keys = []
    members = []
    def __init__(self,interval_keys):
        self.intervals = self.find_intervals(interval_keys)
    def __repr__(self):
        return '{0}: {1}'.format(self.name, self.intervals)
    def find_interval(self,key):
        """
        find interval value by single key

        >>> s = Scale([])
        >>> s.find_interval('P1')
        0
        >>> s.find_interval('P15')
        24
        >>> s.find_interval('d12')
        18
        >>> s.find_interval('A11')
        18
        >>> s.find_interval('A3')
        """
        return interval.get(key)
    def find_intervals(self,keys):
        """
        find interval values by keys

        >>> s = Scale([])
        >>> s.find_intervals(['P1','P15','M6','d7','A3'])
        [0, 24, 9, 9]
        """
        return [interval.get(i) for i in keys if i in interval]
    def find_interval_keys(self,value):
        """
        find interval keys by its value

        >>> s = Scale([])
        >>> s.find_interval_keys(0)
        ['P1']
        >>> s.find_interval_keys(24)
        ['P15']
        >>> s.find_interval_keys(18)
        ['d12', 'A11']
        >>> s.find_interval_keys(-1)
        []
        """
        return [k for k,v in interval.items() if v == value]
    def start_with(self,note):
        """
        """
        assert note in self.roots,'start note must in {0}'.format(self.roots)
        index = STRINGS.index(note)
        try:
            self.members = [STRINGS[index+i] for i in self.intervals]
        except IndexError:
            print("can't make scale/chord start with {0}".format(note))

class Major_Scale(Scale):
    name = 'MajorScale'
    interval_keys = ['P1','M2','M3','P4','P5','M6','M7','P8']
    def __init__(self,roots):
        Scale.__init__(self,self.interval_keys)
        self.roots = roots

class Nutural_minor_Scale(Scale):
    name = 'Nutural_minor_Scale'
    interval_keys = ['P1','M2','m3','P4','P5','m6','m7','P8']

class Harmonic_minor_Scale(Scale):
    name = 'Harmonic_minor_Scale'
    interval_keys = ['P1','M2','m3','P4','P5','m6','M7','P8']

class Melodic_minor_Scale(Scale):
    name = 'Melodic_minor_Scale'
    interval_keys = ['P1','M2','m3','P4','P5','M6','M7','P8','m7','m6','P5','P4','m3','M2','P1']

class minor_Scale(Nutural_minor_Scale,Harmonic_minor_Scale,Melodic_minor_Scale):
    name = 'minor_Scale'
    def __init__(self,roots):
        Nutural_minor_Scale.__init__(self,Nutural_minor_Scale.interval_keys)
        self.nutural_intervals = self.intervals[:]
        Harmonic_minor_Scale.__init__(self,Harmonic_minor_Scale.interval_keys)
        self.harmonic_intervals = self.intervals[:]
        Melodic_minor_Scale.__init__(self,Melodic_minor_Scale.interval_keys)
        self.melodic_intervals = self.intervals[:]
        self.roots = roots
        self.form = {'nutural':self.nutural_intervals,'harmonic':self.harmonic_intervals,'melodic':self.melodic_intervals}
    def start_with(self,note,formation):
        assert note in self.roots
        index = STRINGS.index(note)
        self.members = [STRINGS[index+i] for i in self.form[formation]]
    def __repr__(self):
        str_n = '{0}: {1}'.format(Nutural_minor_Scale.name, self.nutural_intervals)
        str_h = '{0}: {1}'.format(Harmonic_minor_Scale.name, self.harmonic_intervals)
        str_m = '{0}: {1}'.format(Melodic_minor_Scale.name, self.melodic_intervals)
        return '{0}\n{1}\n{2}'.format(str_n,str_h,str_m)

c_major = Major_Scale(do)
c_major.start_with(C4)
c_minor = minor_Scale(do)
c_minor.start_with(C4,'nutural')
