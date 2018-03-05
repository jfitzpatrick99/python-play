

def merge_sort(l):
  if len(l) == 1:
    return l

  middle = int(len(l) / 2)

  left = l[0:middle]
  right = l[middle:len(l)]

  left = merge_sort(left)
  right = merge_sort(right)

  l = merge(left, right)
  return l


def merge(left, right):
  merged = []

  l = 0
  r = 0

  while l < len(left) or r < len(right):
    if l < len(left) and r < len(right):
      if left[l] < right[r]:
        merged.append(left[l])
        l = l+1
      else:
        merged.append(right[r])
        r = r+1
    else:
      if l < len(left):
        merged.append(left[l])
        l = l+1
      if r < len(right):
        merged.append(right[r])
        r = r+1

  return merged


def main():
  l = [1, 5, 3, 6, 9]
  l = merge_sort(l)
  print(l)


if __name__ == "__main__":
  main()
