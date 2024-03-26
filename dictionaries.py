d = {
    'key': 999,
    6: 'six'
}

d['abc'] = 'xyz'
d['mylist'] = [1, 2, 3, 4]
d['mydict'] = {1: 'one', 2: 'two'}

for key, value in d.items():
    print(key, value)

print(d.get('key'))
print(d.get('badkey', 'default not found value'))


def mutation_example(my_dict):
    my_dict['new'] = 'mutation'


mutation_example(d)

print(d['new'])


'''
Count all the words in a string
Return new string with the count of each word in paranthesis
input: this is this example
output: this(2) is(1) this(2) example(1)
'''


def solution(s):
    word_counts = {}
    words = s.split()

    for word in words:
        if word not in word_counts:
            word_counts[word] = 0

        word_counts[word] += 1

    result_str = ""

    for word in words:
        result_str += f"{word}({word_counts[word]}) "

    return result_str.strip()


print(
    solution("this is this example")
)
