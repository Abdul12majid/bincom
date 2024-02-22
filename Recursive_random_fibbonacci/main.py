
import random



# -------------------------------------------------------------------------------------------------------------------------------------
# recursive search
def search(data, target, start=0):

  if not data:
    return -1

  mid = len(data) // 2
  if data[mid] == target:
    return mid + start
  elif target < data[mid]:
    return search(data[:mid], target, start)
  else:
    return search(data[mid+1:], target, start + mid + 1)


while True:
  try:
    target = int(input("Enter the number to search for: "))
    break
  except ValueError:
    print("Invalid input. Please enter a number.")


data = [2, 4, 6, 8, 10, 12, 14, 16]

index = search(data, target)

if index != -1:
  print(f"Number {target} found at index {index}")
else:
  print(f"Number {target} not found in the list")



# -------------------------------------------------------------------------------------------------------------------------------------
# Generate random four digits numbers of 0s and 1s and conver to base 10
randomDigits = []

for i in range(4):
    randomDigits.append(str(random.choice([0, 1])))
randomDigits = "".join(randomDigits)

print(f'Generated digits {randomDigits} in base ten {int(randomDigits, 2)}')



# -------------------------------------------------------------------------------------------------------------------------------------
# Fibinacci Sequence
FibArray = [0, 1]

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[n]


print(f'Sum of the first 50 fibonacci sequence is {fibonacci(50)}')