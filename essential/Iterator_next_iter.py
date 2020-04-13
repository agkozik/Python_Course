# свой аналог range:
import math


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second

            if step != 0:
                self.step = step
            else:
                raise ValueError('Step can not be zero')

            self.length = math.ceil((self.end - self.first) / self.step)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError('My range index out og range')

    def __repr__(self):
        return 'MyRange({}, {}, {})'.format(self.start, self.end, self.step)


r = MyRange(10)
it = iter(r)
print(next(it))


# # реализация цикла For с использованием итератора:
# def my_for(iterable, callback):
#     it = iter(iterable)
#     while True:
#         try:
#             value = next(it)
#             callback(value)
#         except StopIteration:
#             break
#
#
# def loop_body(value):
#     print("Next value received: ", value)
#
#
# my_for(range(10), loop_body)


# class SimpleIterable:
#     # self это iterable, index начинается с нуля
#     def __getitem__(self, index):
#         if 0 <= index <= 5:
#             return index * 2
#         else:
#             raise IndexError
#
#
# iterable = SimpleIterable()
# for value in iterable:
#     print(value)
