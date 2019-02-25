import pandas as pd

# Encoding source: https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
df = pd.read_csv('2columns.csv')

pd_A = df['A']
pd_B = df['B']
# pd_C = df['C']
# pd_D = df['D']

list1 = pd_A.tolist()
list2 = pd_B.tolist()
# list3 = pd_C.tolist()
# list4 = pd_D.tolist()

# Correct index to match CSV when open in Excel
df.index += 2

### COMMENTED DID NOT WORK WITH SFTP KEYS
# Duplicated on Column A
# dup_column_a = pd.concat(g for _, g in df.groupby("A") if len(g) > 0)
# dup_column_b = pd.concat(g for _, g in df.groupby("B") if len(g) > 0)

# Sort by columns, Sorts only column A on this case
# print(df.sort_values(by=['A', 'B']))

temp1_yes = []
temp1_no = []

temp2_yes = []
temp2_no = []

# Remove duplicated
set1 = set(list1)
set2 = set(list2)

# Count empty rows
list1_empty = []
list2_empty = []
for i, l1 in enumerate(list1):
    l1 = str(l1)
    if l1 == 'nan':
        list1[i] = '_no_value'
        # +2 is to print correct index to match Excel
        list1_empty.append((i+2, list1[i]))
    elif l1 in list2:
        temp1_yes.append((i+2, l1))
    else:
        temp1_no.append((i+2, l1))

for i, l2 in enumerate(list2):
    l2 = str(l2)
    if l2 == 'nan':
        list2[i] = '_no_value'
        # +2 is to print correct index to match Excel
        list2_empty.append((i+2, list2[i]))
    elif l2 in list1:
        temp2_yes.append((i+2, l2))
    else:
        temp2_no.append((i+2, l2))


# TODO: find index in list for unique values
# for i, l1 in enumerate(set1):
#     if l1 in set2:
#         temp1_yes.append(str(l1))
#     else:
#         temp1_no.append(str(l1))
#
# for l2 in set2:
#     if l2 in set1:
#         temp2_yes.append(str(l2))
#     else:
#         temp2_no.append(str(l2))
        # print(l2)

# Sort
temp1_yes = sorted(temp1_yes)
temp2_yes = sorted(temp2_yes)

print(f'\nList1 Total Rows: \t\t{str(len(list1))}')
print(f'List1 Filled Rows: \t\t{len(list1)-len(list1_empty)}')
# print(f'\nList1 Total: \t\t{str(len(list1))}')
print(f'List1 Empty Rows: \t\t{len(list1_empty)}')
for i, _ in enumerate(list1_empty):
    print(f'{list1_empty[i][0]}\t{list1_empty[i][1]}')

print(f'\nList2 Total Rows: \t\t{str(len(list2))}')
print(f'List2 Filled Rows: \t\t{len(list2)-len(list2_empty)}')
print(f'List2 Empty Rows: \t\t{len(list2_empty)}')
for i, _ in enumerate(list2_empty):
    print(f'{list2_empty[i][0]}\t{list2_empty[i][1]}')

print(f'\nItems in List1 only: {len(temp1_no)}')
for i, _ in enumerate(temp1_no):
    print(f'{temp1_no[i][0]}\t{temp1_no[i][1]}')


print(f'\nItems in List2 only: {len(temp2_no)}')
for i, _ in enumerate(temp2_no):
    print(f'{temp2_no[i][0]}\t{temp2_no[i][1]}')

shared_items = list(set(list1) & set(list2))
# print(f'type {type(shared_items)}')
print(f'\nItems Both Lists: {len(shared_items)}')
# for i, key_txt in enumerate(shared_items):
#     print(i, " ", key_txt)

# Find the shared_items and get index from List1
shared_items_indexed = []

for i, key_txt in enumerate(shared_items):
    for ii, li_item in enumerate(list1):
        if key_txt == li_item:
            item_indexed = (ii, key_txt)
            shared_items_indexed.append(item_indexed)

# Order list by Index in tuple
shared_items_indexed = sorted(shared_items_indexed, key=lambda x: x[0])

# Find the shared_item on List2
temp_l1 = ''
temp_l2 = ''
matches_rows = []

for i, key_txt in enumerate(shared_items_indexed):
    # Correct the row number
    row_l1 = key_txt[0] + 2
    # Get tuple values
    temp_l1 = (row_l1, key_txt[1])
    # Find match in List2
    for iii, l2 in enumerate(list2):
        if l2 == key_txt[1]:
            row_iii = iii + 2
            # Assign CSV columns B, C, D, etc
            temp_l2 = (str(row_iii), key_txt[1])
    # If matches are assigned to each temporary list
    if temp_l1 and temp_l2:
        # print(temp_l1, temp_l2)
        # print('eeeee')
        print(f'<{temp_l1[0]}> {temp_l1[1]}\n<{temp_l2[0]}> {temp_l2[1]}\n')
        matches_rows.append((temp_l1[0], temp_l2[0]))
        temp_l1 = ''
        temp_l2 = ''

print(f'Rows matching {len(matches_rows)}')
for item in matches_rows:
    print(item)


### BACKUP
# for i, key_txt in enumerate(shared_items):
#     for ii, l1 in enumerate(list1):
#         if l1 == key_txt:
#             # print('_________', ii)
#             # temp_l1 = str(ii) + " >>> " + key_txt
#             temp_l1 = (str(ii + 2), key_txt)
#     for iii, l2 in enumerate(list2):
#         if l2 == key_txt:
#             row_iii = iii + 2
#             # print('_________', iii)
#             # temp_l2 = str(iii) + " >>> " + key_txt
#             temp_l2 = (str(row_iii), list3[row_iii], list4[row_iii], key_txt)
#     if temp_l1 and temp_l2:
#         print(f'<{temp_l1[0]}> {temp_l1[1]}\n<{temp_l2[0]}> __{temp_l2[1]}__ <{temp_l2[2]}> {temp_l2[3]}\n')
#         matches_rows.append((temp_l1[0], temp_l2[0]))
#         temp_l1 = ''
#         temp_l2 = ''

### COMMENTED DID NOT WORK WITH SFTP KEYS
# print(f'\nDuplicated in Column A: \n{dup_column_a}\n')
# print(f'Duplicated in Column B: \n{dup_column_b}\n')


# Find better way to print
# print(f'Items in List1 & List2: {len(temp1_yes)} \n {temp1_yes}\n')
# print(f'Items in List2 & List1: {len(temp2_yes)} \n {temp2_yes}\n')


# # match
# match = set(list1) & set(list2)
#
# if "" in match:
#     match.remove("")
#
# # No match
# no_match = set(list1) ^ set(list2)
# if "" in no_match:
#     no_match.remove("")

# print("\n")
# print("Match Total: {} \n {}" . format( len(match), match))
# print("\n")
# print("NO Match Total: {} \n {}" . format( len(no_match), no_match))
# print("NO Match Total: " + str(len((no_match))) + "\n" + str(no_match))
