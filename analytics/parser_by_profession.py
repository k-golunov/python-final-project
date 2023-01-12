import csv

file_name = 'vacancies_with_skills_and_salary.csv'
profession_names = list()

while True:
    name = input("Вводите построчно варианты названия профессии: ")
    if name == "":
        break
    profession_names.append(name)

with open(file_name, "r", encoding="utf-8-sig") as data:
    reader = csv.reader(data)
    fields = next(reader)
    data = [row for row in reader if len(row) == len(fields)]

name_index = fields.index('name')
profession_data = []

for row in data:
    vacancy_name = row[name_index]
    for version in profession_names:
        if version in vacancy_name:
            profession_data.append(row)

with open("vacancies_need.csv", "a", encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(profession_data)



