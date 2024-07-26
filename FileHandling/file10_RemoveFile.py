
import os
if os.path.exists("person.txt"):
  os.remove("person.txt")
else:
  print("The file does not exist")

