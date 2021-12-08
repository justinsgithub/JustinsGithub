import re

def strips(my_string: str):
    return my_string.strip()


def lowers(my_string: str):
    new_string = my_string.lower()
    return new_string


def append_to_file(file_name: str, content: str):
    with open(file_name, "a") as file:
        file.write(f'{content}\n')


def write_to_file(file_name: str, content: str):
    with open(file_name, "w") as file:
        file.write(f'{content}\n')


def list_file(file_name: str):
    with open(file_name, "r") as file:
        my_list = [line.strip() for line in file.readlines()]
        return my_list


def delete_whitespace(my_strings: str):
    return re.sub("\s", "", my_strings)


def hyphenate(string_with_spaces: str):
    return re.sub("\s", "-", string_with_spaces.strip())


def get_this_word(sentence: str, array_position: int):
    seperated_sentence = re.split("\s", sentence)
    return seperated_sentence[array_position]


def delete_numbers(my_strings: str):
    return re.sub("\d", "", my_strings)


def delete_not_numbers(my_strings: str):
    return re.sub("\D", "", my_strings)


def get_age(content: str):
    return delete_not_numbers(get_this_word(content, 0))


def get_gender(content: str):
    return delete_numbers(get_this_word(content, 0))