
from string import Template

my_string = Template('Data science has been called $identifier')
my_string.substitute(identifier="sexiest job of the 21st century")

job= "Datascience"
name ="sexiest job of the 21st century"

my_string2= Template('$title has been called $description')
my_string2.substitute(title=job, description=name)

#using the safe substitute will show the missing value insted of display an error
favorite = dict(flavor="chocolate")
my_string3 = Template('I like $flavor $cake very much')
#put only the dictionary nothing else
print(my_string3.safe_substitute(favorite))



tools = ['Natural Language Toolkit', '20', 'month']

# Select variables
our_tool = tools[0]
our_fee = tools[1]
our_pay = tools[2]

# Create template
course = Template("We are offering a 3-month beginner course on $tool just for $$ $fee ${pay}ly")

# Substitute identifiers with three variables
print(course.substitute(tool=our_tool, fee=our_fee, pay=our_pay))