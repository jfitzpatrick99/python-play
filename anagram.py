

def is_anagram(word1, word2):
  if len(word1) != len(word2):
    return False

  d = {}
  for c in word1:
    if c in d:
      count = d[c]
      count = count + 1
      d[c] = count
    else:
      d[c] = 1

  for c in word2:
    if c in d:
      count = d[c]
      count = count - 1
      if count == 0:
        del d[c]
      elif count < 0:
        return False
      else:
        d[c] = count
    else:
      return False

  return not bool(d)


def main():
  word_tuples = [("listen", "silent"), ("foo", "bar"), ("aadrr", "radar")]
  for word_tuple in word_tuples:
    print("{} and {} is_anagram: {}".format(word_tuple[0],
                                            word_tuple[1],
                                            is_anagram(word_tuple[0], word_tuple[1])))


if __name__ == "__main__":
  main()
