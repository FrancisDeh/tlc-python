import csv
import psycopg2

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
# Create a cursor via the connection
cur = con.cursor()
# Alternatively, set the 'search_path' to set the schema search path (prefix)
cur.execute("SET search_path TO pubs2")

# table name
TABLE_NAME = "people"


def close_db_connection():
    cur.close()
    con.close()


# Create table
def create_people_table():
    # drop table if already exist
    cur.execute(f"drop table if exists {TABLE_NAME}")

    # first_name, last_name, address, city, county, state, zip, phone1, phone2
    cur.execute(f"create table {TABLE_NAME}("
                "first_name varchar(200) not null,"
                "last_name varchar(200) not null,"
                "address varchar(200),"
                "city varchar(200),"
                "county varchar(200),"
                "state varchar(200),"
                "zip varchar(200),"
                "phone1 varchar(200),"
                "phone2 varchar(200))"
                )
    con.commit()


# read data from csv file
def read_csv_file():
    with open('users.csv', newline='') as file:
        read = csv.DictReader(file)
        people = []  # [{last_name: "James", first_name: "John"}]
        for row in read:
            # first_name, last_name, address, city, county, state, zip, phone1, phone2
            people.append(
                (row['first_name'],
                 row['last_name'],
                 row['address'],
                 row['city'],
                 row['county'],
                 row['state'],
                 row['zip'],
                 row['phone1'],
                 row['phone2'])
            )
        file.close()
    return people


# write data to file
def write_to_file(people_list):
    file = open('new_users.txt', 'w')
    file.write(str(people_list))
    file.close()


def add_a_person_to_db(person_tuple):
    # ("Jane", 23, "Achimota")
    cur.execute(f"insert into {TABLE_NAME} values (%s, %s)", person_tuple)
    con.commit()
    print(f"{cur.rowcount} record(s) inserted successfully")


def delete_people_table():
    cur.execute(f"delete from {TABLE_NAME}")
    con.commit()


def add_people_to_db(people_list):
    # [("Jane", 23, "Achimota")]
    cur.executemany(f"insert into {TABLE_NAME} values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", people_list)
    con.commit()
    print(f"{cur.rowcount} record(s) inserted successfully")


def number_of_people_by_state():
    query = f"select state, count(first_name) from {TABLE_NAME} group by state;"
    cur.execute(query)
    return cur.fetchone()  # fetchmany(4), fetchall(), fetchone()


def find_people_by_zip_code(zip_code):
    query = f"select zip, first_name from {TABLE_NAME} where zip = %s;"
    cur.execute(query, (str(zip_code),))
    return cur.fetchall()


def find_all_people_grouped_by_zip_code():
    query = f"SELECT zip, string_agg(first_name , ', ') FROM {TABLE_NAME} GROUP BY zip;"
    cur.execute(query)
    return cur.fetchall()


def find_people_by_last_name_first_character(first_character):
    query = f"select last_name from {TABLE_NAME} where last_name like '{first_character}%';"
    cur.execute(query)
    return cur.fetchall()


# create_people_table()
# delete_people_table()
# plist = read_csv_file()
# write_to_file(plist)
# add_people_to_db(plist)
# result = number_of_people_by_state()
# result = find_people_by_zip_code('10003')
# result = find_people_by_last_name_first_character('E')
result = find_all_people_grouped_by_zip_code()
print(result)

for value in result:
    print(value)

close_db_connection()
