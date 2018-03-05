

def fibonacci(n):
  result = 0

  n2 = 0
  n1 = 1

  for i in range(0, n+1):
    if i == 0:
      result = n2
    elif i == 1:
      result = n1
    else:
      result = n2 + n1
      n2, n1 = n1, result

  return result


def main():
  for i in range(8):
    print("fib({}) = {}".format(i, fibonacci(i)))


if __name__ == "__main__":
  main()
