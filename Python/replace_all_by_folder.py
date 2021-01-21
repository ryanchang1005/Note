import os


def replace_all_text(path, old, new):
    # for one line
    with open(path, "rt") as fin:
        with open('tmp', "wt") as fout:
            for line in fin:
                fout.write(line.replace(old, new))
    os.rename('tmp', path)

    # for show line
    # with open(path, "rt") as fin:
    #     show_path = False
    #     for line in fin:
    #         if old in line:
    #             show_path = True
    #             print(line)

    #     if show_path:
    #         print(path)
    #         print('---')


if __name__ == "__main__":
    target_dir = '/your/folder/path'
    keyword = 'old'
    to = 'new'
    for subdir, dirs, files in os.walk(target_dir):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith('.java'):
                replace_all_text(filepath, keyword, to)
