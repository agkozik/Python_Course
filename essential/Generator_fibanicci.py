# def fib(count):
#     first, second = 0, 1
#     for _ in range(count):
#         yield second
#         first = second
#         second = first + second
#         # first, second = second, first + second
#
#
# count = int(input('How many fibanacci numbers to print? '))
# for i in fib(count):
#     print(i)

# -----------------------------------------------------------------------------
# def generator_function():
#     for x in range(5):
#         for y in range(3):
#             if (x+y) % 2 == 0:
#                 yield x * y
#
# generator = generator_function()
# generator = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0)
# for value in generator:
#     print(value)
# -----------------------------------------------------------------------------

# for i in (x*x for x in range(10)): print(i)

# -------------------------------SubGenerator или range----------------------------------------------
def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'

def generator():
    yield '[generator]  start'
    yield from subgenerator()
    yield '[generator]  end'


def generator_with_range():
    # yield from range(3)
    yield from (x * 3 for x in range(3))
    yield 'end'


for value in generator_with_range():
    print(value)
print('-----------------------------------------------------------------')
for value in generator():
    print(value)