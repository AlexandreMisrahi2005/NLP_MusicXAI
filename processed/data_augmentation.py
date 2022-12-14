# utils
import os
import random

# music libraries
import music21
import mido
import pretty_midi

def augment(out_folder="processed/augmented_segmented_midi",
			folder_name="processed/segmented_midi",
			override_output_folder=True,
			notes_increment=True,
			random_notes=True,
			timber_aug=True,
			inverted_aug=True,
			retrograde_aug=True):

	n_files = len(os.listdir(folder_name))

	if not os.path.isdir(out_folder):
		os.mkdir(out_folder)

	if override_output_folder:
		for filename in os.listdir(out_folder):
			if filename[-4:] == ".mid" or filename[-8:] == "DS_Store":
				os.remove(os.path.join(out_folder, filename))
			else:
				print("was going to remove non-midi file:",os.path.join(folder_name,filename))

	print(f"Augmenting {n_files} files...",end="\r")

	for filename in os.listdir(folder_name):
		if filename[-4:] == ".mid":
			filepath = os.path.join(folder_name,filename)

			# rewrite original file
			mid = mido.MidiFile(filepath)
			mid.save(os.path.join(out_folder,filename[:-4]+"_original.mid"))


			# ---------------------------------------------------------
			# increment notes
			if notes_increment:
				midi = mido.MidiFile(filepath)
				for notes_increment in range(1,4):
					for msg in midi.tracks[0]:
						if msg.type == 'note_on':
							msg.note += 3*notes_increment     # change by a semitone

					midi.save(os.path.join(out_folder,filename[:-4]+f"_augmented_notes_{notes_increment}.mid"))
			# ---------------------------------------------------------
			

			# ---------------------------------------------------------
			# add random notes
			if random_notes:
				midi = music21.converter.parse(filepath)
				score = music21.stream.Score()
				for part in midi.parts:
					new_part = music21.stream.Part()
					for note in part.recurse().notes:
						new_part.append(note)
						if random.random() > 0.7:  # hyperparameter: frequency of noise
							new_note = music21.note.Note(random.randint(0,127))
							new_part.append(new_note)
					score.append(new_part)
				score.write("midi",os.path.join(out_folder,filename[:-4]+f"_augmented_random_notes.mid"))
			# ---------------------------------------------------------


			# ---------------------------------------------------------
			# increase speed (timber)
			if timber_aug:
				midi = pretty_midi.PrettyMIDI(filepath)
				for instrument in midi.instruments:
					for note in instrument.notes:
						note.velocity = int(note.velocity*(1+0.1*(random.randint(0,100)/100.0)))   # hyperparameter
						note.end += random.randint(0,5)                                            # hyperparameter
				try:
					midi.write(os.path.join(out_folder,filename[:-4]+f"_augmented_timber.mid"))
				except ValueError:
					print("error saving one file: music too fast!")
			# ---------------------------------------------------------


			# ---------------------------------------------------------
			# invert every note by its complement on the note scale
			if inverted_aug:
				midi = mido.MidiFile(filepath)
				inv = mido.MidiFile()
				for track in mid.tracks:
					inv_track = mido.MidiTrack()
					inv.tracks.append(inv_track)
					for message in track:
						if message.type == "note_on" or message.type == "note_off":
							message.note = 127-message.note
						inv_track.append(message)
				inv.save(os.path.join(out_folder,filename[:-4]+f"_augmented_inverted.mid"))
			# ---------------------------------------------------------


			# ---------------------------------------------------------
			# retrograde augmentation
			if retrograde_aug:
				midi = mido.MidiFile(filepath)
				out_mid = mido.MidiFile()
				for track in mid.tracks:
					out_track = mido.MidiTrack()
					out_track.extend(reversed(track))
					out_mid.tracks.append(out_track)
				out_mid.save(os.path.join(out_folder,filename[:-4]+f"_augmented_retrograde.mid"))


	print(f"Augmented {n_files} midi files into {len(os.listdir(out_folder))} => {len(os.listdir(out_folder))-n_files} new files created")
	return None
	

if __name__ == "__main__":
	augment(out_folder="processed/augmented_segmented_midi",
			folder_name="processed/segmented_midi",
			override_output_folder=True,
			notes_increment=True,
			random_notes=True,
			timber_aug=True,
			inverted_aug=True,
			retrograde_aug=True)
	print("Warning: make sure to zip and rename the augmented folder to \"segmented_midi.zip\" to proceed with data pre-processing, training, etc.")


























