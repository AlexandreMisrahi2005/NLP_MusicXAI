
import mido
from mido import MidiFile, MidiTrack
def invert_midi(midi_file):
    # Read the input midi file
    mid = MidiFile(midi_file)
    
    # Create a new midi file to hold the inverted version
    inv = MidiFile()
    
    # Iterate through each track in the input midi file
    for track in mid.tracks:
        # Create a new track in the inverted midi file
        inv_track = MidiTrack()
        inv.tracks.append(inv_track)
        
        # Iterate through each message in the track
        for message in track:
            # Invert the pitch of each note message
            if message.type == 'note_on' or message.type == 'note_off':
                message.note = 127 - message.note
            
            # Add the inverted message to the new track
            inv_track.append(message)
    
    return inv
# Read a midi file
midi_file = 'Schubert_D960_mv2_8bars_0_01.mid'

# Invert the midi file
inv_midi = invert_midi(midi_file)

# Write the inverted midi file to a new file
inv_midi.save('inverted.mid')

