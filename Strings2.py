

double = "She said, \"that's a greate tasting apple!\""

print (double)

single = 'she said, "that\'s a great tasting apple!"'
print (single)

print (' i ' + 'eat ' + 'you') #concatenation

first = "I"
second = "EAT"
third = "python"

sentence = first + ' ' + second +' ' + third
print(sentence)

print ('-' * 50) # hacer una linea con 50 guiones

happines = "happy " * 3
print(happines)

version = 3
print ("this is python" + str(version) + ".")
print ("THIS is python{}." .format(version)) # aqui otro metodo utilizando .format

# formating strings with .format

print("I {} Python".format('love'))
print("{} {} {}".format("I", "love", "python")) # con .format en cada lleve se reemplaza por cada palabra en format

print ("I {0} {1}. {1} {0}s me." .format("love", "python")) # se puede decidir que palabra va en las llaves y el orden

print ('{} {} {}.' .format(first, second, third)) # con las variables de arriba

#{0:8} use the first character and make 8 characters wide
#formating strings alignment
# < left
# ^ center
#> right

print ('{0:^8} | {1:^8}'.format('Fruit', 'Quantity'))
print ('{0:<8} | {1:<8}'.format('Apple', '3.333'))
print ('{0:<8} | {1:^8}'.format('Orange', '10'))

fruit = input('Enter the name of a fruit ')
print ('{} is a loverly fruit.' .format(fruit) )

