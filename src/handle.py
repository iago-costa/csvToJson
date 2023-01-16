import re
import pandas


def get_list(string):
    pattern = re.compile(r'\d{1,2}\.\d{2,3}\.\d{2,3}\.\d{2,3}\-\d{1}')
    # remove numbers and dots and dash from string
    pattern_for_remove = re.compile(r"(\d+)+(.)+(-)+|(\d)")

    try:
        code = re.findall(pattern, string)[0]
    except IndexError:
        code = ' '

    try:
        name = re.sub(pattern, '', string).replace('"', '').strip()
        name = re.sub(pattern_for_remove, '', name)
    except IndexError:
        name = ' '

    list = [code, name]
    return list


def read_csv(file):
    lines = open(file, 'r').readlines()
    return lines

def save_csv(file, data):
    data.to_csv(file, sep=',', encoding='utf-8', index=False)
    return data


def line_by_line(new_file, old_file):
    old_data = read_csv(old_file)
    new_data = pandas.DataFrame()
    for index, row in enumerate(old_data):
        if index != 0:
            list_line = get_list(row)
            new_data.loc[index, 'codigo'] = list_line[0]
            new_data.loc[index, 'nome'] = list_line[1]
    return save_csv(new_file, new_data)

def main():
    new_file = 'courses.csv'
    old_file = 'TabeladeAreasdoConhecimento.csv'
    line_by_line(new_file, old_file)
