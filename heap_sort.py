

def max_heapify(l, i, s):
  left = 2 * i
  right = 2 * i + 1
  largest = None
  if left < s and l[left] > l[i]:
    largest = left
  else:
    largest = i
  if right < s and l[right] > l[largest]:
    largest = right
  if largest != i:
    l[i], l[largest] = l[largest], l[i]
    max_heapify(l, largest, s)
  return l


def build_max_heap(l):
  for i in range(int(len(l) / 2), -1, -1):
    max_heapify(l, i, len(l))
  return l


def heapsort(l):
  build_max_heap(l)
  heap_size = len(l)
  for i in range(len(l)-1, 0, -1):
    l[0], l[i] = l[i], l[0]
    heap_size = heap_size - 1
    max_heapify(l, 0, heap_size)
  return l


def main():
  l = [3, 8, 1, 10, 4, 2, 2]
  print(l)
  heapsort(l)
  print(l)


if __name__ == "__main__":
  main()
