##################Algorithms###################
# 1. Find the greatest common denominatar of two numbers
# 2. Using Euclid's Algorithm

#Solution:
#1. For 2 integers a and b, where a > b, divide by b.
#2. If the reminder, r is 0 then stop: GCD is b
#3. Otherwise, set a to b, b to r, and repeat at step 1 until r is 0

# def gcd(a, bi):
#     while (bi != 0):
#         te = a

#         a = bi

#         bi = te % bi

#     return a

# print(gcd(60, 96))


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print ("My age is " + str(self.age))

    def add_birthday(self):
        self.age =+ 1


cat = Dog("catyy", 9)

cat.age = 10

print(cat.add_birthday())
