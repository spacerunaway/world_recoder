from scale import *
import copy

class Chord(Scale):
    """
    A chord is any harmonic set of pitches consisting of two or more (usually three or more) notes
    (also called "pitches") that are heard as if sounding simultaneously.
    (For many practical and theoretical purposes, arpeggios and broken chords,
    or sequences of chord tones, may also be considered as chords.)
    """
    name = 'UnknowChord'
    interval_keys = []
    roots = None
    bases = None
    def __init__(self,roots=None):
        Scale.__init__(self,self.interval_keys[:])
        self.roots = roots
        self.bases = roots
    def __repr__(self):
        str_name = '{0}: {1}'.format(self.name, self.intervals)
        str_members = ''
        if hasattr(self,'bass'):
            str_members = '\n{0} on {1}'.format(self.members, self.bass)
        return '{0}{1}'.format(str_name, str_members)
    def __eq__(self,y):
        if self.interval_keys != y.interval_keys:
            return False
        if self.roots != y.roots:
            return False
        return True
    def addroots(self,roots):
        self.roots = roots
        if self.bases is None:
            self.bases = roots

    def add(self,intervals):
        """
        An added tone chord is a triad chord with an added, non-tertian note,
        such as the commonly added sixth as well as chords with an added
        ninth(second) or eleventh (fourth) or a combination of the three.

        >>> CM = Major_Triad(do)
        >>> CM = CM.add(['M9'])
        >>> CM
        Major_Triad_add9: [0, 4, 7, 14]
        >>> CM.default()
        >>> CM = CM.add([])
        >>> CM
        Major_Triad: [0, 4, 7]
        >>> CM = CM.add(['M6','M9'])
        >>> CM = CM.add(['P11'])
        >>> CM = CM.add(['M6','M9'])
        >>> CM
        Major_Triad_add6_add9_add11: [0, 4, 7, 9, 14, 17]
        """
        if type(intervals) != list:
            return print('argument must be list')
        add_keys = [i for i in intervals if i not in self.interval_keys[:]]
        new_name = self.name + ''.join(['_add' + i[1:] for i in add_keys])
        self.rebuild_chord(self.interval_keys + add_keys, new_name)

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
        >>> CM = CM.add(['M9'])
        >>> CM.aug(['P5','M9'])
        >>> CM
        Major_Triad_add9_aug5_aug9: [0, 4, 8, 15]
        >>> CM.aug(['M9'])
        >>> CM
        Major_Triad_add9_aug5_aug9: [0, 4, 8, 15]
        """
        if type(keys) != list:
            return print('argument must be list')
        for key in [k for k in keys if k in self.interval_keys[:]]:
            distance = self.find_interval(key)
            new_key = self.find_interval_keys(distance + 1,'aug')
            self.interval_keys = [new_key if i == key else i for i in self.interval_keys[:]]
            self.name = self.name + ''.join('_aug' + key[1:])
        self.rebuild_chord(self.interval_keys, self.name)

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
        >>> CM = CM.add(['M9'])
        >>> CM.dim(['P5','M9'])
        >>> CM
        Major_Triad_add9_dim5_dim9: [0, 4, 6, 13]
        >>> CM.dim(['M9'])
        >>> CM
        Major_Triad_add9_dim5_dim9: [0, 4, 6, 13]
        """
        if type(keys) != list:
            return print('argument must be list')
        for key in [k for k in keys if k in self.interval_keys[:]]:
            distance = self.find_interval(key)
            new_key = self.find_interval_keys(distance - 1,'dim')
            self.interval_keys = [new_key if i == key else i for i in self.interval_keys[:]]
            self.name = self.name + ''.join('_dim' + key[1:])
        self.rebuild_chord(self.interval_keys, self.name)

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

    def rebuild_chord(self,interval_keys,name):
        self.name = name
        self.interval_keys = interval_keys
        self.intervals = self.find_intervals(self.interval_keys)
        if self.members:
            self.start_with(self.members[0],self.bass)

