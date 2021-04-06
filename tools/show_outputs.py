import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = []

    with open('output.csv') as f:
        reader = csv.reader(f)
        titles = next(reader)
        for row in reader:
            data.append(row)

    plt.figure()

    for idx, title in enumerate(titles):
        if 'position_1' in title:
            column = [float(row[idx*2]) for row in data]
            plt.plot(column, '-', label=title.replace('_position_1', ''))

    plt.legend()
    plt.show()
