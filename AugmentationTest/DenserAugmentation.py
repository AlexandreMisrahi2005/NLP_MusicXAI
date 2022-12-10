# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 06:03:14 2022

@author: medon
"""
import random
import music21

# Load the midi file
midi = music21.converter.parse('Schubert_D960_mv2_8bars_0_01.mid')

# Create a new score
score = music21.stream.Score()

# Iterate through the parts of the midi
for part in midi.parts:
    # Create a new part
    newPart = music21.stream.Part()
    # Iterate through the notes in the midi
    for note in part.recurse().notes:
        # Add the note to the new part
        newPart.append(note)
        # Randomly decide if a new note should be added
        if random.random() > 0.5:
            # Create a new random note
            newNote = music21.note.Note(random.randint(0,127))
            # Add the new note to the new part
            newPart.append(newNote)
    # Finally, add the new part to the score
    score.append(newPart)

# Write the modified midi file
score.write('midi', 'modified_file_path.mid')