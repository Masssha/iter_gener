import types


def flat_generator(list_of_lists):
    cursor = 0
    number = 0
    while list_of_lists:
        if len(list_of_lists[cursor]) > number:
            item = list_of_lists[cursor][number]
            number += 1
        if len(list_of_lists[cursor]) == number:
            cursor += 1
            number = 0

        yield item


list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

for g in flat_generator(list_of_lists_1):
    print(g)

# def test_2():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#
#     assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
#
#
# if __name__ == '__main__':
#     test_2()