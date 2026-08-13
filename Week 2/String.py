s = 'Chennai'
print(s)
# Output: 'Chennai'
type(s)
# Output: <class 'str'>

title = "Hitchhiker's"
print(title)
# Output: "Hitchhiker's"

myquote = '''He said his favourite book is "Hitchhiker's Guide to the Galaxy"'''
print(myquote)
# Output: 'He said his favourite book is "Hitchhiker\'s Guide to the Galaxy"'

multi_line_string = '''First line
Second line
Third line'''
print(multi_line_string)
# Output:
# First line
# Second line
# Third line

s = "hello"
s[0] # Output: 'h'
s[1] # Output: 'e'

s[-1] # Output: 'o'
s[-2] # Output: 'l'


s[1:4] # Output: 'ell' (characters at index 1, 2, 3)

s[:3] # Output: 'hel' (characters at index 0, 1, 2)

s[2:] # Output: 'llo' (characters at index 2, 3, 4)

s[3:1] # Output: '' (empty string)
s[0:7] # Output: 'hello' (goes up to the last character)

s = "hello"
t = "there"
combined = s + t
print(combined)
# Output: 'hellothere'

spaced_combined = s + " " + t
print(spaced_combined)
# Output: 'hello there'

s = "hello"
length_s = len(s)
print(length_s)
# Output: 5

s = "hello"
# To change "hello" to "help!"
new_s = s[0:3] + "p!"
print(new_s)
# Output: 'help!'