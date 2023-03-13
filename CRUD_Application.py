# Opening CSV file as database using 'with' statement
with open('records.csv', 'r') as files:
    header = ['Index ID', 'Patient ID', 'Name', 'Day', 'Month', 'Year', 'Gender', 'Blood', 'Phone']
    data = []
    for line in files:
        values = line.strip().split(',')
        values[3], values[4], values[5]= int(values[3]), int(values[4]), int(values[5])
        dictionary = dict(zip(header,values))
        data.append(dictionary)
    patients_list = data

# Function to append patient data to 'patients_list'
def save_data(id_number, full_name, day, month, year, gender, blood, ph_number):
    patient_new = {'Index ID':int(id_number), 'Patient ID':id_number, 'Name':full_name, 'Day':day, 
                   'Month':month, 'Year': year, 'Gender':gender, 'Blood':blood, 'Phone':ph_number}
    patients_list.append(patient_new)

# Functions to input patient data
def id_entry():
    while True:
        id_number = input('Please enter Patient Record ID = MedRec-')
        if (' ' not in id_number) and (len(id_number) > 0):
            if (id_number.isdigit()) and (len(id_number) == 3):
                id_list = [i.setdefault('Patient ID') for i in patients_list]
                if id_number in id_list:
                    print(f'Error Duplicates : Patient with ID MedRec-{id_number} already exists')
                else:
                    print(f'Patient Records ID = MedRec-{id_number}\n')
                    break
            else:
                print('Error Messages : Patient ID only accepts 3 numeric entries')
        else:
            if ' ' in id_number:
                print('Error Messages : Patient ID must not contain space character')
            elif len(id_number) == 0:
                print('Error Messages : Patient ID must be filled')
    return id_number
def name_entry():
    while True:
        full_name = input('Please enter Patient Name = ').title()
        name = full_name.split(' ')
        if len(full_name) > 0:
            for each_name in name:
                if each_name.isalpha() == False:
                    print('Error Messages : Name only accepts letters and space in between')
                    break
            else:
                print('Patient Name =', full_name)
                print('')
                break
        else:
            print('Error Messages : Name must be filled')
    return full_name
