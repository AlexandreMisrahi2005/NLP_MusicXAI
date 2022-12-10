import mido

# Load the midi file
mid = mido.MidiFile('Schubert_D960_mv2_8bars_0_01.mid')

# Create a new midi file for the augmented data
out_mid = mido.MidiFile()

# Loop through the tracks in the original midi file
for track in mid.tracks:
    # Create a new track in the output midi file
    out_track = mido.MidiTrack()
    # Add the messages from the original track to the new track, in reverse order
    out_track.extend(reversed(track))
    # Add the new track to the output midi file
    out_mid.tracks.append(out_track)

# Save the augmented midi file
out_mid.save('retrograde.mid')