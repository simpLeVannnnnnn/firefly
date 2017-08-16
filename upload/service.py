import os

def handle_uploaded_file(f):
    path = "library/library/files/"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def handle_uploaded_file_cover(f):
    path = "library/library/files/cover/"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = path + f.name
    destination = open(file_name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

