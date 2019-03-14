
from string import whitespace, punctuation
title = "Section 5: Rewrinting and Immutable String"
title_list = list(title)

colon_position = title_list.index(":")
del title_list[:colon_position+1]
for position in range(len(title_list)):
    if title_list[position] in whitespace+punctuation:
        title_list[position]="_"
title = ''.join(title_list)
print(title)
title_list.insert(0, "PREFIX")
title = ''.join(title_list)
print (title)