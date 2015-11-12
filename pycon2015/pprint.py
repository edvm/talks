def get_people():
    pedro = 'pedro'
    maris = 'maris'
    pablo = 'pablo'
    perla = 'perla'
    group = {'pedro': pedro, 'pablo': pablo, 'maris': maris, 'perla': perla,
            'cantidad': 4, 'promedios': {'peso': 10, 'edad': 40,
                'altura': {'maxima': '2mts', 'minima': 10}}}
    pablo = maris
    maris = pedro
    pablo = perla
    pedro = pablo
    perla = maris

    return pedro, maris, pablo, perla, pablo, group

if __name__ == '__main__':
    people_list = get_people()
    print(people_list)
