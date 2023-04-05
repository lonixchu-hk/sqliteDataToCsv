import sqlite3
import csv
import os

# handle result folder if no result folder is created
result_dir = 'result'
abs_result_dir = os.path.abspath(result_dir)
if not os.path.exists(abs_result_dir):
    os.mkdir(abs_result_dir)
    os.chmod(abs_result_dir, 0o777)

source_dir = 'source'
abs_source_dir = os.path.abspath(source_dir)
source_files = os.listdir(abs_source_dir)
files_to_ignore = ['.gitignore', '.gitkeep']
for ignore_file in files_to_ignore:
    source_files.remove(ignore_file)

print("Here are files to be handled: " + ', '.join(source_files))

for file in source_files:

    try:
        folder_name = file.split('.')[0]

        if folder_name == '':
            raise ValueError('')

        # handle result folder if no result folder is created
        result_folder = result_dir + '/' + folder_name
        abs_result_folder = os.path.abspath(result_folder)
        if os.path.exists(abs_result_folder):
            for file_name in os.listdir(abs_result_folder):
                file_path = os.path.join(abs_result_folder, file_name)
                os.remove(file_path)
            os.rmdir(abs_result_folder)
        os.mkdir(abs_result_folder)
        os.chmod(abs_result_folder, 0o777)
        # Open the SQLite database
        try:
            conn = sqlite3.connect(source_dir + '/' + file)

            # Get a list of all tables in the database
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            print('Handling ' + file)

            # Loop through all tables and export them to CSV
            for table in tables:
                table_name = table[0]
                csv_file_name = result_folder + '/' + table_name + '.csv'
                cursor.execute("SELECT * FROM " + table_name)
                with open(csv_file_name, 'w', newline='', encoding='UTF-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])
                    csv_writer.writerows(cursor)
                print(table_name + ' Done.')
            # Close the database connection
            conn.close()
        except sqlite3.DatabaseError:
            print('Skip non DB file')
        else:
            print(file + ' is done. Check out the csv in ' + folder_name)

    except ValueError:
        print('Skip source file with no name')
