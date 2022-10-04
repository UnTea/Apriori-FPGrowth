import csv

from apriori_python import apriori as a_apriori
from efficient_apriori import apriori as e_apriori
from fpgrowth_py import fpgrowth

dataset = []

with open('dataset.csv') as file:
    input_file = csv.DictReader(file)

    for row in input_file:
        string = []

        for key, value in row.items():
            if row[key] == '1':
                string.append(key)

        dataset.append(string)

if __name__ == '__main__':
    freqItemSet, rules = a_apriori(dataset, minSup=0.5, minConf=0.5)

    for i in rules:
        print(i)

    # print("===================================")
    #
    # freqItemSet, rules = e_apriori(dataset, min_support=0.5, min_confidence=0.5)
    #
    # for i in rules:
    #     print(i)
    #
    # print("===================================")

    # freqItemSet, rules = fpgrowth(dataset, minSupRatio=0.1, minConf=0.1)
    #
    # for i in rules:
    #     print(i)
