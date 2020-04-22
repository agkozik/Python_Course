# обычный синтаксис
def concat_sequence_v1_yeild(s1, s2):
    for elem in s1:
        yield elem
    for elem in s2:
        yield elem


# упрощенный синтаксис
def concat_sequence_v2_yield_from(s1, s2):
    yield from s1
    yield from s2


seq1 = range(10)
seq2 = range(10, 20)
result = concat_sequence_v1_yeild(seq1, seq2)

for i in result:
    print(i)
print('---------------------------------------------')
seq1 = range(10)
seq1 = range(10, 20)
result = concat_sequence_v2_yield_from(seq1, seq2)

for i in result:
    print(i)