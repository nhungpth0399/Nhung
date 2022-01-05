import csv
import datetime
# Define global variables

student_fields = ['Roll', 'Student Card', 'First Name', 'Last Name',
                  'Gender', 'Date of birth', 'Phone', 'Mid-term', 'Final', 'GPA']
student_database = 'students.csv'

def display_menu():
    print("---------------------------------")
    print(" Student Management System")
    print("---------------------------------")
    print("1. Create New Student")
    print("2. View Details of All Students")
    print("3. Search Details of A Student")
    print("4. Edit Details of Student")
    print("5. Delete Details of Student")
    print("6. Total Number of Good Student")
    print("7. Quit")

# def check_form_date_of_birthday(x):
#     if (int(x[0]) > 3 and int(x[1]) > 9 and int(x[2]) > 1 and int(x[3]) > 2 and int(x[4]) > 2 and int(x[5]) > 9 and int(x[6]) > 9 and int(x[7]) > 9 and len(x)>8):
#         return False

def check_date(year, month, day):
        correctDate = None
        try:
            newDate = datetime.datetime(year, month, day)
            correctDate = True
        except ValueError:
            correctDate = False
        return correctDate

def create_student():
    print("--------------------------")
    print("Create Student Information")
    print("--------------------------")
    global student_fields
    global student_database

    student_data = ['Roll', 'Student Card', 'First Name', 'Last Name',
                  'Gender', 'Date of birth', 'Phone', 'Mid-term', 'Final', 'GPA']
    # for field in student_fields:
    #     # moi lan nhap nay nen dat trong dieu kien nhu if()-else()
    #     value = input("Enter " + field + ": ")
    #     student_data.append(value)

    #vong nay bat buoc phai nhap so
    while True:
        student_data[0]= input("Roll: ")
        if (student_data[0].isdigit()== False):
            while True:
                student_data[0] = input("Enter roll again: ")
                if student_data[0].isdigit():
                    break
            break
        else:
            break

    student_data[1]=input("Student Card: ")

    while True: #isalpha : để kiểm tra xem tất cả ký tự trong chuỗi có phải là ký tự chữ hay không
        student_data[2] = input("First name: ")
        if (student_data[2].isalpha() == False):
            while True:
                student_data[2] = input("Enter first name again: ")
                if student_data[2].isalpha():
                    break
            break
        else:
            break

    while True: #isalpha : để kiểm tra xem tất cả ký tự trong chuỗi có phải là ký tự chữ hay không
        student_data[3] = input("Last name: ")
        if (student_data[3].isalpha() == False):
            while True:
                student_data[3] = input("Enter Last name again: ")
                if student_data[3].isalpha():
                    break
            break
        else:
            break


#vong nay khong cho phep nhap so
    while True:
        student_data[4]= input("Gender: ")
        if student_data[4].isalpha()==False:  #can xem lai vi co the nhap chu vs so
            while True:
                student_data[4]=input("Enter gender again: ")
                if student_data[4].isalpha():
                    break
            break
        else:
            break
#kiem tra ngay/thang/nam
    while True:
        student_data[5] = input(" Enter your birthday in dd/mm/yyyy format: ")
        day, month, year = list(map(int, student_data[5].split("/")))
        check = check_date(year, month, day)
        if check:
            break
        while True:
            student_data[5] = input(" re- Enter your birthday in dd/mm/yyyy format: ")
            day, month, year = list(map(int, student_data[5].split("/")))
            check = check_date(year, month, day)
            if check == True:
                break
        break


    # while True:
    #     student_data[5] = input("Date of birthday: ")
    #     if (student_data[5].isdigit() == False or len(student_data[5]) != 8):
    #         while True:
    #             student_data[5] = input("Enter date of birthday again: ")
    #             if (student_data[5].isdigit() and len(student_data[5]) == 8):
    #                 x = student_data[
    #                     5]  # khong duoc gan x=student_data[5] o dong tren vi neu nguoi dung nhap sai lan dau thi se bi loi chuong trinh khi ep kieu int()
    #                 year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #                 month = int(x[2]) * 10 + int(x[3])
    #                 date = int(x[0]) * 10 + int(x[1])
    #                 if (check_date(year, month, date)):
    #                     break  # lenh break nay de thoat ra khoi vong while true thu 2
    #         break  # lenh break nay de thoat ra khoi vong while true dau tien
    #
    #     elif (student_data[5].isdigit() and len(student_data[5]) == 8):
    #         x = student_data[5]
    #         year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #         month = int(x[2]) * 10 + int(x[3])
    #         date = int(x[0]) * 10 + int(x[1])
    #         if (check_date(year, month, date) == True):
    #             break
    #         while True:
    #             student_data[5] = input("Enter date of birthday again: ")
    #             if (student_data[5].isdigit() and len(student_data[5]) == 8):
    #                 x = student_data[5]
    #                 year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #                 month = int(x[2]) * 10 + int(x[3])
    #                 date = int(x[0]) * 10 + int(x[1])
    #                 if (check_date(year, month, date)):
    #                     break
    #         break
    #     else:
    #         break
