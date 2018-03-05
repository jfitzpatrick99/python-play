

def bubble_sort(l):
  for i in range(len(l)):
    for j in range(i, len(l)):
      if l[j] < l[i]:
        l[i], l[j] = l[j], l[i]

  return l


def main():
  l = [3, 8, 1, 10, 4, 2, 2]
  print(l)
  bubble_sort(l)
  print(l)


if __name__ == "__main__":
  main()
