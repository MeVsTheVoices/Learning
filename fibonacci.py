class Fib:
    def __iter__(self):
        self.a = 1
        self.b = 1
        self.cap = 1000000 
        return self

    def __next__(self):
        hold = self.a
        self.a = self.b
        self.b = self.b + hold
        if hold > self.cap:
            raise StopIteration
        else:
            return hold


