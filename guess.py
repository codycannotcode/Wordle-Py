import words

class Guess():
  normal = '\033[0m'
  green = '\033[1;102m'
  yellow = '\033[1;103m'
  strikethrough = '\033[9;90m'
  used_letters = []

  @classmethod
  def init(cls):
    letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    for letter in letters:
      cls.used_letters.append(Letter(letter))
  
  def __init__(self, word, correct):
    word = word.upper()
    correct = correct.upper()
    self.word = []
    self.correct = True
    for l in word:
      self.word.append(Letter(l))
    
    #we need to check for greens first because they take precedence over yellows
    for i, l in enumerate(word):
      if l == correct[i]:
        self.word[i].status = Letter.in_place
        correct = f"{correct[:i]}_{correct[i+1:]}"
        self.updateList(l, Letter.in_place)
      else:
        self.correct = False

    #now check for yellows
    for i, l in enumerate(word):
      if l in correct and self.word[i].status != Letter.in_place:
        self.word[i].status = Letter.contains
        index = correct.find(l)
        correct = f"{correct[:index]}_{correct[index+1:]}"
        self.updateList(l, Letter.contains)
      else:
        self.updateList(l, Letter.absent)

  def display(self):
    output = ""
    for l in self.word:
      if l.status == Letter.in_place:
        output += f"{self.green}{l.letter}{self.normal} "
      elif l.status == Letter.contains:
        output += f"{self.yellow}{l.letter}{self.normal} "
      else:
        output += f"{l.letter} "
    print(output)

  @staticmethod
  def verify(guess, wordlist):
    return len(guess) == 5 and guess in wordlist

  def debug(self):
    for l in self.word:
      print(f"Letter: {l.letter}, Status: {l.status}")

  @classmethod
  def display_letters(cls):
    output = ''
    
    for l in cls.used_letters:
      if l.status == Letter.unguessed:
        output += f"{l.letter} "
      elif l.status == Letter.contains:
        output += f"{cls.yellow}{l.letter}{cls.normal} "
      elif l.status == Letter.in_place:
        output += f"{cls.green}{l.letter}{cls.normal} "
      else:
        output += f"{cls.strikethrough}{l.letter}{cls.normal} "
      if l.letter == 'P' or l.letter == 'L':
        output += '\n'

    print(output)

  @classmethod
  def updateList(cls, letter, status):
    for i, l in enumerate(cls.used_letters):
      if l.letter == letter:
        if l.status < status:
          l.status = status

  @classmethod
  def debugList(cls):
    output = ''
    for l in cls.used_letters:
      status = ''
      if l.status == Letter.unguessed:
        status = 'unguessed'
      elif l.status == Letter.contains:
        status = 'yellow'
      elif l.status == Letter.in_place:
        status = 'green'
      else:
        status = 'crossed'
      output += f"{l.letter}: {status} "
    print(output)

class Letter():
  unguessed = 0
  absent = 1
  contains = 2
  in_place = 3
  
  def __init__(self, letter, status=0):
    self.letter = letter
    self.status = status