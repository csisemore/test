def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here

    name_list = fullname.split()
    init = ""
    for name in name_list:
        init = init + name[0]
    print(init.upper())

def main():
    get_initials("homer simpson")
    #print(init.upper())
    get_initials("marge simpson")
    get_initials("lisa simpson")
    get_initials("bart Simpson")
    get_initials("Maggie simpson")

if __name__ == '__main__':
    main()

