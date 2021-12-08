# donkeycar4_training_fix
Small script to handle errors with empty images breaking donkey4 training. For Ubuntu systems.

For use, run:

python training_data_fix.py <src> <dest>

while in the proper donkey conda environment

<src> will just be the path to the relevant data you want to train on that was created by donkey

<dest> will just be the path to a new folder that will be created. Note that this must not be a folder that already exists.

Ex:

python training_data_fix.py data fixed_data

This example assumes that the python file is in the same directory as the data directory

All of the contents from data will be copied into fixed_data and all of the catalog files will have their references to faulty images removed. 
Note that this will only work on linux as of right now. If the demand is required, you can just modify all of the '/' characters to '\\' and that will make it compatible with Windows.


Quick low-quality video demonstrating the script: https://drive.google.com/file/d/1Qha2bK6-5LVsVVvbIRRZSmkpDW4iDSiq/view?usp=sharing

Libraries used:
- shutil
- os
- sys
