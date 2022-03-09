def load():
  with open('five.txt') as f:
    words = f.read().splitlines()
  return words