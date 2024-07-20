# "str".format -> works like a backtick(``) in javascript. assigns the argument in placeholder {}

#basic format
print("Hi! I am {}, {} from {}".format("Clement", "21", "Dalaguete"))

#accepts variables
name = "Clement"
age = 21
place = "Cebu"
print("Hi! I am {}, {} from {}".format(name, age, place))

# assigned values
print("Hi! I am {name}, {age} from {place}".format(name = "John", age = 20, place = "Argao"))
print("Hi! I am {place}, {age} from {name}".format(name = "John", age = 20, place = "Argao"))

#tabs
print("Hi! I am {place}, {age:>10} from {name:}".format(name = "John", age = 20, place = "Argao")) # default {:10}
print("Hi! I am {place}, {age:<10} from {name:}".format(name = "John", age = 20, place = "Argao")) # tab to teh right
print("Hi! I am {place}, {age:^10} from {name:}".format(name = "John", age = 20, place = "Argao")) # center
print("Hi! I am {place}, {age:.3f} from {name:}".format(name = "John", age = 20, place = "Argao")) # floating pint numbers
print("Hi! I am {place}, {age:b} from {name:}".format(name = "John", age = 20, place = "Argao")) # binary
print("Hi! I am {place}, {age:o} from {name:}".format(name = "John", age = 20, place = "Argao")) # octal
print("Hi! I am {place}, {age:x} from {name:}".format(name = "John", age = 20, place = "Argao")) # hex
