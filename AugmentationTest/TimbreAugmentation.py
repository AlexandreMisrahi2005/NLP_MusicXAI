# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 07:00:53 2022

@author: medon
"""

import pretty_midi
import random

# Load MIDI file
midi_data = pretty_midi.PrettyMIDI('Schubert_D960_mv2_8bars_0_01.mid')

# Iterate through all the instruments in the midi file
for instrument in midi_data.instruments:
    print(instrument)
    # Iterate through all the notes in the instrument
    for note in instrument.notes:
        # Randomly change the duration or velocity of individual notes
        note.velocity = int(note.velocity * (1 + 0.7 * (random.randint(0, 100) / 100.0)))
        note.end = note.end + random.randint(0,100)

# Save modified MIDI file
midi_data.write('modified_midi.mid')
