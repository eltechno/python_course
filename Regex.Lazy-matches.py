"""
You need to keep working and cleaning your tweets dataset. You realize that there are some HTML tags present.
You need to remove them but keep the inside content as they are useful for analysis.

Let's take a look at this sentence containing an HTML tag:

I want to see that <strong>amazing show</strong> again!.

You know that for getting HTML tag you need to match anything that sits inside angle brackets < >.
But the biggest problem is that the closing tag has the same structure. If you match too much, you will end up
removing key information. So you need to decide whether to use a greedy or a lazy quantifier.

"""
import re
string = 'I want to see that <strong>amazing show</strong> again!'



# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print (string_notags)