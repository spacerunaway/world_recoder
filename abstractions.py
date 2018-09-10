# music

def make_music(key, scale, rhythm, tenpo):
    """ Return a abstraction of music """
    return list(key, scale, rhythm, tenpo)

def music_key(music):
    """ Return the key of music, wich is string."""
    return music[0]

def music_scale(music):
    """ Return the scale of music, which is sequence. """
    return music[1]

def music_rhythm(music):
    return music[2]

def music_tenpo(music):
    """ Return the tenpo of music, which is a pair compose by denominator and numetator and seperator "/"."""
    return music[3]

def scale(key):
    """ return a sequence of scale of the start key """

def tenpo(numetator, denominator):
    """ Retrun a tupple of fraction """
    return (numetator, "/", denominator)
