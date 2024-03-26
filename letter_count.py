'''
Count number of occurences of a certain letters in a string

Want to know the count of eadch of a set of letters in the input string

how many a's, x's, AND j's in string

return list of request accounts in array
return empty array if letters is empty
'''


def solution(s, letters):
    if not letters or len(letters) == 0:
        return []

    letter_count = {}

    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 0

        letter_count[letter] += 1

    result_counts = [
        letter_count[letter] if letter in letter_count else 0
        for letter in letters
    ]

    return result_counts


test_1 = {"s": "aaabbb", "letters": "ab"}
test_2 = {"s": "ababababaca", "letters": "ac"}
test_3 = {"s": "ananna", "letters": ""}
test_4 = {"s": "abc", "letters": "ad"}

tests = [test_1, test_2, test_3, test_4]
assertions = [[3, 3], [6, 1], [], [1, 0]]


def run_tests(tests_list, assertions_list):
    for i in range(len(tests_list)):
        print(
            solution(tests_list[i]["s"], tests_list[i]["letters"])
            == assertions_list[i]
        )


run_tests(tests, assertions)
