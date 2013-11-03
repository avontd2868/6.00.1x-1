count = 0
for index in range(len(s) - 2):
  if s[index : index + 3].lower() == 'bob':
    count += 1
print count
