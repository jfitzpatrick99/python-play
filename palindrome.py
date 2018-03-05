

def is_palindrome(s):
  for i in range(len(s)):
    if s[i] != s[len(s) - i - 1]:
      return False

  return True


def main():
  ss = ["ascsa", "radar", "hello", "a man a plan canal panama", "abba", "goodbye"]
  for i in range(len(ss)):
    print("{} is_palindrome: {}".format(ss[i], is_palindrome(ss[i])))


if __name__ == "__main__":
  main()
