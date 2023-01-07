def suffix_ordinals(input_string):
    list_of_strings = input_string.split(".")
    output_string = ""

    for elem in list_of_strings:
        output_string += elem
        units = int(elem) % 10
        dozens = int(elem) % 100

        if (units == 1 and dozens != 11):
            output_string += "st"
        elif (units == 2 and dozens != 12):
            output_string += "nd"
        elif (units == 3 and dozens != 13):
            output_string += "rd"
        else:
            output_string += "th"
        output_string += " of the "
    
    return output_string[:-8]

print(suffix_ordinals("1.3.2.11.0.13.1234"))