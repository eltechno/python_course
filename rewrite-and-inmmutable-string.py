

title = "Recipe 5: Rewriting, and The Immutable String"
colon_position = title.index(":")
print(colon_position)
discard_text, post_colon_text = title[:colon_position], title[colon_position+1:]
print(discard_text)
print(post_colon_text)

pre_colon_text, _, post_colon_text = title.partition(":")
print(pre_colon_text)
print(post_colon_text)

#agregar un _ entre cada letra
post_colon_text =  post_colon_text.replace("", "_")
print(post_colon_text)

#otra forma de hacerlo
from string import whitespace, punctuation
for character in whitespace + punctuation:
    post_colon_text = post_colon_text.replace(character, "_")
print(post_colon_text)

post_colon_text = post_colon_text.lower()
print(post_colon_text)

post_colon_text = post_colon_text.capitalize()
print(post_colon_text)

post_colon_text = post_colon_text.strip("_")
print(post_colon_text)

while "__" in post_colon_text:
    post_colon_text = post_colon_text.replace("__","-")
print(post_colon_text)



title2 = "This is a test : Please stand by"  #string completo
again_Split = title2.index(":") #busca la posicion del caracter deseado
print(again_Split)
#variable1, Variable2 = parte de la string      , parte2 de la string
derecha, izquierda = title2[:again_Split].strip(), title2[again_Split+1:].strip()
print(derecha)
print(izquierda)
                     #the complete string title[:]
derecha, izquierda = title2[:].strip(), title2[again_Split+1:].strip()
print(derecha)

#imprime las letras de atras para adelante
for i in range(-1, -20, -1):
    print (i, title2[i])