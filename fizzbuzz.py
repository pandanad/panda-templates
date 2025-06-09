# I want to crack google, I need fizzbuzz

def fizzbuzz(n):
  for i in range(n):
    if n % 3 == 0 and n % 5 == 0:
      print("FizzBuzz")
    elif n % 3 == 0:
      print("Fizz")
    elif n % 5 == 0:
      print("Buzz")
    else:
      print(i)

# Ab to Google crack
print(fizzbuzz(100))
