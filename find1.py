import pandas as pd
# import pprint
import texttable as tt
from texttable import Texttable, get_color_string, bcolors

# from itertools import cycle

import click

import difflib


from colorama import Fore, Back, Style
"""
COLORS LIST:
black
red
green
yellow
blue
magenta
cyan
white
"""
reset = Style.RESET_ALL
dim = Style.DIM
bold = Style.BRIGHT

greenf = Fore.GREEN
greenb = Back.GREEN
whitef = Fore.WHITE
whiteb = Back.WHITE
redf = Fore.RED
redb = Back.RED
bluef = Fore.BLUE
blueb = Back.BLUE
blackf = Fore.BLACK
blackb = Back.BLACK


# # Print text in red
# print('{} red' . format(redf))
# reset   # trigger the formatting reset
# # Print text in bold and reset
# print('{} bold {}' . format(bold, reset))
# # Print background red, foreground black, bold and finally reset all formatting
# print('{}{}{} bold red {}' . format(redb, blackf, bold, reset))
# # Organized formmating: set text message, set formatting, print formatted message
# text1 = 'this is a text'
# pre_formatted = f'{redb}{blackf}{bold}{text1}{reset}'
# print(pre_formatted)
# # Print other formatting
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')



@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def name(name):
    """test only, enter a name"""
    print(f"my name is {name}")


@cli.command()
@click.argument('rows')
@click.option('-col', default='all', help='Columns')
@click.option('-find', default='all', help='Columns')
@click.option('-file', default='all', help='You must select a file')
def rows(rows, col, find, file):
    """
    Select rows, columns and file
    ie. python3 pandas11.py rows 1,2,3 -col 2,3 -file 4columns2.csv
    """

    print(f'___file {file}')
    df = pd.read_csv(file)

    parsed_r = []
    parsed_c = []
    sel_row = []
    sel_col = []

    range_start = 0
    range_end = 0

    if ',' in rows:
        parsed_r = rows.split(',')
        print(f'parsed_r {parsed_r}')

    if ',' in col:
        parsed_c = col.split(',')
        print(f'parsed_c {parsed_c}')

    print(f"my rows {rows} and col {col}")
    if parsed_r:
        for i in parsed_r:
            sel_row.append(int(i))
            print(i)

    if col == 'all':
        sel_col = 'all'

    print(f"my col {rows} and col {col}")
    if len(col) == 1:
        sel_col.append(int(col))
    if parsed_c:
        for i in parsed_c:
            sel_col.append(int(i))
            print(i)

    my_rows(sel_row, sel_col, sel_find, df)


# TODO:
# Compare row1 vs row2, row1 vs row3, row1 vs row4

# When empty celd is found, its value is 'nan', chande to use something different, maybe color the background


@cli.command()
@click.argument('row_pairs')
@click.option('-col', default='all', help='Columns')
@click.option('-find', default='all', help='Find')
@click.option('-file', default='all', help='You must select a file')
def row_pairs(row_pairs, col, find, file):
    """
    Compare 2 rows
    ie. python3 pandas11.py row-pairs 1,2,3 -col 2,3 -file 4columns2.csv
    """
    print(f'Rows {row_pairs}')
    print(f'Columns {col}')
    print(f'Find {find}')
    print(f'Filename {file}')

    parsed_r = []
    parsed_c = []
    sel_row = []
    sel_col = []

    range_start = 0
    range_end = 0

    sel_row = []
    sel_col = []

    if ',' in row_pairs:
        parsed_r = row_pairs.split(',')
        print(f'parsed_r {parsed_r}')
        if int(parsed_r[0]) < 2:
            error_text1 = 'ERROR on selected rows:'
            error1 = f'{blackb}{redf}{bold}{error_text1}{reset}'
            print(error1)
            print(f'Do not select a Column Header row. Row #1 is reserved for Headers.\nSelect row #2 or above. Your rows are {parsed_r}')
            exit()

    if ',' in col:
        parsed_c = col.split(',')
        print(f'parsed_c {parsed_c}')

    print(f"my rows {row_pairs} and col {col}")
    if parsed_r:
        for i in parsed_r:
            sel_row.append(int(i))

    if col == 'all':
        sel_col = 'all'

    if len(col) == 1:
        sel_col.append(int(col))
    if parsed_c:
        for i in parsed_c:
            sel_col.append(int(i))

    sel_find = ''
    check_row_pairs(sel_row, sel_col, sel_find, file)

