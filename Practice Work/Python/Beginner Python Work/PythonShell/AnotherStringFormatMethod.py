#Formulating Strings using the format() method

'''
The syntax goes:
"string to be formatted".format(values/variables to be inserted into string, seperated by commas)
When using the format method, we don't use %s, %f or %d as placeholders
Instead, we use curly brackets:
'''

message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
print (message)

'''
When we write format(‘Apple’, 1299, 1.235235245), we
are passing in three parameters to the format() method.

Parameters are data that the method needs in order to perform its
task. The parameters are ‘Apple’, 1299 and 1.235235245.

The parameter ‘Apple’ has a position of 0,
1299 has a position of 1 and
1.235235245 has a position of 2.

Positions always start from ZERO.

When we write {0:s}, we are asking the interpreter to replace {0:s}
with the parameter in position 0 and that it is a string (because the
formatter is ‘s’).

When we write {1:d}, we are referring to the parameter in position 1,
which is an integer (formatter is d).

When we write {2:4.2f}, we are referring to the parameter in position
2, which is a float and we want it to be formatted with 2 decimal
places and a total length of 4 (formatter is 4.2f).

'''

#Without formatting the string:

message2 = 'The price of this {} laptop is {} USD and the exchange rate is {} USD to 1 EUR'.format('Apple', 1299, 1.25125145)
print (message2)

mess1 = '{0} is easier than {1}'.format('Python', 'Java')
mess2 = '{1} is eaiser than {0}'.format('Python', 'Java')
mess3 = '{:10.2f} and {:d}'.format(1.23423423412, 12)
mess4 = '{}'.format(1.234234234)

print(mess1)
print(mess2)
print(mess3)
print(mess4)
