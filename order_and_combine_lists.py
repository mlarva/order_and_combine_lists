import sys

#with the input of multiple ordered lists of equal length, create an output of one ordered list containing all the elements of inputted lists
def order_and_combine_lists(*args):
  """
  this function takes in any number of ordered  of equal length and returns one ordered list containing all the elements of the lists inputted

  parameters:
  arg* (list) : an ordered list

  returns:
  list: and ordered list
  """

  #first check to see if lists are of equal length
  equal_list_lengths = check_list_length(*args)
  if not equal_list_lengths:
    return "Please enter multiple lists of equal length"

  #establish pointers
  list_of_pointers = [0] * len(args)

  #establish how many elements return_list should have
  return_length = 0
  for x in args:
    return_length += len(x)

  #compare pointers and add lower pointed value to return list
  return_list = []
  while len(return_list) != return_length:
    #first get the lowest value of the pointer and its argument
    lowest_value = sys.maxsize
    for argument, pointer in enumerate(list_of_pointers):
      #if pointer is higher than the len of list, continue to avoid index out of range being thrown
      if list_of_pointers[argument] >= len(args[argument]):
        continue
      if args[argument][pointer] < lowest_value:
        lowest_value = args[argument][pointer]
        lowest_value_argument = argument
    #then add value to return_list and up that arguments pointer
    return_list.append(lowest_value)
    list_of_pointers[lowest_value_argument] += 1
  return return_list

def check_list_length(*args):
  """
  this function takes in any number of lists and returns True if the lists are of equal length or false if not. If less than 2 lists are used as a parameters, False is returned

  parameters:
  arg* (list) : a list

  returns:
  bool: true if lists are of equal length. False if lists are not of equal length, or if less than two lists are given as arguments.
  """
  if len(args) < 2:
    return False
  length = len(args[0])
  for x in args:
    if len(x) != length:
      return False
    length = len(x)
  return True

list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
list3 = [20,30,40,50,60]
list4 = [3,]
print("Output with equal list sizes as input: ")
print(order_and_combine_lists(list1, list2, list3))
print("Output with unequal list sizes as input: ")
print(order_and_combine_lists(list1, list2, list4))
