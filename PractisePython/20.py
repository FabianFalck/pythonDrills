#Without the binary search

def non_binary_search(ordered_list, number):
    found = False
    for i in ordered_list:
        if i == number:
            print "The number is in the list!"
            found = True
            break
        else:
            continue
    if found == False:
        print "Sorry, not found!"

def binary_search(ordered_list, number):
    found = False
    it = int(round(len(ordered_list)/2,0))-1 #before was one off! be careful with such errors!
    copy_ordered_list = ordered_list[:]

    while len(copy_ordered_list)>1:
        it = int(round(len(ordered_list)/2,0))-1  #before was one off! be careful with such errors!
        if copy_ordered_list[it] == number:
            found = True
            print "The number is in the list!"
        elif copy_ordered_list[it] < number:
            copy_ordered_list = copy_ordered_list[it:len(copy_ordered_list)-1]
        elif copy_ordered_list[it] > number:
            copy_ordered_list = copy_ordered_list[0:it]

    if found == False:
        print "Sorry, not found!"

non_binary_search([1,2,3,4,5,6,7],8)
binary_search([1,2,3,4,5,6,7],4)


def find(ordered_list, element_to_find):
  start_index = 1
  end_index = len(ordered_list) - 1

  while True:
    middle_index = (end_index - start_index) / 2

    if middle_index < start_index or middle_index > end_index or middle_index < 0:
      return False

    middle_element = ordered_list[middle_index]
    if middle_element == element_to_find:
      return True
    elif middle_element < element_to_find:
      end_index = middle_index
    else:
      start_index = middle_index

if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(find(l, 5)) # prints False
  print(find(l, 10)) # prints True
  print(find(l, -1)) # prints False
  print(find(l, 2)) # prints True
