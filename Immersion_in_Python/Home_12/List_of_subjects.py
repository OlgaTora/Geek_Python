"""Create list of school subjects in csv file"""
import csv


def create_csv(file_name: str, list_subjects: list):
    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        csv_result = csv.DictWriter(file, dialect='excel', fieldnames=list(list_subjects[0].keys()))
        csv_result.writeheader()
        csv_result.writerows(list_subjects)


if __name__ == '__main__':
    list_of_subjects = ['Algebra', 'Biology', 'Drawing', 'Chemistry', 'Geography',
                        'Geometry', 'History', 'Literature']

    rows_to_write = []
    for subject in list_of_subjects:
        rows_to_write.append({'Subject': subject})


    file = 'list_of_subjects.csv'
    create_csv(file, rows_to_write)
