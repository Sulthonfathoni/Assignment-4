def fibonacci(n):
  """Prints the first n elements of the Fibonacci sequence.

  Args:
    n: The number of elements to print.
  """

  if n == 0:
    return []

  fibs = [0, 1]
  for i in range(2, n):
    fibs.append(fibs[i - 1] + fibs[i - 2])

  return fibs


def main():
  n = int(input("Enter the number of elements: "))
  fibs = fibonacci(n)
  print("The first {} elements of the Fibonacci sequence are: {}".format(n, fibs))


if __name__ == "__main__":
  main()