@cli.command()
@click.argument('one_all')
@click.option('-col', default='all', help='Columns')
@click.option('-find', default='all', help='Find')
@click.option('-file', default='all', help='You must select a file')
def one_all(one_all, col, find, file):
    """
    Compare 2 rows
    ie. python3 pandas11.py row-pairs 1,2,3 -col 2,3 -file 4columns2.csv
    """
    print(f'Rows {one_all}')
    print(f'Columns {col}')
    print(f'Find {find}')
    print(f'Filename {file}')
    # df = pd.read_csv(file)

    parsed_r = []
    parsed_c = []
    sel_row = []
    sel_col = []

    range_start = 0
    range_end = 0

    sel_row = []
    sel_col = []

    if ',' in one_all:
        parsed_r = one_all.split(',')
        print(f'parsed_r {parsed_r}')
        if int(parsed_r[0]) < 2:
            error_text1 = 'ERROR on selected rows:'
            error1 = f'{blackb}{redf}{bold}{error_text1}{reset}'
            print(error1)
            print(f'Do not select a Column Header row. Row #1 is reserved for Headers.\nSelect row #2 or above. Your rows are {parsed_r}')
            exit()

    if ',' in col:
        parsed_c = col.split(',')
        print(f'parsed_c {parsed_c}')

    print(f"my rows {one_all} and col {col}")
    if parsed_r:
        for i in parsed_r:
            sel_row.append(int(i))

    if col == 'all':
        sel_col = 'all'

    if len(col) == 1:
        sel_col.append(int(col))
    if parsed_c:
        for i in parsed_c:
            sel_col.append(int(i))

    sel_find = ''
    one_all_f(sel_row, sel_col, sel_find, file)

# def find(list):
#     for col_index, col_item in enumerate(col):
#     if keyword == col_item:
#         col[col_index] = get_color_string(bcolors.GREEN, col_item)

def diff_color(diff_char):
    abc = ''
    br_color = ''
    for iii, s in enumerate(diff_char):
        if s[0]==' ':
            # br_color = f'{blackb}{whitef}{bold}{s[-1]}{reset}'
            abc = abc + s[-1]
        elif s[0]=='-':
            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'

        elif s[0]=='+':
            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
            abc = abc + br_color
    return abc

def diff_color_keyword(diff_char):
    abc = ''
    br_color = ''
    for iii, s in enumerate(diff_char):
        if s[0]==' ':
            br_color = f'{blackb}{greenf}{bold}{s[-1]}{reset}'
            abc = abc + br_color
        elif s[0]=='-':
            br_color = f'{redb}{greenf}{bold}{s[-1]}{reset}'

        elif s[0]=='+':
            br_color = f'{redb}{greenf}{bold}{s[-1]}{reset}'
            abc = abc + br_color
    return abc

