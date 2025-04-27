cities=["Gujranwala","Lahore","Islamabad","Karachi","Multan","meerpur"]
heroes=["Musa","Eesa","Fahed","Faizan"]
def print_len(list):
    print(len(list))


def print_list(list):
    for city in list:
        print(city, end=" ")   # end function single line my hi convert kr ky dy ga agr na lgay to 
                               # output multiple line my ay gi


print_list(cities)



def print_list(list):
    for hero in list:      # is py end ka function use nhi howa is wja sy sy single line my output nhi ha 
        print(hero) 

print_list(heroes)
        
