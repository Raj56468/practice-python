class student():
    
    count = 0

    def __init__(self, name):
        self.name = name
        student.count += 1


s1 = student("Alice")
s2 = student("Bob")
s3 = student("Charlie")

print("Total number of student objects created:", student.count)