def one_all_f(sel_row, sel_col, sel_find, file):

    sel_find = sel_find
    keyword = 'cccZZZ'

    filename = file

    df = pd.read_csv(filename)

    # Get columns headers
    index = len(df.index)

    # Get only the selected columns
    columns = []
    for i in sel_col:
        columns.append(df.columns[i-1])

    columns_index = len(columns)

    # !!! Test find in columns
    # print('___')
    # print(df.columns.str.contains("A|C")==True)

    new_list = []
    old_list = []
    group = []
    results = []
    row_group = []

    row_old = ''
    row_new = ''
    find_flag = True

    for i, data in enumerate(sel_row):
        # first row
        if i == 0:
            # pass   # ??? does it need to check i==0 ???
            old_list = df.loc[data - 2, columns].tolist()
            row_old = data   # row number

            # !!! Test searching
            # print(df.loc[data - 2, columns].str.contains("aaa6|aaa4")==True)

        # next rows
        else:
            new_list = df.loc[data - 2, columns].tolist()
            row_group.append(new_list)
            row_new = data   # row number

            # !!! Test searching
            # print(df.loc[data - 2, columns].str.contains("dddd")==True)

            # Group of rows. ie. #2 and #3, #3 and #4...
            group = []

            # for each column
            for ii, old in enumerate(old_list):
                # Fill empty cells with <EMPTY> to allow difflib.ndiff
                if type(old) == type(0.1):
                    old = '<EMPTY>'
                if type(new_list[ii]) == type(0.1):
                    new_list[ii] = '<EMPTY>'

                # append first row of columns to group
                if len(group) == 0:
                    row_info = ['Row / Col', row_old, row_new, 'Compare']
                    # Feature Find: Append Find if searching for a keyword
                    if find_flag == True:
                        row_info.append('Find')
                    # Append first column
                    group.append(row_info)

                # Feature Compare: SAME values on temp list "col"
                if old == new_list[ii]:
                    col = [columns[ii], old, new_list[ii], '-']

                    # Feature Find: color formatting and adding Yes on Find row
                    if col[1] == keyword:
                        keyword_format = f'{blackb}{greenf}{bold}{keyword}{reset}'
                        col[1] = keyword_format
                        col.append('Yes')
                    if col[2] == keyword:
                        keyword_format = f'{blackb}{greenf}{bold}{keyword}{reset}'
                        col[2] = keyword_format
                        col.append('Yes')
                    else:
                        col.append('-')

                # Feature Compare: DIFFERENT values on temp list "col"
                else:
                    col = [columns[ii], old, new_list[ii], get_color_string(bcolors.RED,"diff")]

                    if col[1] == keyword:
                        col.append('Yes')

                    elif col[2] == keyword:
                        col.append('Yes')
                    else:
                        col.append('-')

                    # 1st row formatting: apply color for each different character
                    abc = ''
                    a = old
                    b = new_list[ii]

                    if keyword == a:
                        diff_char = difflib.ndiff(b, a)
                        abc = diff_color_keyword(diff_char)

                    else:
                        diff_char = difflib.ndiff(b, a)
                        abc = diff_color(diff_char)

                    # for iii, s in enumerate(difflib.ndiff(b, a)):
                    #     # APPLY different colors
                    #     abc = ''
                    #
                    #     if a == keyword:
                    #         abc = diff_color_keyword(s, abc)
                    #         # print(abc)
                    #         # if s[0]==' ':
                    #         #     abc = abc + s[-1]
                    #         # elif s[0]=='-':
                    #         #     br_color = f'{redb}{greenf}{bold}{s[-1]}{reset}'
                    #         #
                    #         # elif s[0]=='+':
                    #         #     br_color = f'{redb}{greenf}{bold}{s[-1]}{reset}'
                    #         #     abc = abc + br_color
                    #
                    #     else:
                    #         abc = diff_color(s, abc)
                    #         # print(abc)
                    #         # if s[0]==' ':
                    #         #     abc = abc + s[-1]
                    #         # elif s[0]=='-':
                    #         #     br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                    #         #
                    #         # elif s[0]=='+':
                    #         #     br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                    #         #     abc = abc + br_color

                    # Assign wrong characters colored in red
                    col[1] = abc

                    # 2nd row formatting: apply color for each different character

                    abc = ''
                    a = old
                    b = new_list[ii]

                    if keyword == b:
                        diff_char = difflib.ndiff(a, b)
                        abc = diff_color_keyword(diff_char)

                    else:
                        diff_char = difflib.ndiff(a, b)
                        abc = diff_color(diff_char)

                    # abc = ''
                    # for iii, s in enumerate(difflib.ndiff(a, b)):
                    #     if s[0]==' ':
                    #         abc = abc + s[-1]
                    #     elif s[0]=='-':
                    #         br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                    #     elif s[0]=='+':
                    #         br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                    #         abc = abc + br_color

                    # Assign wrong characters colored in red
                    col[2] = abc

                    # Check if find keyword
                    # if col[1] == keyword:
                    #     k = ' '
                    #     keyword_format = f'{greenb}{greenf}{bold}{k}{reset}'
                    #     col[1] = keyword_format + col[1] + keyword_format
                    # if col[2] == keyword:
                    #     k = 'X'
                    #     keyword_format = f'{greenb}{greenf}{bold}{k}{reset}'
                    #     col[2] = keyword_format + col[2] + keyword_format
                        # col[2] = keyword_format


                    # print('+++')
                    t1 = f'{reset}{col[2]}{reset}'
                    print(t1)

                # !!! Test find in columns
                # for col_index, col_item in enumerate(col):
                #     if 'aaa4' == col_item:
                #         col[col_index] = get_color_string(bcolors.GREEN, col_item)



                # print(f'col {col}')
                group.append(col)

                # add group to results and reset the lists
                if ii == (columns_index - 1):
                    results.append(group)
                    # clean lists
                    new = []
                    group = []

            # DISABLE this reassignment to compare One row VS Rest rows
            # Re-assign new list and index to old list and index
            # old_list = new_list     # List with row values
            # row_old = row_new       # Variable with row number value


    print(f'------------ one vs all ------------------')
    for group in results:
        tab = tt.Texttable()
        tab.set_deco(tab.HEADER)

        for row in zip(*group):
            tab.add_row(row)

        s = tab.draw()
        print(s, '\n')







