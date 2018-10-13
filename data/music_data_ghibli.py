import sys
sys.path.append('../music')
from music import *

MUSIC_LIST=[]

m = Music('title','composer')
m.addmelody([['melodynotes_matches_chord1'],['melodynotes_matches_chord2'],['etc...']])
info = Info(C_Major,(4,4),86,'Mederato')
m.add_chordprogression([START,info,'chord1','chord2'])
m.add_tags(['ghibli'])
