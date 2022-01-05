import management

while True:
    management.display_menu()
    choice = input("Enter your choice: ")

    if choice.isalpha(): #neu nhap vao nguyen ky tu

        while True:
            choice= input(" Enter your choice again: ")
            if choice.isdigit():
                if choice == '1':
                    management.create_student()
                elif choice == '2':
                    management.view_students()
                elif choice == '3':
                    management.search_student()
                elif choice == '4':
                    management.edit_student()
                elif choice == '5':
                    management.delete_student()
                elif choice == '6':
                    management.good_student()
                elif choice =='7':
                    break
            break

    elif choice.isdigit(): #neu nhap vao nguyen so

        if choice == '1':
            management.create_student()
        elif choice == '2':
            management.view_students()
        elif choice == '3':
            management.search_student()
        elif choice == '4':
            management.edit_student()
        elif choice == '5':
            management.delete_student()
        elif choice == '6':
            management.good_student()
        elif choice =='7':
            break
    else:  # neu nhap vao ca so va ky tu

        while True:
            choice = input(" Enter your choice again: ")
            if choice.isdigit():
                if choice == '1':
                    management.create_student()
                elif choice == '2':
                    management.view_students()
                elif choice == '3':
                    management.search_student()
                elif choice == '4':
                    management.edit_student()
                elif choice == '5':
                    management.delete_student()
                elif choice == '6':
                    management.good_student()
                elif choice == '7':
                    break
            break

print("---------------------------")