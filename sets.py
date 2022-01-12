def remove_duplicate(list): 
    without_duplicate = []
    for element in list:
        if element not in without_duplicate:
            without_duplicate.append(element)
    return without_duplicate

def rm_duplicate(my_list):
    return list(set(my_list))

def run():
    my_list = [1,2,2,2,3,3,1,1,4]
    print(rm_duplicate(my_list))

if __name__ == "__main__":
    run()