def check_row_pairs(sel_row, sel_col, sel_find, file):

    sel_find = sel_find
    filename = file

    df = pd.read_csv(filename)

    # Get columns headers
    index = len(df.index)

    # Get only the selected columns
    columns = []
    for i in sel_col:
        columns.append(df.columns[i-1])

    # !!! Test find in columns
    # print('___')
    # print(df.columns.str.contains("A|C")==True)

    columns_index = len(columns)

    new_list = []
    old_list = []
    group = []
    results = []
    row_group = []

    row_old = ''
    row_new = ''

    for i, data in enumerate(sel_row):
        # first row
        if i == 0:
            # pass   # ??? does it need to check i==0 ???
            old_list = df.loc[data - 2, columns].tolist()
            row_old = data   # row number
            # !!! Test searching
            # print(df.loc[data - 2, columns].str.contains("aaa6|aaa4")==True)

        # next rows
        else:
            new_list = df.loc[data - 2, columns].tolist()
            row_group.append(new_list)
            row_new = data   # row number

            # !!! Test find in columns
            # print(df.loc[data - 2, columns].str.contains("dddd")==True)

            # Group of rows. ie. #2 and #3, #3 and #4...
            group = []

            # for each column
            for ii, old in enumerate(old_list):
                # Fill empty cells with <EMPTY> to allow difflib.ndiff
                if type(old) == type(0.1):
                    old = '<EMPTY>'
                if type(new_list[ii]) == type(0.1):
                    new_list[ii] = '<EMPTY>'

                # append first row of columns to group
                if len(group) == 0:
                    row_info = ['Row / Col', row_old, row_new, 'Result']
                    group.append(row_info)

                # compare each column, same values on temp list "col"
                if old == new_list[ii]:
                    col = [columns[ii], old, new_list[ii], '-']

                # compare column, different values
                else:
                    # Test to apply color in 1 word
                    br = f'{redb}{whitef}{bold}{new_list[ii]}{reset}'
                    col = [columns[ii], old, br, get_color_string(bcolors.RED,"diff")]
                    a = old
                    b = new_list[ii]

                    # 1st row formatting: apply color for each different character
                    abc = ''
                    for iii, s in enumerate(difflib.ndiff(b, a)):
                        if s[0]==' ':
                            abc = abc + s[-1]
                        elif s[0]=='-':
                            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'

                        elif s[0]=='+':
                            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                            abc = abc + br_color

                    # Assign wrong characters colored in red
                    col[1] = abc

                    # 2nd row formatting: apply color for each different character
                    abc = ''
                    for iii, s in enumerate(difflib.ndiff(a, b)):
                        if s[0]==' ':
                            abc = abc + s[-1]
                        elif s[0]=='-':
                            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                        elif s[0]=='+':
                            br_color = f'{redb}{whitef}{bold}{s[-1]}{reset}'
                            abc = abc + br_color

                    # Assign wrong characters colored in red
                    col[2] = abc

                for col_index, col_item in enumerate(col):
                    if 'aaa4' == col_item:
                        col[col_index] = get_color_string(bcolors.GREEN, col_item)



                # print(f'col {col}')
                group.append(col)

                # add group to results and reset the lists
                if ii == (columns_index - 1):
                    results.append(group)
                    # clean lists
                    new = []
                    group = []

            # Re-assign new list and index to old list and index
            old_list = new_list     # List with row values
            row_old = row_new       # Variable with row number value


    print(f'------------ table ------------------')
    for group in results:
        tab = tt.Texttable()
        tab.set_deco(tab.HEADER)

        for row in zip(*group):
            tab.add_row(row)

        s = tab.draw()
        print(s, '\n')

