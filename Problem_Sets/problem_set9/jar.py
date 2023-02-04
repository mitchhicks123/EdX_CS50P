

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError

        self._size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError

        self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity


def main():
    cookie = Jar(24)
    cookie.deposit(7)
    cookie.withdraw(1)
    print(cookie)


if __name__ == "__main__":
    main()
