TO_DOS = 'xmas.txt'                        # capital letters to rep variable for constant strings


def get_reading(de_doc=TO_DOS):             # using local variable to represent the txt file by default arg
    """ Read a text file and return a list 
    of the entries 
    """                                            # a doc-string used to describe what this function does
    with open(de_doc, 'r') as oge:                 # opening txt file for reading using with-context
        get_entries = oge.readlines()              # readlines read the infor as a list
    return get_entries


def get_writing(entries_local, de_doc=TO_DOS):    # one default arg after one variable in the function parameters
    """ write the entries item list in the text file"""
    with open(de_doc, 'w') as oge:                 # opening txt file for writing using variables and with-context
        oge.writelines(entries_local)              # writelines stores the infor as a list using a local variable


if __name__ == "__main__":                       # a condition to test function in this page but not run where imported
    print('yes oh')
    print(get_reading())