cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'
# Adding a string to a list. Prints as 'o', 'k', 'e' The string needs to have a trailing comma 'Oke',
cheese += 'Oke',
print(cheese)
# Append only takes one argument
cheese += 'raclette', 'halloumi'
cheese[:0]='edam', 'gouda'
cheese.extend(['gruyere', 'red leicester'])
print(cheese)

