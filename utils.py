from classes import *

def make_chord_dict(chordprogression):
    chord_list = chordprogression.chord_list
    chord_dict = {chord.name:[] for chord in chord_list}
    def next_chord(chord_list,before):
        if len(chord_list) == 0:
            return 0
        else:
            before_next_list = chord_dict[before]
            now = chord_list[0]
            if now in before_next_list:
                now.count +=1
            else:
                now.count +=1
                before_next_list.append(now)
            before = chord_list[0]
            chord_list = chord_list[1:]
            return next_chord(chord_list,before)
