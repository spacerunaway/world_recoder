R = pow(2,1.0/12.0)
NOTE_DICT = {}
SOUND = {}

class Note(object):
    """
    In music, a note is the pitch and duration of a sound, and also its representation
    in musical notation (♪, ♩). A note can also represent a pitch class.
    Notes are the building blocks of much written music: discretizations of
    musical phenomena that facilitate performance, comprehension, and analysis.

    Two notes with fundamental frequencies in a ratio equal to any integer power of two
    (e.g., half, twice, or four times)are perceived as very similar.
    Because of that, all notes with these kinds of relations can be grouped under the same pitch class.
    """
    def __init__(self,name,pitch,num=0,hz=0):
        self.name = name
        self.pitch = pitch
        self.num = num
        self.Hz = hz
    def __repr__(self):
        return '{0}{1}'.format(self.name,self.pitch)

# definition all note
A0 = Gss0 = Bbb0 = Note('A',0,0,27.500)
As0 = Bb0 = Cbb0 = Note('Ais',0,1,A0.Hz*pow(R,1))
B0 = Cb1 = Ass0 = Note('B',0,2,A0.Hz*pow(R,2))
C1 = Bs0 = Dbb1 = Note('C',1,3,A0.Hz*pow(R,3))
Cs1 = Db1 = Bss0 = Note('Cis',1,4,A0.Hz*pow(R,4))
D1 = Css1 = Ebb1 = Note('D',1,5,A0.Hz*pow(R,5))
Ds1 = Eb1 = Fbb1 = Note('Dis',1,6,A0.Hz*pow(R,6))
E1 = Fb1 = Dss1 = Note('E',1,7,A0.Hz*pow(R,7))
F1 = Es1 = Gbb1 = Note('F',1,8,A0.Hz*pow(R,8))
Fs1 = Gb1 = Ess1 = Note('Fis',1,9,A0.Hz*pow(R,9))
G1 = Fss1 = Abb1 = Note('G',1,10,A0.Hz*pow(R,10))
Gs1 = Ab1 = Note('Gis',1,11,A0.Hz*pow(R,11))

A1 = Gss1 = Bbb1 = Note('A',1,12,A0.Hz*2)
As1 = Bb1 = Cbb1 = Note('Ais',1,13,As0.Hz*2)
B1 = Cb2 = Ass1 = Note('B',1,14,B0.Hz*2)
C2 = Bs1 = Dbb2 = Note('C',2,15,C1.Hz*2)
Cs2 = Db2 = Bss1 = Note('Cis',2,16,Cs1.Hz*2)
D2 = Css2 = Ebb2 = Note('D',2,17,D1.Hz*2)
Ds2 = Eb2 = Fbb2 = Note('Dis',2,18,Ds1.Hz*2)
E2 = Fb2 = Dss2 = Note('E',2,19,E1.Hz*2)
F2 = Es2 = Gbb2 = Note('F',2,20,F1.Hz*2)
Fs2 = Gb2 = Ess2 = Note('Fis',2,21,Fs1.Hz*2)
G2 = Fss2 = Abb2 = Note('G',2,22,G1.Hz*2)
Gs2 = Ab2 = Note('Gis',2,23,Gs1.Hz*2)

A2 = Gss2 = Bbb2 = Note('A',2,24,A1.Hz*2)
As2 = Bb2 = Cbb2 = Note('Ais',2,25,As1.Hz*2)
B2 = Cb3 = Ass2 = Note('B',2,26,B1.Hz*2)
C3 = Bs2 = Dbb3 = Note('C',3,27,C2.Hz*2)
Cs3 = Db3 = Bss2 = Note('Cis',3,28,Cs2.Hz*2)
D3 = Css3 = Ebb3 = Note('D',3,29,D2.Hz*2)
Ds3 = Eb3 = Fbb3 = Note('Dis',3,30,Ds2.Hz*2)
E3 = Fb3 = Dss3 = Note('E',3,31,E2.Hz*2)
F3 = Es3 = Gbb3 = Note('F',3,32,F2.Hz*2)
Fs3 = Gb3 = Ess3 = Note('Fis',3,33,Fs2.Hz*2)
G3 = Fss3 = Abb3 = Note('G',3,34,G2.Hz*2)
Gs3 = Ab3 = Note('Gis',3,35,Gs2.Hz*2)

