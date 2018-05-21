from faker import Faker
import csv
fake = Faker()

#fake.name()
#fake.first_name()


def gen_names(number):
    with open("random_names.csv", 'w', newline='') as csvfile:
        fieldnames = ['First Name', 'Last Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        while number > 0:
            number -= 1
            first_name = fake.first_name()
            last_name = fake.last_name()
            writer.writerow({"First Name": first_name, "Last Name": last_name})