# Define a function which will require a name to be passed as an arguement.

def greetMe(name):
    greeting = 'Hi {}! How are you today?'.format(name)
    print(greeting)

greetMe("Ste")