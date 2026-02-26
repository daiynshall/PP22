# generators.py — супер простые примеры

# 1) iter() и next()
a = [10, 20, 30]
it = iter(a)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# 2) цикл по итератору
b = [1, 2, 3, 4]
for x in iter(b):
    print(x * x)  # квадраты

# 3) свой итератор (класс)
class MyCounter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n

print(list(MyCounter(5)))  # [4,3,2,1,0]

# 4) генератор (yield)
def gen_numbers(n):
    for i in range(n):
        yield i

for x in gen_numbers(5):
    print("gen:", x)

# 5) генератор-выражение
gen = (x*x for x in range(1, 6))
print(list(gen))  # [1,4,9,16,25]
