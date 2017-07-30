__author__ = 'kathan'
import psycopg2
import os
from datetime import datetime

# Creates connection
def get_connection():
    try:
        conn = psycopg2.connect(database=database, user=user, password=password, host=hostname, port=port)
    except Exception, e:
        raise Exception("Unable to connect!\n{0}".format(e))

    return conn

# Creates tables
def create_tables():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + "/create_table_queries.txt", "r") as create_tables_f:
        create_tables_queries = create_tables_f.read()

    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    try:
        cursor.execute(create_tables_queries)
    except Exception, e:
        conn.rollback()
        conn.close()
        raise Exception("Error creating tables!\n{0}".format(e))

    conn.commit()
    conn.close()
    print "Tables created"


# Loads user data from CSV file
def load_user_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + "/load_user_data_queries.txt", "r") as load_user_data_f:
        user_queries = load_user_data_f.read().format(user_profile_file_path)

    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(user_queries)
    except Exception, e:
        conn.rollback()
        conn.close()
        raise Exception("Loading user data failed.!\n{0}".format(e))

    conn.commit()
    conn.autocommit = True
    conn.close()
    print "User data successfully loaded."


# Loads relationship data from CSV file
def load_relationship_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + "/load_relationship_data_queries.txt", "r") as load_relationship_data_f:
        relationship_queries = load_relationship_data_f.read().format(relationship_file_path)

    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    conn.autocommit = False
    cursor = conn.cursor()

    try:
        cursor.execute(relationship_queries)
    except Exception, e:
        conn.rollback()
        conn.close()
        raise Exception("Loading relationship data failed.!\n{0}".format(e))

    conn.commit()
    conn.autocommit = True
    conn.close()
    print "Relationship data successfully loaded."


# Creates index on relationship table
def create_index():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + "/index_queries.txt", "r") as index_f:
        index_queries = index_f.read()

    conn = get_connection()
    if not conn:
        raise Exception("Connection lost with database")

    cursor = conn.cursor()

    try:
        cursor.execute(index_queries)
    except Exception, e:
        conn.rollback()
        conn.close()
        raise Exception("Creating index failed.!\n{0}".format(e))

    conn.commit()
    conn.close()
    print "Index created."


database = raw_input("Enter database : ").replace(" ", "") or "postgres"
user = raw_input("Enter username : ").replace(" ", "") or "postgres"
password = raw_input("Enter password : ").replace(" ", "") or ""
hostname = raw_input("Enter hostname : ").replace(" ", "") or "localhost"
port = raw_input("Enter port number : ").replace(" ", "") or "5432"
user_profile_file_path = raw_input("Enter complete user profile data file path : ").replace(" ", "")
relationship_file_path = raw_input("Enter complete relationship data file path : ").replace(" ", "")

if not user_profile_file_path:
    raise Exception("Please provide user profile file path.")

if not relationship_file_path:
    raise Exception("Please provide relationship file path.")

print datetime.now().time()

create_tables()
load_user_data()
load_relationship_data()
create_index()

print datetime.now().time()


