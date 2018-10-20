my_list  = ["first", "second", "third"]
my_dict  = {"first":1, "second":2, "thrid":3 }
MY_TUPLE = ("const1", "const2", "const3")
#print_list(my_list)
#my_list.append("fourth")
#print_list(my_list)
#my_list.pop(0)
#print_list(my_list)
#Remove a item 
##del my_list[1]
##my_list.pop(1)
##value = my_dict.pop("second")
##print value
##del my_dict["second"]
##print my_dict
##print MY_TUPLE
#_str = "A string value"
#str_to_list = _str.split()
#print str_to_list
#list_to_str = "_".join(str_to_list)
#print list_to_str
#from random import randint
#from random import choice
#print dir(random)
#print help(random.gauss)
#print choice(my_list)


class Car(object):
    """docstring for Car"""
    def __init__(self, arg):
        super(Car, self).__init__()
        self.arg = arg
        