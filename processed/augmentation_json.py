import json
import random

with open("processed/midi_label_map_apex_reg_cls.json", "r") as f:
    data = json.load(f)

for file_path, vec in data.items():
	for i in range(len(vec)-1):
		data[file_path][i] = max(0,data[file_path][i]+random.gauss(0,0.1))

		""" # modify label 
		elif type(vec[i]) == "int":
			if random.random() > 0.9:
				data[file_path][i] += 1
		"""

with open("processed/midi_label_map_apex_reg_cls_aug.json", "w") as f:
    json.dump(data, f)