def my_rows(row, selected_columns, sel_find, df):
    print(f'selected_columns {selected_columns}')
    # row = [1, 3, 5, 6]
    # selected_columns = [2, 3]
    # selected_columns = []

    # Get columns headers
    index = len(df.index)
    # print(f'index: {index}')

    columns = list(df.columns)
    columns_index = len(columns)
    # print(f'columns_index: {columns_index}')

    # Determine to use selected_columns or all_columns
    if selected_columns == 'all':
        the_columns = range(1, columns_index + 1)
    else:
        the_columns = selected_columns


    header_list = []
    row_list = []
    row_group = []
    row_info_rows = []

    group = []
    results = []

    # Build 1st Column of table
    row_info_rows.append('Row / Col')

    # for each row
    for i in row:
        # first row
        if i == 1:
            header_list = df.loc[i, columns].tolist()
        # next row
        else:
            row_list = df.loc[i-2, columns].tolist()
            row_group.append(row_list)
            row_info_rows.append(str(i))    # Build 1st Column of table

    row_info_rows.append('Results')         # Build 1st Column of table
    # print(row_info_rows)

    results.append(row_info_rows)

    col_results = []
    col_r = []
    for i, lista in enumerate(row_group):
        if i == 0:
            # for column_i in range(1, columns_index + 1):
            for column_i in the_columns:

                col = column_i - 1

                for header_i, header in enumerate(columns):
                    if col == header_i:
                        col_r.append(header)

                col_r.append(lista[col])

                for ii, lista2 in enumerate(row_group):
                    if i != ii:
                        col_r.append(lista2[col])

                set_col_r = set(col_r[1:])
                if len(set_col_r) == 1:
                    print(set_col_r)
                    col_r.append('-')
                if len(set_col_r) > 1:
                    print(set_col_r)
                    col_r.append(get_color_string(bcolors.RED,"diff"))


                print('group')
                print(group)

                # group.append(col_r)
                results.append(col_r)
                # print(results)
                col_r = []

    print(f'------------ rows ------------------')
    tab = tt.Texttable()
    tab.set_deco(tab.HEADER)

    for row in zip(*results):
        tab.add_row(row)

    s = tab.draw()
    print(s, '\n')


if __name__ == '__main__':
    cli()
