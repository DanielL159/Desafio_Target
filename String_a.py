def count_letter_a(string: str) -> int:

    string_lower = string.lower()

    return string_lower.count('a')

text = input('Give me a string: ')

count_a = count_letter_a(text)

if count_a > 0:
    print(f'The letter "A" appears {count_a} time(s) in the string: "{text}".')
else:
    print(f'The letter "A" does not appear in the string: "{text}".')