#String Stuff
'''
To declare a string, you can either use variableName =
‘initial value’ (single quotes) or variableName =
“initial value” (double quotes)

To declare a string, you can either use variableName =
‘initial value’ (single quotes) or variableName =
“initial value” (double quotes)

Make sure to use quotes or else it will be identified as an integer

We can combine multiple substrings by using the concatenate sign
(+). For instance, “Peter” + “Lee” is equivalent to the string
“PeterLee”.

Some String Methods

upper() -- capitalizes all letters in a string

Formatting Strings using the % Operator

Strings can also be formatted using the % operator. This gives you
greater control over how you want your string to be displayed and
stored. The syntax for using the % operator is

“string to be formatted” %(values or variables to
be inserted into string, separated by commas)


'''


brand = 'Apple'
exchangeRate = 1.235235245
message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
print (message)

#% is used for placeholders in the string
'''
%s is for strings
%d is for integer
If we want to add spaces before an integer, we can add a number between % and d to indicate the desired length of the strong
E.x: %5d %(123) will give us "  123" with sp spaces in the front and a total length of 5
&f for floats
Here we used $4.2f where 4 refers to the TOTAL LENGTH and 2 refers to 2 DECIMAL PLACES

If we want to add spaces before the
number, we can format is as %7.2f, which will give us “ 1.24” (with
2 decimal places, 3 spaces in front and a total length of 7).

'''
