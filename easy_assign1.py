def append_two_strings(string_1, string_2):
    print(string_1+string_2)


def append_character(string_1, char_1):
    print(string_1+char_1)


def append_num_to_string(string_1, num_1):
    num_1=str(num_1)
    print(string_1+num_1)   

if __name__ == "__main__":
    append_two_strings("Hello", " World")
    append_character("Hell", "o")
    append_num_to_string("Hello",1)