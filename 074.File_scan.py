import os
import fnmatch


def file_path(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(path, file)


paths = file_path("music", 'emp3')

for p in paths:
    print(p)
