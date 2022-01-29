def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"
    
    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)
    #raise NotImplementedError()

#Part A: Find a list of all of the names in the following string using regex.
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    
    return re.findall('[A-Z][a-z]+', simple_string)

    # YOUR CODE HERE
    # raise NotImplementedError()
assert len(names()) == 4, "There are four names in the simple_string"

#Part B: The dataset file in assets/grades.txt contains a line separated list of people with their grade in a class. Create a regex to generate a list of just those students who received a B in the course.
import re
def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()
    return re.findall('([A-Z]\S+ [A-Z]\S+): B', grades)
    # YOUR CODE HERE
    #raise NotImplementedError()

assert len(grades()) == 16

#part c: Consider the standard web log file in assets/logdata.txt. This file records the access a user makes when visiting a web page (like this one!). Each line of the log has the following items:
# a host (e.g., '146.204.224.152')
# a user_name (e.g., 'feest6811' note: sometimes the user name is missing! In this case, use '-' as the value for the username.)
# the time a request was made (e.g., '21/Jun/2019:15:45:24 -0700')
# the post request type (e.g., 'POST /incentivize HTTP/1.1' note: not everything is a POST!)
# Your task is to convert this into a list of dictionaries, where each dictionary looks like the following:
# example_dict = {"host":"146.204.224.152", 
#                 "user_name":"feest6811", 
#                 "time":"21/Jun/2019:15:45:24 -0700",
#                 "request":"POST /incentivize HTTP/1.1"}
import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
    req = re.findall('(\d+[.]\d+[.]\d+[.]\d+) - ([a-z-]\S*) [\[](\S+ -0700)\] "([A-Z]\S+ \/\S+ HTTP\/[0-9.]+)',logdata)
    
    l = []
    for i in req:
        l.append({'host': i[0],'user_name': i[1],'time': i[2],'request': i[3]})
    return l
    # YOUR CODE HERE
    #raise NotImplementedError()
    assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in log results, check your formating"
https://github.com/hoaint25/Intro_datascience_with_python.git