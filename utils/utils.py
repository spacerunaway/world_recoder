import sys
sys.path.append('../data')
from scale_data import *
from chord_data import *

def complete_keys_triad():
    return

def cpdict(cp):
    """
    Handle music is similar to natural language processing.
    chord_progression_dict(cpdict) is think music chord progression like words in sentence.
    counting next chord on chord progression.

    >>> c_p = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> d = cpdict(c_p)
    >>> d
    {'start': {'C': 1}, 'C': {'Am': 2}, 'Am': {'F': 2}, 'F': {'G': 1, 'G7': 1}, 'G': {'C': 1}, 'G7': {'end': 1}}
    >>> d2 = cpdict(c_p2)
    >>> d2
    {'start': {'C': 1}, 'C': {'Am': 2, 'D': 1}, 'Am': {'F': 2}, 'F': {'G': 2}, 'G': {'C': 1, 'Em': 1, 'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    >>> c_p3 = [C_Major,C_Major,START,'C',END,START,START,END,'F',G_Major]
    >>> d3 = cpdict(c_p3)
    >>> d3
    {'start': {'C': 1, 'start': 1, 'end': 1}, 'C': {'end': 1}, 'end': {'start': 1, 'F': 1}}
    """
    res = dict()
    cp = [chord_name for chord_name in cp if type(chord_name) is str]
    i = 0
    while i < len(cp)-1:
        if cp[i] not in res.keys():
            res[cp[i]] = {}
        if cp[i+1] not in res[cp[i]].keys():
            res[cp[i]][cp[i+1]] = 1
        else:
            res[cp[i]][cp[i+1]] += 1
        i += 1
    return res

def down(name,higher):
    """
    return a name that not contain higher str

    >>> s = 'Cadd9'
    >>> higher = list('add','^','9','11','13')
    >>> down(s,higher)
    'C'
    >>> s = 'add9'
    >>> down(s,higher)
    ''
    >>> s = 'Caug7add9add11^C'
    >>> down(s,higher)
    'Caug7'
    >>> s = 'start'
    >>> down(s,higher)
    'start'
    """
    if type(name) is not str:
        return name
    while name in higher:
        name = name[0:-1] #not work need two pointor
    return name

def nontension_cpdict(cp):
    """
    return a chord progression that reduce the dimension of tension chrods(e.g. add9,^G,69)
    Tension -- any note that interval over perfect 8(octave)

    >>> c_p = [START,C_Major,'ConG','AmonC','Fadd9','G^F','C69','AmM7','F6','G7','G11','BsaugM7','BsaugM7add11',END]
    >>> ntcp = nontension_cpdict(c_p)
    >>> c_p
    [START,C_Major,'ConG','AmonC','F','G','C6','AmM7','F6','G7','G7','BsaugM7','BsaugM7',END]
    """
    nontension_cp = []
    for chord_name in cp:
        if type(chord_name) is str and chord_name in CHORD:
            if CHORD[chord_name].isdominant:
                chord_name = chord_name.replace("9", "7").replace("11", "7").replace("13", "7")
        nontension_cp.append(chord_name)
    higher = list('add','^','9','11','13')
    return [down(chord_name,higher) for chord_name in nontension_cp]

def nonbass_cpdict(cp):
    """
    return a chord progression that reduce the dimension of on-bass chord(e.g. onE)
    oon-bass -- on-bass chord can be one or both of the following:
                1: the invertion of the chord (ConG)
                2: the bass note on the chord (ConF F isn't contain in C)

    >>> c_p = [START,C_Major,'ConG','AmonC','Fadd9','G^F','C69','AmM7','F6','G7','G11','BsaugM7','BsaugM7add11',END]
    >>> c_p = nontension_cpdict(c_p)
    >>> c_p
    [START,C_Major,'C','Am','Fadd9','G^F','C69','AmM7','F6','G7','G11','BsaugM7','BsaugM7add11',END]
    """
    higher = list('on')
    return [down(chord_name,higher) for chord_name in cp]

def sum_dicts(dicts,sumfx):
    """
    sum two or more dict use given sumfx function.
    the sumfx is a two argument function
    usage:
      sum chord progression dict(cpdict) for analysis some trend of composer, genre, age, or theory.

    >>> c_p = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> d = cpdict(c_p)
    >>> d
    {'start': {'C': 1}, 'C': {'Am': 2}, 'Am': {'F': 2}, 'F': {'G': 1, 'G7': 1}, 'G': {'C': 1}, 'G7': {'end': 1}}
    >>> d2 = cpdict(c_p2)
    >>> d2
    {'start': {'C': 1}, 'C': {'Am': 2, 'D': 1}, 'Am': {'F': 2}, 'F': {'G': 2}, 'G': {'C': 1, 'Em': 1, 'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    >>> sum_d = sum_dicts([d,d2,d],sum_2_cpdicts)
    >>> sum_d
    {'start': {'C': 3}, 'C': {'Am': 6, 'D': 1}, 'Am': {'F': 6}, 'F': {'G': 4, 'G7': 2}, 'G': {'C': 3, 'Em': 1, 'end': 1}, 'G7': {'end': 2}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    """
    sum_result = {}
    for item in dicts:
        sumfx(item,sum_result)
    return sum_result

def sum_2_cpdicts(cpdict_a,cpdict_b):
    """
    Sum 2 dicts of cpdict and store the result in the second parameter
    """
    for item in cpdict_a.keys():
        if item not in cpdict_b.keys():
            cpdict_b[item] = dict(cpdict_a[item])
        else:
            for chords in cpdict_a[item].keys():
                if chords not in cpdict_b[item].keys():
                    cpdict_b[item][chords] = cpdict_a[item][chords]
                else:
                    cpdict_b[item][chords] += cpdict_a[item][chords]
    return cpdict_b


def summary_as_triad(d):
    """
    Cadd9 -> C
    CM7 -> C
    C7 -> C7
    Cm -> Cm
    Caug7 -> Caug
    Cm6 -> Cm
    ConG -> C
    """

def summary_chord_type(d):
    """
    C -> traid
    ConG -> traid onchord
    Cm -> traid
    Caug -> traid
    Cdim -> traid
    C7 -> dominant seventh
    CM7 -> seventh
    Cadd9 -> tension
    C69 -> tension sixth
    Cmb5 -> dominant
    C7sus4 -> suspend dominant seventh
    """

def parse_cpdict_as_TSD(cpdict):
    """
    Chords has some role in their scale(key) like Tonic,Subdominant,Dominant
    I = T
    II = S
    III = T
    IV = S
    V = D
    V7 = D
    I2 -> V7 = D
    VI = T
    VII = D
    others = EXTRA
    [T - S - D - T - E - S -D]
    """

def parse_chord_distance():
    """
    C in C_Major distance is 0
    Dm in C_Major distance is 0
    D in C_Major distance is 1
    """