A3 = Gss3 = Bbb3 = Note('A',3,36,A2.Hz*2)
As3 = Bb3 = Cbb3 = Note('Ais',3,37,As2.Hz*2)
B3 = Cb4 = Ass3 = Note('B',3,38,B2.Hz*2)
C4 = Bs3 = Dbb4 = Note('C',4,39,C3.Hz*2)
Cs4 = Db4 = Bss3 = Note('Cis',4,40,Cs3.Hz*2)
D4 = Css4 = Ebb4 = Note('D',4,41,D3.Hz*2)
Ds4 = Eb4 = Fbb4 = Note('Dis',4,42,Ds3.Hz*2)
E4 = Fb4 = Dss4 = Note('E',4,43,E3.Hz*2)
F4 = Es4 = Gbb4 = Note('F',4,44,F3.Hz*2)
Fs4 = Gb4 = Ess4 = Note('Fis',4,45,Fs3.Hz*2)
G4 = Fss4 = Abb4 = Note('G',4,46,G3.Hz*2)
Gs4 = Ab4 = Note('Gis',4,47,Gs3.Hz*2)

A4 = Gss4 = Bbb4 = Note('A',4,48,A3.Hz*2)
As4 = Bb4 = Cbb4 = Note('Ais',4,49,As3.Hz*2)
B4 = Cb5 = Ass4 = Note('B',4,50,B3.Hz*2)
C5 = Bs4 = Dbb5 = Note('C',5,51,C4.Hz*2)
Cs5 = Db5 = Bss4 = Note('Cis',5,52,Cs4.Hz*2)
D5 = Css5 = Ebb5 = Note('D',5,53,D4.Hz*2)
Ds5 = Eb5 = Fbb5 = Note('Dis',5,54,Ds4.Hz*2)
E5 = Fb5 = Dss5 = Note('E',5,55,E4.Hz*2)
F5 = Es5 = Gbb5 = Note('F',5,56,F4.Hz*2)
Fs5 = Gb5 = Ess5 = Note('Fis',5,57,Fs4.Hz*2)
G5 = Fss5 = Abb5 = Note('G',5,58,G4.Hz*2)
Gs5 = Ab5 = Note('Gis',5,59,Gs4.Hz*2)

A5 = Gss5 = Bbb5 = Note('A',5,60,A4.Hz*2)
As5 = Bb5 = Cbb5 = Note('Ais',5,61,As4.Hz*2)
B5 = Cb6 = Ass5 = Note('B',5,62,B4.Hz*2)
C6 = Bs5 = Dbb6 = Note('C',6,63,C5.Hz*2)
Cs6 = Db6 = Bss5 = Note('Cis',6,64,Cs5.Hz*2)
D6 = Css6 = Ebb6 = Note('D',6,65,D5.Hz*2)
Ds6 = Eb6 = Fbb6 = Note('Dis',6,66,Ds5.Hz*2)
E6 = Fb6 = Dss6 = Note('E',6,67,E5.Hz*2)
F6 = Es6 = Gbb6 = Note('F',6,68,F5.Hz*2)
Fs6 = Gb6 = Ess6 = Note('Fis',6,69,Fs5.Hz*2)
G6 = Fss6 = Abb6 = Note('G',6,70,G5.Hz*2)
Gs6 = Ab6 = Note('Gis',6,71,Gs5.Hz*2)

