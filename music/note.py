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
    def __init__(self,name,pitch,num=0,hz=1):
        self.name = name
        self.pitch = pitch
        self.num = num
        self.Hz = hz
    def __repr__(self):
        return '{0}{1}'.format(self.name,self.pitch)