#phan nay yeu cau nhap so dien thoai co 10 chu so
    while True:
        student_data[6]= input("Phone: ")
        if (student_data[6].isdigit()== False or len(student_data[6])!=10):
            while True:
                student_data[6]=input("Enter phone again: ")
                if (student_data[6].isdigit() and len(student_data[6])==10):
                    break
            break
        else:
            break

#phan nay bi loi la nhap so kem theo ky tu no lai cho phep
    while True:
        student_data[7]= input("Mid-term: ")

        if (student_data[7].isnumeric()== False):  #isalpha() phan biet dc so thap phan, con isdigit khong phan biet dc
            while True:
                student_data[7] = input("Enter Mid-term again: ")
                if (student_data[7].isnumeric()):
                    if (float(student_data[7])>=0 and float(student_data[7])<=10):
                        break
            break
        elif (student_data[7].isnumeric()):
            if(float(student_data[7]) >= 0 and float(student_data[7]) <= 10):
                break
            if (float(student_data[7])<0 or float(student_data[7])>10):
                while True:
                    student_data[7] = input("Enter Mid-term again: ")
                    if (student_data[7].isnumeric()):
                        if (float(student_data[7]) >= 0 and float(student_data[7]) <= 10):
                            break
                break
        else:
            break

    while True:
        student_data[8]= input("Final: ")

        if (student_data[8].isnumeric()== False):  #isalpha() phan biet dc so thap phan, con isdigit khong phan biet dc
            while True:
                student_data[8] = input("Enter final again: ")
                if (student_data[8].isnumeric()):
                    if (float(student_data[8])>=0 and float(student_data[8])<=10):
                        break
            break
        elif (student_data[8].isnumeric()):
            if (float(student_data[8]) >= 0 and float(student_data[8]) <= 10):
                break
            if (float(student_data[8])<0 or float(student_data[8])>10):
                while True:
                    student_data[8] = input("Enter final again: ")
                    if (student_data[8].isnumeric()):
                        if (float(student_data[8]) >= 0 and float(student_data[8]) <= 10):
                            break
                break
        else:
            break

    student_data[9]= 0.3*float(student_data[7])+0.7*float(student_data[8])

    with open(student_database,'a+',encoding="utf-8") as f:

        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return
# tao them ham create_student_1 nay de dung khi goi den ham edit_student nhe
def create_student_1(student_data):
    while True:
        student_data[0]= input("Roll: ")
        if (student_data[0].isdigit()== False):
            while True:
                student_data[0] = input("Enter roll again: ")
                if student_data[0].isdigit():
                    break
            break
        else:
            break
    student_data[1]=input("Student Card: ")

    while True: #isalpha : để kiểm tra xem tất cả ký tự trong chuỗi có phải là ký tự chữ hay không
        student_data[2] = input("First name: ")
        if (student_data[2].isalpha() == False):
            while True:
                student_data[2] = input("Enter first name again: ")
                if student_data[2].isalpha():
                    break
            break
        else:
            break

    while True: #isalpha : để kiểm tra xem tất cả ký tự trong chuỗi có phải là ký tự chữ hay không
        student_data[3] = input("Last name: ")
        if (student_data[3].isalpha() == False):
            while True:
                student_data[3] = input("Enter Last name again: ")
                if student_data[3].isalpha():
                    break
            break
        else:
            break


#vong nay khong cho phep nhap so
    while True:
        student_data[4]= input("Gender: ")
        if student_data[4].isalpha()==False:  #can xem lai vi co the nhap chu vs so
            while True:
                student_data[4]=input("Enter gender again: ")
                if student_data[4].isalpha():
                    break
            break
        else:
            break

    while True:
        student_data[5] = input(" Enter your birthday in dd/mm/yyyy format: ")
        day, month, year = list(map(int, student_data[5].split("/")))
        check = check_date(year, month, day)
        if check:
            break
        while True:
            student_data[5] = input("Enter your birthday again in dd/mm/yyyy format: ")
            day, month, year = list(map(int, student_data[5].split("/")))
            check = check_date(year, month, day)
            if check == True:
                break
        break

    # while True:
    #     student_data[5] = input("Date of birthday: ")
    #     if (student_data[5].isdigit() == False or len(student_data[5]) != 8):
    #         while True:
    #             student_data[5] = input("Enter date of birthday again: ")
    #             if (student_data[5].isdigit() and len(student_data[5]) == 8):
    #                 x = student_data[
    #                     5]  # khong duoc gan x=student_data[5] o dong tren vi neu nguoi dung nhap sai lan dau thi se bi loi chuong trinh khi ep kieu int()
    #                 year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #                 month = int(x[2]) * 10 + int(x[3])
    #                 date = int(x[0]) * 10 + int(x[1])
    #                 if (check_date(year, month, date)):
    #                     break  # lenh break nay de thoat ra khoi vong while true thu 2
    #         break  # lenh break nay de thoat ra khoi vong while true dau tien
    #
    #     elif (student_data[5].isdigit() and len(student_data[5]) == 8):
    #         x = student_data[5]
    #         year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #         month = int(x[2]) * 10 + int(x[3])
    #         date = int(x[0]) * 10 + int(x[1])
    #         if (check_date(year, month, date) == True):
    #             break
    #         while True:
    #             student_data[5] = input("Enter date of birthday again: ")
    #             if (student_data[5].isdigit() and len(student_data[5]) == 8):
    #                 x = student_data[5]
    #                 year = int(x[4]) * 1000 + int(x[5]) * 100 + int(x[6]) * 10 + int(x[7])
    #                 month = int(x[2]) * 10 + int(x[3])
    #                 date = int(x[0]) * 10 + int(x[1])
    #                 if (check_date(year, month, date)):
    #                     break
    #         break
    #     else:
    #         break