A6 = Gss6 = Bbb6 = Note('A',6,72,A5.Hz*2)
As6 = Bb6 = Cbb6 = Note('Ais',6,73,As5.Hz*2)
B6 = Cb7 = Ass6 = Note('B',6,74,B5.Hz*2)
C7 = Bs6 = Dbb7 = Note('C',7,75,C6.Hz*2)
Cs7 = Db7 = Bss6 = Note('Cis',7,76,Cs6.Hz*2)
D7 = Css7 = Ebb7 = Note('D',7,77,D6.Hz*2)
Ds7 = Eb7 = Fbb7 = Note('Dis',7,78,Ds6.Hz*2)
E7 = Fb7 = Dss7 = Note('E',7,79,E6.Hz*2)
F7 = Es7 = Gbb7 = Note('F',7,80,F6.Hz*2)
Fs7 = Gb7 = Ess7 = Note('Fis',7,81,Fs6.Hz*2)
G7 = Fss7 = Abb7 = Note('G',7,82,G6.Hz*2)
Gs7 = Ab7 = Note('Gis',7,83,Gs6.Hz*2)

A7 = Gss7 = Bbb7 = Note('A',7,84,A6.Hz*2)
As7 = Bb7 = Cbb7 = Note('Ais',7,85,As6.Hz*2)
B7 = Cb8 = Ass7 = Note('B',7,86,B6.Hz*2)
C8 = Bs7 = Dbb8 = Note('C',8,87,C7.Hz*2)

"""
ALL note in our world (can heard) this case is just a piano
Strings is named from Superstring Theory and it also the meterial to play music.

-Superstring theory is an attempt to explain all of the particles and fundamental forces of
 nature in one theory by modeling them as vibrations of tiny supersymmetric strings.
"""
STRINGS = (A0,As0,B0,C1,Cs1,D1,Ds1,E1,F1,Fs1,G1,Gs1,A1,As1,B1,C2,
Cs2,D2,Ds2,E2,F2,Fs2,G2,Gs2,A2,As2,B2,C3,Cs3,D3,Ds3,E3,F3,Fs3,G3,Gs3,
A3,As3,B3,C4,Cs4,D4,Ds4,E4,F4,Fs4,G4,Gs4,A4,As4,B4,C5,Cs5,D5,Ds5,E5,F5,Fs5,G5,Gs5,
A5,As5,B5,C6,Cs6,D6,Ds6,E6,F6,Fs6,G6,Gs6,A6,As6,B6,C7,Cs7,D7,Ds7,E7,F7,Fs7,G7,Gs7,A7,As7,B7,C8)

#Pitch class
do = [note for note in STRINGS if note.name == 'C']
de = [note for note in STRINGS if note.name == 'Cis']
re = [note for note in STRINGS if note.name == 'D']
ri = [note for note in STRINGS if note.name == 'Dis']
mi = [note for note in STRINGS if note.name == 'E']
fa = [note for note in STRINGS if note.name == 'F']
fi = [note for note in STRINGS if note.name == 'Fis']
so = [note for note in STRINGS if note.name == 'G']
sa = [note for note in STRINGS if note.name == 'Gis']
la = [note for note in STRINGS if note.name == 'A']
chi = [note for note in STRINGS if note.name == 'Ais']
si = [note for note in STRINGS if note.name == 'B']

def check_doremi():
    """
    check pitch class from there are Hz
    if some definition is wrong return False

    >>> check_doremi()
    True
    """
    if do != [note for note in STRINGS if note.Hz % C1.Hz == 0]:
        return False
    if de != [note for note in STRINGS if note.Hz % Cs1.Hz == 0]:
        return False
    if re != [note for note in STRINGS if note.Hz % D1.Hz == 0]:
        return False
    if ri != [note for note in STRINGS if note.Hz % Ds1.Hz == 0]:
        return False
    if mi != [note for note in STRINGS if note.Hz % E1.Hz == 0]:
        return False
    if fa != [note for note in STRINGS if note.Hz % F1.Hz == 0]:
        return False
    if fi != [note for note in STRINGS if note.Hz % Fs1.Hz == 0]:
        return False
    if so != [note for note in STRINGS if note.Hz % G1.Hz == 0]:
        return False
    if sa != [note for note in STRINGS if note.Hz % Gs1.Hz == 0]:
        return False
    if la != [note for note in STRINGS if note.Hz % A0.Hz == 0]:
        return False
    if chi != [note for note in STRINGS if note.Hz % As0.Hz == 0]:
        return False
    if si != [note for note in STRINGS if note.Hz % B0.Hz == 0]:
        return False
    return True
