number_of_strings = int(input())
test_cases = []

for _ in range(number_of_strings):
    test_case = input()
    test_cases.append(test_case)

for case in test_cases:
    even_letters = ""
    odd_letters = ""
    for index in range(len(case)):
        if index % 2 == 0:
            even_letters += case[index]
        else:
            odd_letters += case[index]
    test_cases[test_cases.index(case)] =  even_letters + " " + odd_letters
print("\n".join(test_cases))
