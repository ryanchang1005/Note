import csv


# 16 > 19
def write(row_list):
    output_file_path = 'data/final1.csv'
    with open(output_file_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row_list)
        f.close()


def run():
    exist_name_set = set()

    input_file_path = 'data/output.csv'

    with open(input_file_path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            row = line.split(',')
            name = row[0]

            if name in exist_name_set:
                print(f'name={name} already exist, skip')
                continue

            exist_name_set.add(name)
            write(row)


if __name__ == '__main__':
    run()
