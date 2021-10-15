def find_longest_sequence(origin_string):
  disallowed_letters = "z"
  for character in disallowed_letters:
    origin_string = origin_string.replace(character, "")
  
  return origin_string
