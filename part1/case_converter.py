def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]       #using list comprehension 

    return ''.join(snake_cased_char_list).strip('_')        #stripping the _ at first 


def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()