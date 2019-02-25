import pandas as pd
# import pprint
import texttable as tt
from texttable import Texttable, get_color_string, bcolors

from itertools import cycle

import click

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
@click.option('-file', default='all', help='You must select a file')
def rows(rows, col, file):
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

    my_rows(sel_row, sel_col, df)


# TODO:
# Compare row1 vs row2, row1 vs row3, row1 vs row4


@cli.command()
@click.argument('row_pairs')
@click.option('-col', default='all', help='Columns')
@click.option('-file', default='all', help='You must select a file')
def row_pairs(row_pairs, col, file):
    """
    Compare 2 rows
    ie. python3 pandas11.py row-pairs 1,2,3 -col 2,3 -file 4columns2.csv
    """
    print(f'row_pairs file {file}')
    # df = pd.read_csv(file)

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

    if ',' in col:
        parsed_c = col.split(',')
        print(f'parsed_c {parsed_c}')

    print(f"my rows {row_pairs} and col {col}")
    if parsed_r:
        for i in parsed_r:
            sel_row.append(int(i))
            print(i)

    if col == 'all':
        sel_col = 'all'

    # print(f"my col {rows} and col {col}")
    if len(col) == 1:
        sel_col.append(int(col))
    if parsed_c:
        for i in parsed_c:
            sel_col.append(int(i))
            print(i)

    check_row_pairs(sel_row, sel_col, file)


def check_row_pairs(sel_row, sel_col, file):

    filename = file

    df = pd.read_csv(filename)

    # Get columns headers
    index = len(df.index)

    columns = list(df.columns)
    columns_index = len(columns)

    new_list = []
    old_list = []
    group = []
    results = []
    row_group = []
    # row_info_rows = []

    row_old = ''
    row_new = ''

    for i, data in enumerate(sel_row):
        # first row
        if i == 0:
            old_list = df.loc[data - 2, columns].tolist()
            # print(f'old list {old_list}')
            row_old = data
            # row_old = i
            # pass   # ??? does it need to check i==0 ???
        # next rows
        else:
        # if i in sel_row:
            # print(f'old list {old_list}')
            new_list = df.loc[data - 2, columns].tolist()
            row_group.append(new_list)

            # print(f'new_list {new_list}')
            row_new = data
            # print(f'old1 {row_old} new {row_new}')

            group = []

            # for each column
            for ii, old in enumerate(old_list):
                # append first row of columns to group
                if len(group) == 0:
                    row_info = ['Row / Col', row_old, row_new, 'Result']
                    group.append(row_info)
                    # print(group)

                # compare column, same values
                if old == new_list[ii]:
                    # print(f'SAME old {old} row_group {row_group}')
                    col = [columns[ii], old, new_list[ii], '-']
                # compare column, different values
                else:
                    col = [columns[ii], old, new_list[ii], get_color_string(bcolors.RED,"diff")]
                    # print(f'DIFF old {old} new_list {new_list[ii]}')
                # print(f'col {col}')
                group.append(col)

                # add group to results and reset the lists
                if ii == (columns_index - 1):
                    results.append(group)
                    # clean lists
                    new = []
                    group = []

            # # re-assign rows to old
            old_list = new_list
            row_old = row_new
            # print(f'old2 {row_old} new {row_new}')

    print(f'------------ table ------------------')
    for group in results:
        tab = tt.Texttable()
        # tab.header(columns_name)
        # tab.set_deco(tt.Texttable.BORDER |
        #            tt.Texttable.HEADER |
        #            tt.Texttable.VLINES)
        tab.set_deco(tab.HEADER)

        for row in zip(*group):
            # print(row)
            tab.add_row(row)

        s = tab.draw()
        print(s, '\n')

def my_rows(row, selected_columns, df):
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
