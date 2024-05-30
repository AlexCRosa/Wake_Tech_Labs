#
# Alex Cesar Rosa
# 6/4/2024
#

course_list = []


def main():
    user_menu = input("Enter A to add course, D to drop course, and E to exit: ").upper()

    while user_menu != "E":
        if user_menu == "E":
            break
        elif user_menu == "A":
            add_course()
        elif user_menu == "D":
            drop_course()

        user_menu = input("Enter A to add course, D to drop course, and E to exit: ").upper()


def add_course():
    course = input("Enter course to add: ")

    if course in course_list:
        print("You are already registered in that course")
    else:
        course_list.append(course)
        print("Course added")
        course_list.sort()
        print(f"Courses registered: {course_list}")


def drop_course():
    course = input("Enter course to drop: ")

    if course not in course_list:
        print("You are not registered in that course")
    else:
        course_list.remove(course)
        print("Course dropped")
        print(f"Courses registered: {course_list}")


if __name__ == '__main__':
    main()
