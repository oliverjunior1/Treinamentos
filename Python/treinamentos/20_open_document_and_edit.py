with open('archive.txt', 'w') as archive:
    archive.write("'Anyone go to Father unless for me', said Jesus.")

with open('archive.txt', 'r') as archive:
    print(archive.read())