
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
    def __str__(self):
        n = int(input("Number of cookies: "))
        print(n)

    def deposit(self, n):
        Jar = n + Jar
        if n > capacity:
            raise ValueError

    def withdraw(self, n):
        Jar = Jar - n
        if n > Jar:
            raise ValueError

    @property
    def capacity(self):
        return Jar.capacity

    @property
    def size(self):
        return Jar

