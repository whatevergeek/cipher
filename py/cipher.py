import js
from pyodide import create_proxy

def get_ascii(letter, start_letter, end_letter, distance):
  asciicode = ord(letter)+distance
  while (asciicode > ord(end_letter)):
      asciicode -= 26
  while (asciicode < ord(start_letter)):
      asciicode += 26
  return asciicode
  
def shift(letter, distance):
  if(ord(letter) >= ord('a') and ord(letter) <= ord('z')):
      return chr(get_ascii(letter, 'a', 'z', distance))
  elif (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
      return chr(get_ascii(letter, 'A', 'Z', distance))
  else:
      return letter

def print_result(evt):
    distance = int(js.distance.value)
    sentence = js.sentence.value
    encrypted_sentence = ""
    for letter in sentence:
        encrypted_sentence += shift(letter, distance)
    
    js.document.getElementById("result").innerHTML = f"<p><b>Encrypted Version:</b> {encrypted_sentence}</p>"

print_result_proxy = create_proxy(print_result)
js.document.getElementById("btnEncrypt").addEventListener ('click', print_result_proxy)

js.document.getElementById("result").innerHTML = f"<b>Ready to encrypt!</b>"