import random


def quick_sort(l):
  stack = []

  stack.append(0)
  stack.append(len(l) - 1)

  while len(stack) > 0:
    end = stack.pop()
    start = stack.pop()

    p = partition(l, start, end)

    if p-1 > start:
      stack.append(start)
      stack.append(p - 1)

    if p+1 < end:
      stack.append(p+1)
      stack.append(end)


def partition(l, start, end):
  x = l[end] # pivot
  i = start - 1
  for j in range(start, end):
    if l[j] <= x:
      i = i + 1
      l[i], l[j] = l[j], l[i]
  l[i+1], l[end] = l[end], l[i+1]
  return i+1


def main():
  l = [random.randint(0,1000) for r in range(1000000)]
  quick_sort(l)


if __name__ == "__main__":
  main()
