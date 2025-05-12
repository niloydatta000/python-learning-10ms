# Introduction of static method in OOP
# Encapsulation of related functions in one class

class Number:

    def odd(num):
        return num % 2 != 0

    def even(num):
        return num % 2 == 0

    def doesContainZERO(num):
        '''return "0" in str(num)''' # Short-Hand syntax

        '''
        We had better use an universal (more comprehensive) syntax than short-hand syntax method.
        Universal methods are applied in professional projects so that a new programmer could understand properly.
        It is a matter of professionalism. Mastering short-hand methods is a matter of skill though.
        '''

        # A universal syntax is given below:

        for digit in str(num):
            if digit == "0":
                return True
        return False # N.B :We avoided else statement with proper indentation

oddUserInput = int(input("Enter an odd integer to verify as True or False: "))
evenUserInput = int(input("Enter an even integer to verify as True or False: "))
print("Press '0':")
digitUserInput = input(" ")

'''
We use simple "." in static method to execute class operation.
No object is required here.
'''

print(Number.odd(oddUserInput))
print(Number.even(evenUserInput))
print(Number.doesContainZERO(digitUserInput))