import random


def quick_sort(l):
  help_quick_sort(l, 0, len(l) - 1)
  return l


def help_quick_sort(l, start, end):
  if start < end:
    i = partition(l, start, end)

    help_quick_sort(l, start, i - 1)
    help_quick_sort(l, i + 1, end)


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

