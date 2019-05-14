import os

# current path is fetched
current_path = os.getcwd()
# folder is fetched where images are located dynamically
folder = os.path.join(current_path, 'Images')

# loop to iterate over the images in the folder
for filename in os.listdir(folder):
    filename = os.path.join(folder, filename)
    len_cal = filename.split('.')
    # length of filenames will be three for 2 dots
    if len(len_cal) == 3:
        new_filename = filename.replace(".", "_", 1)
        os.rename(filename, new_filename)
    else:
        pass
