import csv


class FileService:

    @staticmethod
    def read_file(path):
        result = ''
        with open(path, 'r') as f:
            for line in f.readlines():
                result += line
        return result

    @staticmethod
    def write_file_by_append(line, path):
        with open(path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(line)
            f.close()
