message = 'Hello World'
print(message)

print(len(message))
print(message[0])
print(message[0:5])
print(message[6:5])

print(message.lower())
print(message.upper())

print(message.count('Hello'))
print(message.count('l'))
print(message.find('Hello'))

new_message = message.replace('World', 'Universe')
print(new_message)

my_message = 'Hello World'
print(my_message)

message2 = 'Bobby\'s World'
print(message2)

message3 = "Bobby's World"
print(message3)

message4 = """Bobby's World Was A Good
Show In The 1990's"""
print(message4)

greeting = 'Hello'
name = 'Michael'

message5 = greeting + ', ' + name + '. Welcome!'
print(message5)

message6 = '{}, {}. Welcome!'.format(greeting, name)
print(message6)

message7 = f'{greeting}, {name}. Welcome!'
print(message7)

# print(help(str))