def birthdate_entry():
    while True:
        year = input('Please enter Patient Year of Birth = ')
        if (' ' not in year) and (len(year) > 0):
            if (len(year) == 4) and (year.isdigit()) and (year[0] != '0'):
                print(f'Year of Birth = {year}')
                print('')
                year = int(year)
                break
            elif (len(year) == 4) and (year.isdigit()) and (year[0] == '0'):
                print('Error Messages : Year of Birth must not be started with "0" number')
            else:
                print('Error Messages : Year of Birth must have 4 numeric entries')
        else:
            if ' ' in year:
                print('Error Messages : Year of Birth must not contain space character')
            elif len(year) == 0:
                print('Error Messages : Year of Birth must be filled')
    while True:
        month = input('Please enter Patient Month of Birth = ')
        month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        if (' ' not in month) and (len(month) > 0):
            if month in month_list:
                if (len(month) == 2) and (month.isdigit()):
                    month_dict = {'01':'January', '02':'February', '03':'March', '04':'April', '05':'May', '06':'June',
                                  '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
                    month_name = month_dict.setdefault(month)
                    print('Month of Birth = {}'.format(month_name))
                    print('')
                    break
            else:
                print('Error Messages : Month of Birth must have 2 numeric entries from "01" to "12"')
        else:
            if ' ' in month:
                print('Error Messages : Month of Birth must not contain space character')
            elif len(month) == 0:
                print('Error Messages : Month of Birth must be filled')
    while True:
        day = input('Please enter Patient Day of Birth = ')
        if (' ' not in day) and (len(day) > 0):
            if (len(day) == 2):
                int_day = int(day)
                month_28_29 = ['02']
                month_30 = ['04', '06', '09', '11']
                month_31 = ['01', '03', '05', '07', '08', '10', '12']
                if month in month_30:
                    if int_day <= 30:
                        print(f'Day of Birth = {day}')
                        break
                    else:
                        print(f'Error Messages : {month_name} only has 30 days')
                        continue
                elif month in month_31:
                    if int_day <= 31:
                        print(f'Day of Birth = {day}')
                        break
                    else:
                        print(f'Error Messages : {month_name} only has 31 days')
                        continue
                elif month in month_28_29:
                    if ((year%4 == 0) and ((year%100 != 0) or (year%400 == 0))) and (int_day <= 29):
                        print(f'Day of Birth = {day}')
                        break
                    elif int_day <= 28:
                        print(f'Day of Birth = {day}')
                        break
                    elif int_day == 29:
                        print(f'Error Messages : {month_name} in {year} only has 28 days')
                        continue
                    elif int_day > 29:
                        if (year%4 == 0) and ((year%100 != 0) or (year%400 == 0)):
                            print(f'Error Messages : {month_name} in {year} only has 29 days')
                        else:
                            print(f'Error Messages : {month_name} in {year} only has 28 days')
                        continue
            else:
                print('Error Messages : Day of Birth must have 2 numeric entries')
        else:
            if ' ' in day:
                print('Error Messages : Day of Birth must not contain space character')
            elif len(day) == 0:
                print('Error Messages : Day of Birth must be filled')    
    day = int(day)
    month = int(month)
    age = age_calculation(day, month, year)
    print('\nPatient Birthday = ', day, month_name, year)
    print("Patient Age = ", age)
    return day, month, year, month_name
def age_calculation(day, month, year):
    age = 2023 - year - ((3, 11) < (month, day))
    return age
def gender_entry():
    while True:
        print('\n1. Male\n2. Female')
        gender_input = input('Please enter Patient Gender = ')
        if (' ' not in gender_input) and (len(gender_input) > 0):
            if gender_input == '1':
                print('Patient Gender = Male')
                gender = 'Male'
                break
            elif gender_input == '2':
                print('Patient Gender = Female')
                gender = 'Female'
                break
            else:
                print(f'Error Messages : Option Number "{gender_input}" is invalid')
        else:
            error_option_input(gender_input)
    return gender
def bloodType_entry():
    while True:
        print('\n1. A\n2. B\n3. AB\n4. O')
        blood_input = input('Please enter Patient Blood Type = ')
        if (' ' not in blood_input) and (len(blood_input) > 0):
            input_list = ['1', '2', '3', '4']
            if blood_input in input_list:
                if blood_input == '1':
                    print(f'Patient Blood Type = A')
                    blood = 'A'
                elif blood_input == '2':
                    print(f'Patient Blood Type = B')
                    blood = 'B'
                elif blood_input == '3':
                    print(f'Patient Blood Type = AB')
                    blood = 'AB'
                else:
                    print(f'Patient Blood Type = O')
                    blood = 'O'
                break
            else:
                print(f'Error Messages : Option Number "{blood_input}" is invalid')
        else:
            error_option_input(blood_input)
    return blood
def phoneNumber_entry():
    while True:
        ph_number = input('\nPlease enter Patient Phone Number = +62')
        if (' ' not in ph_number) and (len(ph_number) > 0):
            ph_number_iterated = [i.get('Phone') for i in patients_list]
            if ph_number.isdigit() and len(ph_number) >= 10 and len(ph_number) <= 12:
                if ph_number[0] == '0':
                    ph_number = '{}'.format(ph_number[1:])
                print(f'Patient Phone Number = +62{ph_number}')
                if ph_number in ph_number_iterated:
                    print(f'Error Duplicates : Patient with Phone Number +62{ph_number} already exists')
                else:
                    break
            else:
                print('Error Messages : Phone Number must have 11 or 12 numeric entries')
        else:
            if ' ' in ph_number:
                print('Error Messages : Phone Number must not contain space character')
            elif len(ph_number) == 0:
                print('Error Messages : Phone Number must be filled')
    return ph_number

# Functions to retrieve patient data
def show_all_data():
    iterable_list = []
    iterated_patients_list = [i.setdefault('Patient ID') for i in patients_list]
    for i in iterated_patients_list:
        if i != '':
            for keys in ['Index ID', 'Patient ID', 'Name', 'Day', 'Month', 'Year', 'Gender', 'Blood', 'Phone']:
                each_keys_values = [i.setdefault(keys) for i in patients_list]
                iterable_list.append(each_keys_values)
    else:
        patients_list_null = []
        for keys in range(9):
            each_keys_values = [i for i in patients_list_null]
            iterable_list.append(each_keys_values)
    iterable_list = list(zip(iterable_list[0], iterable_list[1], iterable_list[2], iterable_list[3], iterable_list[4], 
                             iterable_list[5], iterable_list[6], iterable_list[7], iterable_list[8]))
    iterable_list.sort()
    t1, t2, t3, t4, t5, t6, t7, t8 = 'No', 'Patient ID', 'Name', 'Birthdate', 'Age', 'Gender', 'Blood', 'Phone Number'
    print('-'.center(130, '-'))
    print('|'+t1.center(4, ' ')+'|'+t2.center(14, ' ')+'|'+t3.center(40, ' ')+'|'+t4.center(21, ' ')+'|'+
          t5.center(7, ' ')+'|'+t6.center(10, ' ')+'|'+t7.center(9, ' ')+'|'+t8.center(16, ' ')+'|')
    print('-'.center(130, '-'))
    nomor = 0
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                  7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    for items in iterable_list:
        nomor += 1
        age = age_calculation(items[3], items[4], items[5])
        v1, v2, v3, v4,  = str(nomor), 'MedRec-'+items[1], items[2], str(items[3])+' '+month_dict.setdefault(items[4])+' '+str(items[5])
        v5, v6, v7, v8 = str(age), items[6], items[7], '+62'+items[8]
        print('|'+v1.center(4, ' ')+'|'+v2.center(14, ' ')+'|'+v3.center(40, ' ')+'|'+v4.center(21, ' ')+'|'+v5.center(7, ' ')+
              '|'+v6.center(10, ' ')+'|'+v7.center(9, ' ')+'|'+v8.center(16, ' ')+'|')
def show_selected_data(input):
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
                  7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
    for patient in patients_list:
        if input == patient['Patient ID']:
            age = age_calculation(patient['Day'], patient['Month'], patient['Year'])
            print('\n'+' PATIENT RECORD '.center(130, '='))
            print('\nPatient ID \t: MedRec-'+patient['Patient ID']+'\nName \t\t: '+patient['Name']+'\nBirthdate \t: '+str(patient['Day'])+
                  ' '+month_dict.setdefault(patient['Month'])+' '+str(patient['Year'])+'\nAge \t\t: '+str(age)+'\nGender \t\t: '+patient['Gender']+'\nBlood Type \t: '
                  +patient['Blood']+'\nPhone Number \t: +62'+patient['Phone'])
            print('\n'+'='.center(130, '='), '\n')
            break
    else:
        print('\n'+' PATIENT RECORD '.center(130, '='), '\n')
        print(f'Patient with MedRec-{input} is not found in our system'.center(130, ' '))
        print('\n'+'='.center(130, '='), '\n')
    return input
def id_filtering():
    while True:
        id_filter = input('Please enter Patient Records ID = MedRec-')
        if (' ' not in id_filter) and (len(id_filter) > 0):
            if (id_filter.isdigit()) and (len(id_filter) == 3):
                print(f'Patient Records ID = MedRec-{id_filter}')
                break
            else:
                print('Invalid Entry : Patient ID only accepts 3 numeric entries')
        else:
            if ' ' in id_filter:
                print('Error Messages : Patient ID must not contain space character')
            elif len(id_filter) == 0:
                print('Error Messages : Patient ID must be filled')
    return id_filter

# Function to delete patient data
def each_patient_delete(input):
    for each_patient in patients_list:
        if input == each_patient['Patient ID']:
            patients_list.remove(each_patient)
            break

# Function to handle error in option input
def error_option_input(option):
    if ' ' in option:
        print('Error Messages : Option input must not contain space character\n')
    elif len(option) == 0:
        print('Error Messages : Option input must be filled\n')

# Main page is included in a function
def main_page():
    while True:
        print('\n'+' PATIENT PERSONAL RECORDS '.center(130, '='))
        print('\n1. Create New Patient Record\n2. Read Patient Records\n3. Update Patient Records\n4. Delete Patient Record\n5. Exit\n')
        print('='.center(130, '='), '\n')
        main_page_input = input('Please enter Option Number = ')
        if (' ' not in main_page_input) and (len(main_page_input) > 0):
            
            # Create Page
            if main_page_input == '1':
                print('\n'+' CREATE NEW PATIENT RECORD '.center(130, '=')+'\n\nPlease fill out New Patient Record\n')
                id_number = id_entry()
                full_name = name_entry()
                (day, month, year, month_name) = birthdate_entry()
                age = age_calculation(day, month, year)
                gender = gender_entry()
                blood = bloodType_entry()
                ph_number = phoneNumber_entry()
                while True:
                    a = '\nWill New Patient Record above be created?\n'
                    b = f'\nPatient ID \t: MedRec-{id_number}\nName \t\t: {full_name}\nBirthdate \t: {day} {month_name} {year}'
                    c = f'\nAge \t\t: {age}\nGender \t\t: {gender}\nBlood Type \t: {blood}\nPhone Number \t: +62{ph_number}'
                    d = '\n1. Yes\n2. No'
                    print('\n'+' NEW PATIENT RECORD '.center(130, '='))
                    print(b+c)
                    print('\n'+'='.center(130, '='))
                    print(a+d)
                    confirmation_input = input('Please enter Option Number = ')
                    if (' ' not in confirmation_input) and (len(confirmation_input) > 0):
                        if confirmation_input == '1' or confirmation_input == '2':
                            if confirmation_input == '1':
                                print('\nOption input = Yes\nPatient Record entried successfully')
                                save_data(id_number, full_name, day, month, year, gender, blood, ph_number)
                            else:
                                print('\nOption input = No\nPatient Record not created. Back to Main Page')
                            break
                        else:
                            print(f'\nError Message : Option number "{confirmation_input}" is invalid')
                    else:
                        error_option_input(confirmation_input)
            
            # Read Page
            elif main_page_input == '2':
                while True:
                    print('\n'+' PATIENTS DATABASE '.center(130, '='))
                    print('\n1. Read all Patients Record\n2. Read a Patient Record')
                    print('3. Back to Main Page\n')
                    print('='.center(130, '='), '\n')
                    read_page_input = input('Please enter Option Number = ')
                    option_list = ['1', '2', '3']
                    if (' ' not in read_page_input) and len(read_page_input) > 0:
                        if read_page_input in option_list:
                            if read_page_input == '1':
                                print('Option input = Read all Patients Record')
                                title = ' ALL PATIENTS RECORDS '
                                print('\n'+' ALL PATIENTS RECORDS '.center(130, '='), '\n')
                                show_all_data()
                                print('\n'+'='.center(130, '='), '\n')
                                input('Press Enter to Continue')
                            elif read_page_input == '2':
                                print('Option input = Read a Patient Record\n')
                                show_selected_data(id_filtering())
                                input('Press Enter to Continue')
                            else:
                                print('Option input = Back to Main Page')
                                break
                            continue
                        else:
                            print(f'\nError Message : Option number "{read_page_input}" is invalid')
                    else:
                        error_option_input(read_page_input)
            
            # Update Page
            elif main_page_input == '3':
                while True:
                    print('\n'+' UPDATE PAGE '.center(130, '='), '\n')
                    print('1. Find Patient Record to update by ID\n2. Back to Main Page')
                    print('\n'+'='.center(130, '='), '\n')
                    update_page_input = input('Please enter option number = ')
                    option_list = ['1', '2']
                    if (' ' not in update_page_input) and (len(update_page_input) > 0):
                        if update_page_input in option_list:
                            if update_page_input == '1':
                                print('\n'+' UPDATE PAGE '.center(130, '='), '\n')
                                show_all_data()
                                print('\n'+'='.center(130, '='), '\n')
                                id_matched_input = id_filtering()
                                id_list = [i.setdefault('Patient ID') for i in patients_list]
                                if id_matched_input in id_list:
                                    while True:
                                        show_selected_data(id_matched_input)
                                        print('1. Update Patient ID\n2. Update Name\n3. Update Birthdate')
                                        print('4. Update Gender\n5. Update Blood Type\n6. Update Phone Number\n7. Back\n')
                                        key = (input('Please enter option number = '))
                                        key_list = ['1', '2', '3', '4', '5', '6', '7']
                                        if ' ' not in key and len(key) > 0:
                                            if key in key_list:
                                                def yes():
                                                    print('\nOption input = Yes')
                                                    print('\nPatient Record updated successfully')
                                                def no():
                                                    print('\nOption input = No')
                                                    print('\nPatient Record not updated')
                                                def confirmation_template():
                                                    print('Do you confirm to update data?\n\n1. Yes\n2. No')
                                                    confirmation = input('Please enter option number = ')
                                                    return confirmation
                                                if key == '1':
                                                    print('\nOption input = Update Patient ID')
                                                    id_number_new = id_entry()
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Patient ID'] = id_number_new
                                                                        i['Index ID'] = int(id_number_new)
                                                                        id_matched_input = id_number_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                elif key == '2':
                                                    print('\nOption input = Update Patient Name')
                                                    name_new = name_entry()
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Name'] = name_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                elif key == '3':
                                                    print('\nOption input = Update Patient Birthdate')
                                                    (day_new, month_new, year_new, age_new) = birthdate_entry()
                                                    print('')
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Day'] = day_new
                                                                        i['Month'] = month_new
                                                                        i['Year'] = year_new
                                                                        i['Age'] = age_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                elif key == '4':
                                                    print('\nOption input = Update Patient Gender')
                                                    gender_new = gender_entry()
                                                    print('')
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Gender'] = gender_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                elif key == '5':
                                                    print('\nOption input = Update Patient Blood Type')
                                                    blood_new = bloodType_entry()
                                                    print('')
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Blood'] = blood_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                elif key == '6':
                                                    print('\nOption input = Update Patient Phone Number')
                                                    phone_new = phoneNumber_entry()
                                                    print('')
                                                    while True:
                                                        confirmation = confirmation_template()
                                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                                            if confirmation == '1':
                                                                for i in patients_list:
                                                                    if id_matched_input == i['Patient ID']:
                                                                        i['Phone'] = phone_new
                                                                yes()
                                                            elif confirmation == '2':
                                                                no()
                                                            else:
                                                                print(f'Error Message : Option number "{confirmation}" is invalid\n')
                                                                continue
                                                            break
                                                        else:
                                                            error_option_input(confirmation)
                                                else:
                                                    print('\nOption input = Back to Update Page')
                                                    break
                                            else:
                                                print(f'\nError Message : Option number "{key}" is invalid\n')
                                        else:
                                            error_option_input(key)
                                else:
                                    show_selected_data(id_matched_input)
                                    print('Back to Update Page')
                            else:
                                print('\nOption input = Back to Main Page')
                                break
                        else:
                            print(f'\nError Message : Option number "{update_page_input}" is invalid\n')
                    else:
                        error_option_input(update_page_input)
            
            # Delete Page
            elif main_page_input == '4':
                while True:
                    print('\n'+' DELETE PAGE '.center(130, '='), '\n')
                    print('1. Find Patient Record to delete by ID\n2. Back to Main Page')
                    print('\n'+'='.center(130, '='), '\n')
                    delete_page_input = input('Please enter Option Number = ')
                    option = ['1','2']
                    if (' ' not in delete_page_input) and (len(delete_page_input) > 0):
                        if delete_page_input in option:
                            if delete_page_input == '1':
                                print('\n'+' DELETE PAGE '.center(130, '='), '\n')
                                show_all_data()
                                print('\n'+'='.center(130, '='), '\n')
                                id_matched_input = show_selected_data(id_filtering())
                                id_list = [i.setdefault('Patient ID') for i in patients_list]
                                if id_matched_input in id_list:
                                    print('1. Proceed to delete\n2. Cancel delete. Back to Delete Page\n')
                                    while True:
                                        confirmation = input('Please enter Option Number = ')
                                        if (' ' not in confirmation) and (len(confirmation) > 0):
                                            if confirmation == '1' or confirmation == '2':
                                                if confirmation == '1':
                                                    each_patient_delete(id_matched_input)
                                                    print('Option input = Proceed to delete')
                                                    print('\nPatient Record deleted successfully')
                                                else:
                                                    print('Option input = Cancel delete')
                                                    print('\nPatient Record not deleted')
                                                break
                                            else:
                                                print(f'Error Message : Option input "{confirmation}" is invalid')
                                        else:
                                            error_option_input(confirmation)
                                else:
                                    print('Back to Delete Page')
                            else:
                                print('Option input = Back to Main Page')
                                break
                        else:
                            print(f'Error Message : Option number "{delete_page_input}" is invalid')
                    else:
                        error_option_input(delete_page_input)
            
            # Exit and saving CSV file as database using 'with' statement
            elif main_page_input == '5':
                with open('records.csv', 'w') as files:
                    for dictionaries in patients_list:
                        row = ','.join(str(value) for value in dictionaries.values())
                        files.write(row+'\n')
                    print('\nExit successfully')
                    exit()
            
            else:
                print(f'\nError Message : Option number "{main_page_input}" is invalid')
        else:
            error_option_input(main_page_input)

# Execute the program by calling 'main_page' function
main_page()
