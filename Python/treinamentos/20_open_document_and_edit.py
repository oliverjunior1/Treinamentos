with open('archive.txt', 'w') as arquive:
    arquive.write("Jesus is the light of the world")

with open('archive.txt', 'r') as arquive:
    print(arquive.read())
