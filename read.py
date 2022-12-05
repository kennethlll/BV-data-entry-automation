# for getting the file path
import os

# import sys

# for reading the pdf file
import fitz
# export the data to the csv
import csv

# import re

# for list all the file under folder
import glob
# script_dir = os.path.dirname(__file__)
# rel_path = "pdf/X052A-C9079-AX.pdf"
# abs_file_path = os.path.join(script_dir, rel_path)

# glob for listing all the path in certain folder
# https://stackoverflow.com/questions/18262293/how-to-open-every-file-in-a-folder

# transfer the decription in pdf to the company part number
def get_PN(check):
    with open("metalsheet.csv", "r") as file:
        reader = csv.reader(file)
        # skip the header
        next(reader)
        # case for non fraction description
        if check.find("0.25") != -1 or check.find(".25") != -1:
            check += " 1/4"
        if check.find("0.5") != -1 or check.find(".5") != -1:
            check += " 1/2"
        for row in reader:
            if check.find(row[0]) != -1 and check.find(row[1]) != -1:
                return row[3]
    return None


def get_info_from_pdf():

    # pdf file path
    path = 'pdf'
    data = []
    count = 0

    count2 = 1
    sub = []

    # read every pdf under the path folder
    for filename in glob.glob(os.path.join(path, '*.pdf')):
        with fitz.open(os.path.join(os.getcwd(), filename)) as f:
            tmp = ''
            for page in f:
                tmp += page.get_text()
            title = f.metadata['title']

        # tmp info for data_list
        row = ['', '', '', '', '']
        temp_mat = []
        count += 1
        row[0] = count
        row[1] = title
        if row[1][0:3] == 'X05':
            row[3] = 'WJ'
        elif row[1][0:3] == 'X46':
            row[3] = 'PS'
        elif row[1][0:3] == 'X16':
            row[3] = 'GFE'


        tmp = tmp.split("\n")


        # classify the type of pdf file with
        for i in range(len(tmp)):
            # getting the part number
            # getting the title
            if tmp[i] == "TITLE:" and row[1][0:3] == 'X05':
                row[2] = tmp[i+1]
            elif tmp[i] == "TITLE:" and (row[1][0:3] == 'X46' or row[1][0:3] == 'X16'):
                row[2] = tmp[i+4]
            # getting the material
            # row2 is for tmp row for the sub csv
            row2 = ['', '', '', '', '']
            if tmp[i][0:11] == " 1. MAT'L: " and row[1][0:3] == 'X05':
                unique = True
                for item in sub:
                    # already exist in the table
                    if item[3] == tmp[i][10:].strip():
                        unique = False
                        row[4] = item[0]
                        break
                if unique:
                    row2[0] = count2
                    row[4] = count2
                    count2 += 1
                    row2[1] = count
                    # add the sub aseembly part number
                    row2[2] = get_PN(tmp[i][11:].strip())
                    # row2[2] = tmp[i][12:].strip()
                    # get the part name
                    row2[3] = tmp[i][10:].strip()
                    # add the sub assembly qty
                    row2[4] = 1
                    # add the sub csv
                    # print(row2)
                    sub.append(row2)


            # getting the material for press shop
            elif tmp[i][0:12] == "MADE FROM : " and row[1][0:3] == 'X46':

                # unique sub assembly part id
                row2[0] = count2
                row[4] = count2
                count2 += 1
                # refer to top assem
                row2[1] = count
                # add the sub aseembly part number
                row2[2] = tmp[i][12:].strip()
                # add the sub assembly qty
                row2[4] = 1
                # add the sub csv
                sub.append(row2)

            # reading the BOM table and save it in "sub" list
            elif tmp[i][0:4] == "QTY." and row[1][0:3] == 'X16':
                j = 2
                while True:
                    # print("tmp: ", tmp[i + j-1])
                    if tmp[i + j - 1][0:11] == "PAPER SIZE:":
                        break
                    row2 = ['', '', '', '', '']
                    unique = True
                    for item in sub:
                        # already exist in the table
                        if tmp[i + j] == item[2]:
                            unique = False
                            row2[0] = item[0]
                            break
                    # unique sub assembly part id
                    # refer to top assem
                    row2[1] = count
                    # add the sub aseembly part number
                    row2[2] = tmp[i + j]
                    j += 1
                    # add the sub assembly name
                    row2[3] = tmp[i + j]
                    j += 1
                    # add the sub assembly qty

                    # for debug the description have two row

                    while True:
                        if tmp[i + j].isdigit() or (tmp[i + j].find("IN") != -1 and tmp[i + j].find("DAMPING") == -1):
                            break
                        j += 1

                    row2[4] = tmp[i + j]
                    j += 2

                    if unique:
                        row2[0] = count2
                        count2 += 1
                        sub.append(row2)
                    temp_mat.append(row2[0])
                row[4] = temp_mat
        data.append(row)

    with open("data.csv", "w", newline='') as file:
        reader = csv.writer(file, delimiter=',')
        header = ['id', 'part_no', 'part name',
                  'facility', 'material']
        reader.writerow(header)
        reader.writerows(data)

    with open("sub.csv", "w", newline='') as file:
        reader = csv.writer(file, delimiter=',')
        header_2 = ['id', 'top part_id',
                    'sub part number', 'sub part name', 'quantity']
        reader.writerow(header_2)
        reader.writerows(sub)

    print("Sucessfully read pdf file")
