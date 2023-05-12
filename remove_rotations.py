import os

folder_path = "/home/intern/Desktop/fiftyone-scripts/real_data/vehicle"

# Get list of files in folder
files = os.listdir(folder_path)

# Remove images with rotated names
for x in files:
    if "rotated" in x:
        os.remove(os.path.join(folder_path, x))
        print("Removed: ", x)