# here we are discussing regex library
# rege is used to make or evaluate strings and set some rules

import re
statement = "He told me, 'I will work for you' "

new = re.sub('[a-z]','', statement)
print(new)

# here is how we can set rules to analyze strings
