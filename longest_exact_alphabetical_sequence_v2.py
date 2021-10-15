# origin_string = "abcabcobobegghakl"
origin_string = "oabcoooooooooabcdooooo"
# origin_string = "acegikmoqsuwy"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def maggie_original():
  longest = origin_string[0] #starting at 'a'
  current = origin_string[0] #Starting at 'a'
  for c in origin_string[1:]: #startig a 'z'
    
    alphabet_vari = alphabet.find(c)
    if c == alphabet[alphabet_vari]:
      if (current.find(alphabet[alphabet_vari])) == -1:
        current += c
        if len(current) > len(longest):
          longest = current
    else:
          current = c
  print( longest)

def john_find_start_of_sequence():
  first_idx = 0
  # for i in range(2):
  for i in range(len(origin_string)):
    
    # print("\n")
    # print("origin_string[i]")
    # print(origin_string[i])
    
    # print("\n")
    # print("origin_string[i+1]")
    # print(origin_string[i+1])
    
    # print("\n")
    # print("alphabet.index(origin_string[i])")
    # print(alphabet.index(origin_string[i]))
    
    # print("\n")
    # print("alphabet[alphabet.index(origin_string[i])]")
    # print(alphabet[alphabet.index(origin_string[i])])
    
    # print("\n")
    # print("alphabet[alphabet.index(origin_string[i+1])]")
    # print(alphabet[alphabet.index(origin_string[i+1])])
    # print()
    
    if alphabet.index(origin_string[i+1]) - alphabet.index(origin_string[i]) == 1:
      return i

    # if origin_string[i + 1] == alphabet[alphabet.index(origin_string[i+1])]:
    #   return i
    
  return first_idx


# def john_attempt():


 




  # return_string = ""
  # new_sequence = ""
  # # TODO make this the return value of the find_start() function
  # # first_idx = 0
  # first_idx = john_find_start_of_sequence()
  # last_idx = first_idx + 2
  # first_idx_alphabet = alphabet.index(origin_string[first_idx])
  # last_idx_alphabet = first_idx_alphabet + 2
  # for letter in origin_string[first_idx:]:
  #   # print(first_idx)
  #   # print(first_idx)
  #   print(origin_string[first_idx:])
  #   while origin_string[first_idx:last_idx] == alphabet[first_idx_alphabet:last_idx_alphabet]:
  #     new_sequence = origin_string[first_idx:last_idx]
  #     # print(new_sequence)
  #     if len(new_sequence) > len(return_string):
  #       return_string = new_sequence
  #       print(new_sequence)
  #       print(first_idx)
  #       first_idx = last_idx
  #       print(first_idx)
  #     first_idx_alphabet = last_idx
  #   last_idx += 1
  #   last_idx_alphabet += 1
  #   # print(first_idx)
  # return return_string

def john_is_next_letter_in_sequence_next_letter_alphabetically(start_idx):
  return alphabet.index(origin_string[start_idx + 1]) - alphabet.index(origin_string[start_idx]) == 1

def john_cycle_through_string():
  possible_sequence = ""
  for i in range(len(origin_string)):
    



if __name__ == "__main__":
  print("You didn't call any functions")
  # print(john_attempt())
  # print(john_find_start_of_sequence())
  # print(john_is_next_letter_in_sequence_next_letter_alphabetically())
