def super_sum(string):
 string = string + '.'
 s = 0
 x = 0
 for ch in string:
  if ch.isdigit():
   x = x * 10 + int(ch)
  else:
   s = s + x
   x = 0
 return s
print(super_sum('Какова сумма 10 и 5?'))