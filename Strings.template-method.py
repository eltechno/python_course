
from string import Template

my_string = Template('Data science has been called $identifier')
my_string.substitute(identifier="sexiest job of the 21st century")

job= "Datascience"
name ="sexiest job of the 21st century"

my_string2= Template('$title has been called $description')
my_string2.substitute(title=job, description=name)

