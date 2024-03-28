# Made By Brooks Bentley And William Patton
# Empowering Visions, Unleashing Potential
# "With great power comes great responsibility"

from imports import *

def printer(text, speed):
  delay = []
  for i in text:
      delay.append(random.randint(1,9))
  for char,d in list(zip(text,delay)):
      sys.stdout.write(char)
      sys.stdout.flush()
      time.sleep(d/speed)

  if "\n" not in text[-1]:
    sys.stdout.write('\n')  # Add newline if not present at the end of the text
    sys.stdout.flush()