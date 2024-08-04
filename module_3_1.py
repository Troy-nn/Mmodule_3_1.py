calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


print(string_info('string'))

def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
            return True
    return False
print(string_info('Веселое занятие однако'))
print(string_info('Capybara'))
print(is_contains('string', ['string']))
print(is_contains('string', ['zhora_cudejl_He_Tam']))
print(calls)