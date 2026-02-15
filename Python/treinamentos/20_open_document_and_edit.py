with open('archive.txt', 'w') as archive:
    archive.write("Jesus is the light of the world")

with open('archive.txt', 'r') as archive:
    print(archive.read())