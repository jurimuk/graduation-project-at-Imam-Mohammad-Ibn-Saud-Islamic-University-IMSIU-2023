# Import required modules
import csv
import sqlite3



def uploadToDB(filename,table):
    print("uploading to db")
    # Connecting to the geeks database
    connection = sqlite3.connect('instance/university.db')

    # Creating a cursor object to execute
    # SQL queries on a database table
    cursor = connection.cursor()
    # Opening the person-records.csv file
    file = open(filename)

    # Reading the contents of the
    # person-records.csv file
    contents = csv.reader(file)

    # SQL query to insert data into the
    # person table
    if table=="technicalsupport":
        insert_records = "INSERT INTO Technical_Support (name,telephone_number,email,description) VALUES(?,?,?,?)"
        insertExecute(contents, cursor, insert_records)

    if table=="instructor":
        insert_records = "INSERT INTO instructor (first_name,middle_name ,last_name,position ,course_number,section_number ,email ,office_telephone_number,office_floor ,office_number) " \
                         "VALUES(?,?,?,?,?,?,?,?,?,?)"
        insertExecute(contents, cursor, insert_records)

    if table == "majorplan":
        insert_records = "INSERT INTO major_plan (name,    courses_names,    courses_numbers,    total_courses,    total_hours,    name_acronym,    total_levels) " \
                         "VALUES(?,?,?,?,?,?,?)"
        insertExecute(contents, cursor, insert_records)

    if table == "level":
        insert_records = "INSERT INTO level (level_code,    level_number,    level_major,    no_of_optional_courses,    no_of_mandatory_courses,    leve_courses_names,    leve_courses_numbers,    min_term_hours,    max_term_hours) " \
                         "VALUES(?,?,?,?,?,?,?,?,?)"
        insertExecute(contents, cursor, insert_records)

    if table == "course":
        insert_records = "INSERT INTO course (course_name,    course_number,    course_description,    course_requirements,    course_dependent,    major,    expected_term,    no_of_hours,    course_type,    no_of_available_sections) " \
                         "VALUES(?,?,?,?,?,?,?,?,?,?)"
        insertExecute(contents, cursor, insert_records)


    if table == "section":
        insert_records = "INSERT INTO section (course_name,    course_number,    section_number,    major,    no_of_hours,    reference_number,    seats,    classroom,    daytime_days,    daytime_time) " \
                         "VALUES(?,?,?,?,?,?,?,?,?,?)"
        insertExecute(contents, cursor, insert_records)

    connection.commit()


    connection.close()


def insertExecute(contents, cursor, insert_records):
    cursor.executemany(insert_records, contents)
