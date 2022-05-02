with open("File processing/vegetable.txt", "a+") as myfile:
    myfile.write("\norange")
    myfile.seek(0)
    content = myfile.read()

print(content)




