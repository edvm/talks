def get_people():
    csv_data = [
        ('Pedro', '22', 'cereal killer'),
        ('Maris', '21', 'crash override'),
        ('Pablo', '12', 'zero cool'),
        ('Perla', '72', 'lord nikon'),
        ('Pablo', '12', 'zero cool'),
    ]
    import pdb; pdb.set_trace()
    pedro = csv_data[0][2]
    maris = csv_data[1][2]
    pablo = csv_data[2][2]
    perla = csv_data[3][2]
    pablo = csv_data[4][2]
    maris = pedro
    pablo = perla
    pedro = pablo
    perla = maris

    return pedro, maris, pablo, perla, pablo

if __name__ == '__main__':
    people_list = get_people()
    print(people_list)
