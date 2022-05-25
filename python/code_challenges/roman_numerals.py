roman_numerals = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000,
  }

def roman_counter(str):
  total = 0
  roman_list = list(str)
  for current in range(len(roman_list)-1):
    left = roman_list[current]
    right = roman_list[current+1]
    current_num = roman_numerals[left]
    next_num = roman_numerals[right]
    if current_num < next_num:
      current_num = -current_num
    total += current_num

  if str:
    last = roman_list[-1]
    total += roman_numerals[last]
  return total
