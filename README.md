The following files were added to perform data augmentation in the ```processed``` folder.
- ```data_augmentation.py```: performs data augmentation on the segmented midi files (in the unzipped segmented_midi folder). Different types of "musically interpretable" augmentation on the MIDI files.
- ```augmentation_total.py```: performs data augmentation directly on the file ```total.csv```. Adds label noise on duplicate data.
- ```augmentation_json.py```: performs data augmentation directly on the json file ```midi_label_map_apex_reg_cls.json```. Adds noise to the vector representations.
