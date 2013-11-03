start = 0
substrings = []
for i in range(len(s)):
  if i != 0 and (ord(s[i]) < ord(s[i - 1])):
    start = i
  substrings.append(s[start : i + 1])

longest_substring = substrings[0]
for substring in substrings:
  if len(longest_substring) < len(substring):
    longest_substring = substring

print longest_substring
