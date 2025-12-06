with open("file IO/data.txt", "r") as f:
    for line in f:
        print(line)

with open("file IO/data.txt", "r") as f:
    print(f.readline())
