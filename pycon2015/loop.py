def get_person_as_dict(name, age, nickname):
    return {
        'name': name,
        'age': int(age),
        'nickname': nickname.upper()
    }


def get_people_list():
    people = []
    csv_data = [
        ('Pedro', '22', 'cereal killer'),
        ('Maris', '21', 'crash override'),
        ('Pablo', '12', 'zero cool'),
        ('Perla', '72', 'lord nikon'),
    ]

    for item in csv_data:
        name, age, nickname = item
        person_as_dict = get_person_as_dict(name, age, nickname)
        people.append(person_as_dict)

    return people


if __name__ == '__main__':
    people_list = get_people_list()
    print(people_list)
