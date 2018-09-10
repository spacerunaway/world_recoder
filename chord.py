from scale import *

class Chord(Scale):
    name = 'UnknowChord'
    interval_keys = ['P1']
    def __init__(self,roots):
        Scale.__init__(self,self.interval_keys)
        self.roots = roots
        self.bases = roots
    def __repr__(self):
        str_name = '{0}: {1}'.format(self.name, self.intervals)
        str_members = ''
        if hasattr(self,'bass'):
            str_members = '\n{0} on {1}'.format(self.members, self.bass)
        return '{0}{1}'.format(str_name, str_members)

    def add(self,intervals):
        name = self.name + '_add' + ''.join([i[1:] for i in intervals])
        self.extend_chord(self.interval_keys+intervals, name)
        return self

    def aug(self,keys):
        for key in keys:
            assert key in interval_keys
        self.extend_chord(self.interval_keys+keys, self.name)
        return self

    def add(self,intervals):
        name = self.name + '_add' + ''.join([i[1:] for i in intervals])
        self.extend_chord(self.interval_keys+intervals, name)
        return self
    def on(self,bases):
        self.bases = bases

    def set_bass(self,note):
        assert note in self.bases
        self.bass = note

    def start_with(self,note,bass=None):
        Scale.start_with(self,note)
        if bass is None:
            self.set_bass(note)
        else:
            self.set_bass(bass)

    def extend_chord(self,interval_keys,name):
        self.name = name
        self.interval_keys = interval_keys
        self.intervals = self.find_intervals(self.interval_keys)
        if self.members:
            self.start_with(self.members[0],self.bass)

class Major_Triad(Chord):
    name = 'Major_Triad'
    interval_keys = ['P1','M3','P5']
    def dominant_seventh(self):
        self.extend_chord(self.interval_keys+['m7'],'Dominant_seventh')
        return self
    def major_seventh(self):
        self.extend_chord(self.interval_keys+['M7'],'Major_seventh')
        return self
    def sixth(self):
        self.extend_chord(self.interval_keys+['M6'],'Major_sixth')
        return self
    def dominant_ninth(self):
        self.dominant_seventh()
        self.extend_chord(self.interval_keys+['M9'],'Dominant_ninth')
        return self
    def dominant_eleventh(self):
        self.dominant_ninth()
        self.extend_chord(self.interval_keys+['P11'],'Dominant_ninth')
        return self
    def dominant_thirteenth(self):
        self.dominant_eleventh()
        self.extend_chord(self.interval_keys+['M13'],'Dominant_ninth')
        return self
    def sus2(self):
        self.name = "suspended_second"
        self.interval_keys[1] = 'M2'
        self.intervals = self.find_intervals(self.interval_keys)
        return self
    def sus4(self):
        self.name = "suspended_fourth"
        self.interval_keys[1] = 'P4'
        self.intervals = self.find_intervals(self.interval_keys)
        return self
class Minor_Triad(Chord):
    name = 'minor_Triad'
    interval_keys = ['P1','m3','P5']
    def seventh(self):
        self.extend_chord(self.interval_keys+['m7'],'minor_seventh')
        return self
    def major_seventh(self):
        self.extend_chord(self.interval_keys+['M7'],'minor_major_seventh')
        return self
    def sixth(self):
        self.extend_chord(self.interval_keys+['M6'],'minor_sixth')
        return self

class Aug_Triad(Chord):
    name = 'Aug_Triad'
    interval_keys = ['P1','M3','A5']
    def seventh(self):
        self.extend_chord(self.interval_keys+['m7'],'Augmented_seventh')
        return self
    def major_seventh(self):
        self.extend_chord(self.interval_keys+['M7'],'Augmented_major_seventh')
        return self

class Dim_Triad(Chord):
    name = 'dim_Triad'
    interval_keys = ['P1','m3','d5']
    def seventh(self):
        self.extend_chord(self.interval_keys+['d7'],'diminished_seventh')
        return self
    def half_seventh(self):
        self.extend_chord(self.interval_keys+['m7'],'Half-diminished_seventh')
        return self

CM = Major_Triad(do)
Cm = Minor_Triad(do)
Caug = Aug_Triad(do)
Cdim = Cmb5 = Dim_Triad(do)
Cdim7 = Dim_Triad(do).seventh()
Cm7b5 = Dim_Triad(do).half_seventh()
Cm7 = Minor_Triad(do).seventh()
CmM7 = Minor_Triad(do).major_seventh()
Cm6 = Minor_Triad(do).sixth()
Cdom7 = Major_Triad(do).dominant_seventh()
CM7 = Major_Triad(do).major_seventh()
CM6 = Major_Triad(do).sixth()
Caug7 = Aug_Triad(do).seventh()
CaugM7 = Aug_Triad(do).major_seventh()
Cdom9 = Major_Triad(do).dominant_ninth()
Cdom13 = Major_Triad(do).dominant_thirteenth()
Cdom11 = Major_Triad(do).dominant_eleventh()
Cadd9 = Major_Triad(do).add(['M9'])
Cadd11 = Major_Triad(do).add(['P11'])
C69 = Major_Triad(do).add(['M6','M9'])
Csus2 = Major_Triad(do).sus2()
Csus4 = Major_Triad(do).sus4()