#vong nay bat buoc phai nhap so
    while True:
        student_data[6] = input("Phone: ")
        if (student_data[6].isdigit() == False or len(student_data[6]) != 10):
            while True:
                student_data[6] = input("Enter phone again: ")
                if (student_data[6].isdigit() and len(student_data[6]) == 10):
                    break
            break
        else:
            break

        # phan nay bi loi la nhap so kem theo ky tu no lai cho phep
    while True:
        student_data[7] = input("Mid-term: ")
        if (student_data[7].isnumeric() == False):  # isalpha() phan biet dc so thap phan, con isdigit khong phan biet dc
            while True:
                student_data[7] = input("Enter Mid-term again: ")
                if (student_data[7].isnumeric()):
                    if (float(student_data[7]) >= 0 and float(student_data[7]) <= 10):
                        break
            break
        elif (student_data[7].isnumeric()):
            if (float(student_data[7]) >= 0 and float(student_data[7]) <= 10):
                break
            if (float(student_data[7]) < 0 or float(student_data[7]) > 10):
                while True:
                    student_data[7] = input("Enter Mid-term again: ")
                    if (student_data[7].isnumeric()):
                        if (float(student_data[7]) >= 0 and float(student_data[7]) <= 10):
                            break
                break
        else:
            break

    while True:
        student_data[8] = input("Final: ")

        if (student_data[8].isnumeric() == False):  # isalpha() phan biet dc so thap phan, con isdigit khong phan biet dc
            while True:
                student_data[8] = input("Enter final again: ")
                if (student_data[8].isnumeric()):
                    if (float(student_data[8]) >= 0 and float(student_data[8]) <= 10):
                        break
            break
        elif (student_data[8].isnumeric()):
            if (float(student_data[8]) >= 0 and float(student_data[8]) <= 10):
                break
            if (float(student_data[8]) < 0 or float(student_data[8]) > 10):
                while True:
                    student_data[8] = input("Enter final again: ")
                    if (student_data[8].isnumeric()):
                        if (float(student_data[8]) >= 0 and float(student_data[8]) <= 10):
                            break
                break
        else:
            break

    student_data[9] = 0.3 * float(student_data[7]) + 0.7 * float(student_data[8])

def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")

def search_student():
    global student_fields
    global student_database
    print("--- Search Student ---")
    roll = input("Enter Roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Student Card: ", row[1])
                    print("First Name: ", row[2])
                    print("Last Name: ", row[3])
                    print("Gender: ", row[4])
                    print("Date of birth: ", row[5])
                    print("Phone: ", row[6])
                    print("Mid-term: ", row[7])
                    print("Final: ", row[8])
                    print("GPA: ", row[9])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")

def edit_student():
    global student_fields
    global student_database

    print("--- Update Student ---")

    roll = input("Enter Roll no. to edit: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ", index_student)
                    # student_data = []
                    student_data = ['Roll', 'Student Card', 'First Name', 'Last Name',
                                    'Gender', 'Date of birth', 'Phone', 'Mid-term', 'Final', 'GPA']
                    # for field in student_fields:
                    #     value = input("Enter " + field + ": ")
                    #     student_data.append(value)

                    create_student_1(student_data)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

                # Check if the record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter Roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

def good_student():
    global student_fields
    global student_database
    print("--- Good Student ---")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        l= [row for row in reader] #cai nay se sinh ra list 2 chieu l=[list1[], list[2],....]
        #mỗi list la 1 dong trống file CSV
        # vi file csv co nhung dong trống nen se tao ra nhung list trống,
        # cai nay cần fix ham create_student de no khong co nhung dòng trống
        a=0; count=0
        int(count)
        for i in range(len(l)-1):
          #  print(i)
            if (i%2==0):
                if float(l[i][9])>=6.5:
                    print(l[i][3] +" "+ l[i][4])
                    count+=1
                a=1
        if a==1:
            print(" Total good student is : "+ str(count) + " students")
        if(a==0):
            print("No find good student")