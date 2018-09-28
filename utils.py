from scale_data import *
from chord_data import *
START = 'start'
END = 'end'

def complete_keys_triad():
    return
def cpd(chord_p):
    """
    Handle music is similar to natural language processing.
    chord_progression_dict(cpd) is think music chord progression like words in sentence.
    counting next chord on chord progression.

    >>> c_p = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> d = cpd(c_p)
    >>> d
    {'start': {'C': 1}, 'C': {'Am': 2}, 'Am': {'F': 2}, 'F': {'G': 1, 'G7': 1}, 'G': {'C': 1}, 'G7': {'end': 1}}
    >>> d2 = cpd(c_p2)
    >>> d2
    {'start': {'C': 1}, 'C': {'Am': 2, 'D': 1}, 'Am': {'F': 2}, 'F': {'G': 2}, 'G': {'C': 1, 'Em': 1, 'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    >>> c_p3 = [C_Major,C_Major,START,'C',END,START,START,END,'F',G_Major]
    >>> d3 = cpd(c_p3)
    >>> d3
    {'start': {'C': 1, 'start': 1, 'end': 1}, 'C': {'end': 1}, 'end': {'start': 1, 'F': 1}}
    """
    res = dict()
    chord_p = [chord_name for chord_name in chord_p if type(chord_name) is str]
    i = 0
    while i < len(chord_p)-1:
        if chord_p[i] not in res.keys():
            res[chord_p[i]] = {}
        if chord_p[i+1] not in res[chord_p[i]].keys():
            res[chord_p[i]][chord_p[i+1]] = 1
        else:
            res[chord_p[i]][chord_p[i+1]] += 1
        i += 1
    return res

def sum_cpds(cpds):
    """
    sum chord_progression_dict(cpd) for analysis some trend of composer, genre, age, or theory.

    >>> c_p = [START,C_Major,'C','Am','F','G','C','Am','F','G7',END]
    >>> c_p2 = [START,C_Major,'C','Am','F','G','C','Am','F','G',G_Major,'Em','C','D','D7','G',END]
    >>> d = cpd(c_p)
    >>> d
    {'start': {'C': 1}, 'C': {'Am': 2}, 'Am': {'F': 2}, 'F': {'G': 1, 'G7': 1}, 'G': {'C': 1}, 'G7': {'end': 1}}
    >>> d2 = cpd(c_p2)
    >>> d2
    {'start': {'C': 1}, 'C': {'Am': 2, 'D': 1}, 'Am': {'F': 2}, 'F': {'G': 2}, 'G': {'C': 1, 'Em': 1, 'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    >>> sum_d = sum_cpds([d,d2])
    >>> sum_d
    {'start': {'C': 2}, 'C': {'Am': 4, 'D': 1}, 'Am': {'F': 4}, 'F': {'G': 3, 'G7': 1}, 'G': {'C': 2, 'Em': 1, 'end': 1}, 'G7': {'end': 1}, 'Em': {'C': 1}, 'D': {'D7': 1}, 'D7': {'G': 1}}
    """
    sum_result = {}
    for item in cpds:
        sum_2_cpds(item,sum_result)
    return sum_result

def sum_2_cpds(cpd_a,cpd_b):
    """
    Sum 2 dicts of cpd and store the result in the second parameter
    assistant to sum_cpds(List_of_dics)
    """
    for item in cpd_a.keys():
        if item not in cpd_b.keys():
            cpd_b[item] = dict(cpd_a[item])
        else:
            for chords in cpd_a[item].keys():
                if chords not in cpd_b[item].keys():
                    cpd_b[item][chords] = cpd_a[item][chords]
                else:
                    cpd_b[item][chords] += cpd_a[item][chords]
    return cpd_b


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

def parse_cpd_as_TSD(cpd):
    """
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
