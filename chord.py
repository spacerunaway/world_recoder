from scale import *

class Chord(Scale):
    """
    A chord is any harmonic set of pitches consisting of two or more (usually three or more) notes
    (also called "pitches") that are heard as if sounding simultaneously.
    (For many practical and theoretical purposes, arpeggios and broken chords,
    or sequences of chord tones, may also be considered as chords.)
    """
    name = 'UnknowChord'
    interval_keys = []
    def __init__(self,roots):
        Scale.__init__(self,self.interval_keys[:])
        self.roots = roots
        self.bases = roots
    def __repr__(self):
        str_name = '{0}: {1}'.format(self.name, self.intervals)
        str_members = ''
        if hasattr(self,'bass'):
            str_members = '\n{0} on {1}'.format(self.members, self.bass)
        return '{0}{1}'.format(str_name, str_members)

    def add(self,intervals):
        """
        An added tone chord is a triad chord with an added, non-tertian note,
        such as the commonly added sixth as well as chords with an added
        ninth(second) or eleventh (fourth) or a combination of the three.

        >>> CM = Major_Triad(do)
        >>> CM.add(['M9'])
        >>> CM
        Major_Triad_add9: [0, 4, 7, 14]
        >>> CM.default()
        >>> CM.add([])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM.add(['M6','M9'])
        >>> CM.add(['P11'])
        >>> CM
        Major_Triad_add6_add9_add11: [0, 4, 7, 9, 14, 17]
        """
        new_name = self.name + ''.join(['_add' + i[1:] for i in intervals])
        self.extend_chord(self.interval_keys+intervals, new_name)

    def aug(self,keys):
        """
        Augmented diatonic scale tone of chords, in broadest definition it will be an altered chord.
        An altered chord is a chord with one or more notes from the diatonic scale
        replaced by a neighboring pitch in the chromatic scale. Thus the note must be a nonchord tone.

        >>> CM = Major_Triad(do)
        >>> CM.aug(['P5'])
        >>> CM
        Major_Triad_aug5: [0, 4, 8]
        >>> CM.default()
        >>> CM.aug([])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM.aug(['M9'])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM.add(['M9'])
        >>> CM.aug(['M9'])
        >>> CM
        Major_Triad_add9_aug9: [0, 4, 7, 15]
        >>> CM.aug(['M9'])
        >>> CM
        Major_Triad_add9_aug9: [0, 4, 7, 15]
        """
        new_interval_keys = self.interval_keys
        new_name = self.name
        for key in [k for k in keys if k in self.interval_keys[:]]:
            distance = self.find_interval(key)
            new_key = self.find_interval_keys(distance + 1)
            new_interval_keys = [new_key[0] if i == key else i for i in self.interval_keys[:]]
            new_name = self.name + ''.join(['_aug' + i[1:] for i in keys])
        self.extend_chord(new_interval_keys, new_name)

    def dim(self,keys):
        """
        diminished diatonic scale tone of chords, refer to aug()

        >>> CM = Major_Triad(do)
        >>> CM.dim(['P5'])
        >>> CM
        Major_Triad_dim5: [0, 4, 6]
        >>> CM.default()
        >>> CM.dim([])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM.dim(['M9'])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM.add(['M9'])
        >>> CM.dim(['M9'])
        >>> CM
        Major_Triad_add9_dim9: [0, 4, 7, 13]
        >>> CM.dim(['M9'])
        >>> CM
        Major_Triad_add9_dim9: [0, 4, 7, 13]
        """
        new_interval_keys = self.interval_keys
        new_name = self.name
        for key in [k for k in keys if k in self.interval_keys[:]]:
            distance = self.find_interval(key)
            new_key = self.find_interval_keys(distance - 1)
            new_interval_keys = [new_key[0] if i == key else i for i in self.interval_keys[:]]
            new_name = self.name + ''.join(['_dim' + i[1:] for i in keys])
        self.extend_chord(new_interval_keys, new_name)

    def invertion(self,bass):
        """
        There are inverted chords, inverted melodies, inverted intervals,and (in counterpoint) inverted voices.
        The concept of inversion also plays a role in musical set theory.

        An interval is inverted by raising or lowering either of the notes using displacement of
        the octave (or octaves) so that both retain their names (pitch class).
        For example, the inversion of an interval consisting of a C with an E above
        it is an E with a C above it – to work this out, the C may be moved up,
        the E may be lowered, or both may be moved.

        Under inversion, perfect intervals remain perfect, major intervals become minor and vice versa,
        augmented intervals become diminished and vice versa.
        """

        """ add your code """
    def on(self,bases):
        """
        On chord is an inverted chords. For example C Major chord(C,E,G) on G means
        its bass note is G called ConG(G,C,E) is the first invertion of C.
        But there are some extra version like ConF(F,C,E,G)
        We called it extra invertion different to normal invertion.
        """
        self.bases = bases

    def set_bass(self,note):
        """
        Set the bass note, it must be the lowest tone in the chord
        """
        if note in self.bases:
            self.bass = note
            """ add your code """
        else:
            print("bass must be the lowest tone")

    def start_with(self,note,bass=None):
        """
        make chord from any note.
        (e.g. major triad start with C4 is [C4,E4,G4] are chord C,
        major triad start with D4 is [D4,Fs4,A4] are chord D,
        dominant seventh start with C4 and the bass is G3 means [G3,C4,E4,G4,As4] are chord C7onG.)
        """
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
    def default(self):
        self.extend_chord(Major_Triad.interval_keys,Major_Triad.name)
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
Cadd9 = Major_Triad(do)
Cadd9.add(['M9'])
Cadd11 = Major_Triad(do)
Cadd11.add(['P11'])
C69 = Major_Triad(do)
C69.add(['M6','M9'])
Csus2 = Major_Triad(do).sus2()
Csus4 = Major_Triad(do).sus4()