class Major_Triad(Chord):
    name = 'Major_Triad'
    interval_keys = ['P1','M3','P5']
    category = ['Major','Triad']
    def default(self):
        self.rebuild_chord(Major_Triad.interval_keys,Major_Triad.name)
    def add(self,intervals):
        new_chord = copy.copy(self)
        Chord.add(new_chord,intervals)
        return new_chord
    def dominant_seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Major_Triad.interval_keys+['m7']
        new_chord.rebuild_chord(interval_keys,'Dominant_seventh')
        return new_chord
    def major_seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Major_Triad.interval_keys+['M7']
        new_chord.rebuild_chord(interval_keys,'Major_seventh')
        return new_chord
    def sixth(self):
        new_chord = copy.copy(self)
        interval_keys = Major_Triad.interval_keys+['M6']
        new_chord.rebuild_chord(interval_keys,'Major_sixth')
        return new_chord
    def dominant_ninth(self):
        new_chord = self.dominant_seventh()
        interval_keys = new_chord.interval_keys+['M9']
        new_chord.rebuild_chord(interval_keys,'Dominant_ninth')
        return new_chord
    def dominant_eleventh(self):
        new_chord = self.dominant_ninth()
        interval_keys = new_chord.interval_keys+['P11']
        new_chord.rebuild_chord(interval_keys,'Dominant_eleventh')
        return new_chord
    def dominant_thirteenth(self):
        new_chord = self.dominant_eleventh()
        interval_keys = new_chord.interval_keys+['M13']
        new_chord.rebuild_chord(interval_keys,'Dominant_thirteenth')
        return new_chord
    def sus2(self):
        new_chord = copy.copy(self)
        self.interval_keys[1] = 'M2'
        new_chord.rebuild_chord(self.interval_keys,'Suspended_second')
        return new_chord
    def sus4(self):
        new_chord = copy.copy(self)
        self.interval_keys[1] = 'P4'
        new_chord.rebuild_chord(self.interval_keys,'Suspended_fourth')
        return new_chord

class Minor_Triad(Chord):
    name = 'minor_Triad'
    interval_keys = ['P1','m3','P5']
    def seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Minor_Triad.interval_keys+['m7']
        new_chord.rebuild_chord(interval_keys,'minor_seventh')
        return new_chord
    def major_seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Minor_Triad.interval_keys+['M7']
        new_chord.rebuild_chord(interval_keys,'minor_major_seventh')
        return new_chord
    def sixth(self):
        new_chord = copy.copy(self)
        interval_keys = Minor_Triad.interval_keys+['M6']
        new_chord.rebuild_chord(interval_keys,'minor_sixth')
        return new_chord
    def b5(self):
        new_chord = copy.copy(self)
        interval_keys = ['P1','m3','d5']
        new_chord.rebuild_chord(interval_keys,'minor_flat5')
        return new_chord
    def seventh_b5(self):
        new_chord = copy.copy(self)
        interval_keys = ['P1','m3','d5','m7']
        new_chord.rebuild_chord(interval_keys,'minor_seventh_flat5')
        return new_chord

class Aug_Triad(Chord):
    name = 'Aug_Triad'
    interval_keys = ['P1','M3','A5']
    def seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Aug_Triad.interval_keys+['m7']
        new_chord.rebuild_chord(interval_keys,'Augmented_seventh')
        return new_chord
    def major_seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Aug_Triad.interval_keys+['M7']
        new_chord.rebuild_chord(interval_keys,'Augmented_major_seventh')
        return new_chord

class Dim_Triad(Chord):
    name = 'dim_Triad'
    interval_keys = ['P1','m3','d5']
    def seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Dim_Triad.interval_keys+['d7']
        new_chord.rebuild_chord(interval_keys,'diminished_seventh')
        return new_chord
    def half_seventh(self):
        new_chord = copy.copy(self)
        interval_keys = Dim_Triad.interval_keys+['m7']
        new_chord.rebuild_chord(interval_keys,'diminished_seventh')
        return new_chord
