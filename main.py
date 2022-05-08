from log_decorator import log_path_way
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def contacts_treatment(contacts_list):
    edit_contact_list = []
    for element in contacts_list:
        fl_name = (element[0] + ' ' + element[1] + ' ' + element[2]).rstrip().split(' ')
        for iter in range(len(fl_name)):
            element[iter] = fl_name[iter]
        element[5] = re.sub(\
            r'\D*\d?\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2}\s?)[^а-яё]*(доб\.)?\D*(\d*)\D*',\
            r'+7(\g<1>)\g<2>-\g<3>-\g<4>\g<5>\g<6>',\
            element[5])
        edit_contact_list += [element]
    return edit_contact_list
@log_path_way('log.txt')
def double_contacts_treatment(edit_contact_list):
    non_double_contact_list = []
    for contact in range(len(edit_contact_list)-1):
        non_double = False
        for iter in range(contact+1, len(edit_contact_list)):
            if edit_contact_list[contact][0] == edit_contact_list[iter][0] and \
                edit_contact_list[contact][1] == edit_contact_list[iter][1]:
                if edit_contact_list[iter][2] != '':
                    edit_contact_list[contact][2] = edit_contact_list[iter][2]
                if edit_contact_list[iter][3] != '':
                    edit_contact_list[contact][3] = edit_contact_list[iter][3]
                if edit_contact_list[iter][4] != '':
                    edit_contact_list[contact][4] = edit_contact_list[iter][4]
                if edit_contact_list[iter][5] != '':
                    edit_contact_list[contact][5] = edit_contact_list[iter][5]
                if edit_contact_list[iter][6] != '':
                    edit_contact_list[contact][6] = edit_contact_list[iter][6]
                non_double_contact_list += [edit_contact_list[contact]]
                edit_contact_list[iter][0] = 'double'
                non_double = True
        if  edit_contact_list[contact][0] != 'double' and non_double == False:
            non_double_contact_list += [edit_contact_list[contact]]
    return non_double_contact_list


if __name__ == '__main__':
    contacts_list = contacts_treatment(contacts_list)
    contacts_list = double_contacts_treatment(contacts_list)

    with open("edit_phonebook_raw.csv", encoding='utf-8', mode='w') as f:
        writer = csv.writer(f)
        writer.writerows(contacts_list)