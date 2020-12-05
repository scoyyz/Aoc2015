import hashlib

key = 'ckczppom'
i = 0
while True:
  input = key + str(i)
  hash = hashlib.md5(input.encode())
  hex = hash.hexdigest()
  test = str(hex)[:6]
  if test == '000000':
    print(i)
    break
  i += 1