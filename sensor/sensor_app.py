# Runner script for all modules
from load_data import load_sensor_data

##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Unclear how to get the VSCode debug launcher
import os
from pathlib import Path
with Path(os.getcwd()) as mypath:
    good = False
    for item in mypath.glob("datasets"):
        if item.is_dir():
            good = True
            print(f"{mypath} contains a 'datasets' directory")
            break

    if not good:
        knowngoodpath = "/workspace/projects/pluralsight/python-decoding-sensor-data"
        print(f"{mypath} does not contain a 'datasets' directory")
        print(f"Changing to '{knowngoodpath}'")
        os.chdir(knowngoodpath)

# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))

# Module 2 code here:

# Module 3 code here:

# Module 4 code here:

# Module 5 code here: