import re
#positive lookaround
my_text =" tweets.txt transferred, mypass.txt transferred, keyworkds.txt error"
print( re.findall(r"\w+\.txt(?=\stransferred)", my_text))

#negative lookaround
print( re.findall(r"\w+\.txt(?!\stransferred)", my_text))

#positive lookbehind
my_text2 = "Member: Angus Young, Member: Chris Slade, Past: Malcom Young, Past: Cliff Williams"
print (re.findall(r"(?<=Member:\s)\w+\s\w+", my_text2))

#negative lookbehind
my_text3 = "My with cat sat at the table. However, my brown dog was lying on the couch."
print( re.findall(r"(?<!brown\s)(cat|dog)", my_text3))
