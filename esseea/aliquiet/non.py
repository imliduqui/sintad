def get_file_data(file_path):
    with open(file_path, 'r') as file:
        file_data = file.read()
    return file_data
