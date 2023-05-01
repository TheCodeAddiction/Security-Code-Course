import os

def write_list_to_file(filename, array, message):
    file_path = os.path.join("Output", filename)
    print(message)
    with open(file_path, "w") as f:
        for data in array:
            f.write(data + "\n")
        f.close()
