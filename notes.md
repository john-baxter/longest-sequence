
### Given:
alphabet as string\
origin string (a string of random letters)

### Assumptions:
origin string is only lower case letters\
if more than one sequence of the same length exists then return the first sequence of that length

### Steps:
1. find beginning of alphabetical sequence
1. get length of alphabetical sequence
1. set variables to mark the indices of start and end of sequence
1. check through the rest of `origin_string` for more sequences
1. if any subsequent sequences are longer then reassign `start` and `end`* variables
1. return the slice of `origin_string` between `start` and `end`.

\* Don't call a variable `end`

### Pseudocode:
Setup
```
SET variables
first_idx = 0       # might not need this   ## decided to make a separate function to define this
last_idx = 0        # might not need this
alphabet = "abc...xyz"
origin_string = "{whatever}"
return_string = ""  # this might go into the function
```

Find the beginning of a sequence
```
FOR each letter in origin_string STARTING at first_idx
  CHECK if the next letter in origin_string is also the next letter in alphabet
  IF the next letters in origin_string AND alphabet are the same
  THEN set first_idx as idx of letter in origin_string
  ELSE this is not the beginning of a sequence - MOVE on to the next letter in origin_string
```

Find the length of the sequence (or: Find a sequence and set it as return value if it is long enough?)
```
SET variable new_sequence = ""
last_idx = first_idx + 1 # change this to 2 because of how python does slicing
first_idx_alphabet = idx OF letter at first_idx
last_idx_alphabet = first_idx_alphabet + 1 # change this to 2 because of how python does slicing
FOR each letter in origin_string STARTING at first_idx
  WHILE string slice origin_string[first_idx:last_idx] == string slice alphabet[first_idx_alphabet:last_idx_alphabet]
    # swap the order of these next two lines
    INCREMENT last_idx AND last_idx_alphabet
    SET variable new_sequence = string slice origin_string[first_idx:last_idx]
  IF length of new_sequence > length of return_string
  THEN SET variables
    return_string = new_sequence
    first_idx = last_idx + 1 # remove the +1 because of the above `change to +2`
  ELSE do nothing

RETURN return_string
```
<hr>

# Planning

|input|output|
|---|---|
|a|a|
|ab|ab|
|abz|ab|
|zab|ab|
|abc|abc|
|||
|zabczzabcdz|abcd|
|yabcyyabcdy|abcd|
|||

<hr>

# Notes
```
origin_string\
"zabczzabcdz"

index_difference_list\
[23, 1, 1, 21, 0, 23, 1, 1, 1, 20]

list_of_ones\
[1, 1, 1]
```

## input output for index_difference

|input|output|
|---|---|
|""|[]|
|a|[]|
|ab|[1]|
|abz|[1, 22]|
|zab|[23, 1]|
|abc|[1, 1]|
|||
|zabczzabcdz|[-25, 1, 1, 23, 0, -25, 1, 1, 1, 22]|
|yabcyyabcdy|[-24, 1, 1, 22, 0, -24, 1, 1, 1, 21]|
|||
