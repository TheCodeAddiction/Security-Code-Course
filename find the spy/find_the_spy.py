import re

def find_repeated_name(filename):
    name_set = set()
    name_regex = r'(?<=\d\.\s)[^,]+'
    with open(filename, 'r') as file:
        for line in file:
            name = re.search(name_regex,line.strip()).group()
            if name in name_set:
                print(f"{name} is the spy!")
            else:
                name_set.add(name)



find_repeated_name("access_log.log")
