from fst import FST
import string, sys
from fsmutils import composechars, trace

def letters_to_numbers():
    """
    Returns an FST that converts letters to numbers as specified by
    the soundex algorithm
    """

    # Let's define our first FST
    f1 = FST('soundex-generate')

    # Indicate that '1' is the initial state
    f1.add_state('start')
    f1.add_state('next')
    f1.add_state('next0')
    f1.add_state('next1')
    f1.add_state('next2')
    f1.add_state('next3')
    f1.add_state('next4')
    f1.add_state('next5')
    f1.add_state('next6')
    f1.initial_state = 'start'

    # Set all the final states
    f1.set_final('next0')
    f1.set_final('next1')
    f1.set_final('next2')
    f1.set_final('next3')
    f1.set_final('next4')
    f1.set_final('next5')
    f1.set_final('next6')
    
    group0 = ['a','e','h','i','o','u','w','y','A','E','H','I','O','U','W','Y']
    group1 = ['b','f','p','v','B','F','P','V']
    group2 = ['c','g','j','k','q','s','x','z','C','G','J','K','Q','S','X','Z']
    group3 = ['d','t','D','T']
    group4 = ['l','L']
    group5 = ['m','n','M','N']
    group6 = ['r','R']

    # Add the rest of the arcs
    for letter in string.letters:
     
        if(letter in group0):
            f1.add_arc('start', 'next0', (letter), (letter))
               
            f1.add_arc('next', 'next0', (letter), ())
            f1.add_arc('next0', 'next0', (letter), ())
            
            f1.add_arc('next1', 'next0', (letter), ())
            f1.add_arc('next2', 'next0', (letter), ())
            f1.add_arc('next3', 'next0', (letter), ())
            f1.add_arc('next4', 'next0', (letter), ())
            f1.add_arc('next5', 'next0', (letter), ())
            f1.add_arc('next6', 'next0', (letter), ())
                 
        elif(letter in group1):
            f1.add_arc('start', 'next1', (letter), (letter))
            
            f1.add_arc('next', 'next1', (letter), ('1'))
            f1.add_arc('next1', 'next1', (letter), ())
            
            f1.add_arc('next0', 'next1', (letter), ('1'))
            f1.add_arc('next2', 'next1', (letter), ('1'))
            f1.add_arc('next3', 'next1', (letter), ('1'))
            f1.add_arc('next4', 'next1', (letter), ('1'))
            f1.add_arc('next5', 'next1', (letter), ('1'))
            f1.add_arc('next6', 'next1', (letter), ('1'))
         
        elif(letter in group2):
            f1.add_arc('start', 'next2', (letter), (letter))
            
            f1.add_arc('next', 'next2', (letter), ('2'))
            f1.add_arc('next2', 'next2', (letter), ())
            
            f1.add_arc('next0', 'next2', (letter), ('2'))
            f1.add_arc('next1', 'next2', (letter), ('2'))
            f1.add_arc('next3', 'next2', (letter), ('2'))
            f1.add_arc('next4', 'next2', (letter), ('2'))
            f1.add_arc('next5', 'next2', (letter), ('2'))
            f1.add_arc('next6', 'next2', (letter), ('2'))            
        
        elif(letter in group3):
            f1.add_arc('start', 'next3', (letter), (letter))
            
            f1.add_arc('next', 'next3', (letter), ('3'))
            f1.add_arc('next3', 'next3', (letter), ())
            
            f1.add_arc('next0', 'next3', (letter), ('3'))
            f1.add_arc('next1', 'next3', (letter), ('3'))
            f1.add_arc('next2', 'next3', (letter), ('3'))
            f1.add_arc('next4', 'next3', (letter), ('3'))
            f1.add_arc('next5', 'next3', (letter), ('3'))
            f1.add_arc('next6', 'next3', (letter), ('3'))
            
        elif(letter in group4):
            f1.add_arc('start', 'next4', (letter), (letter))
            
            f1.add_arc('next', 'next4', (letter), ('4'))
            f1.add_arc('next4', 'next4', (letter), ())
            
            f1.add_arc('next0', 'next4', (letter), ('4'))
            f1.add_arc('next1', 'next4', (letter), ('4'))
            f1.add_arc('next2', 'next4', (letter), ('4'))
            f1.add_arc('next3', 'next4', (letter), ('4'))
            f1.add_arc('next5', 'next4', (letter), ('4'))
            f1.add_arc('next6', 'next4', (letter), ('4'))

        elif(letter in group5):
            f1.add_arc('start', 'next5', (letter), (letter))
            
            f1.add_arc('next', 'next5', (letter), ('5'))
            f1.add_arc('next5', 'next5', (letter), ())
            
            f1.add_arc('next0', 'next5', (letter), ('5'))
            f1.add_arc('next1', 'next5', (letter), ('5'))
            f1.add_arc('next2', 'next5', (letter), ('5'))
            f1.add_arc('next3', 'next5', (letter), ('5'))
            f1.add_arc('next4', 'next5', (letter), ('5'))
            f1.add_arc('next6', 'next5', (letter), ('5'))          

        elif(letter in group6):
            f1.add_arc('start', 'next6', (letter), (letter))
            
            f1.add_arc('next', 'next6', (letter), ('6'))
            f1.add_arc('next6', 'next6', (letter), ())
            
            f1.add_arc('next0', 'next6', (letter), ('6'))
            f1.add_arc('next1', 'next6', (letter), ('6'))
            f1.add_arc('next2', 'next6', (letter), ('6'))
            f1.add_arc('next3', 'next6', (letter), ('6'))
            f1.add_arc('next4', 'next6', (letter), ('6'))
            f1.add_arc('next5', 'next6', (letter), ('6'))            

    return f1

    # The stub code above converts all letters except the first into '0'.
    # How can you change it to do the right conversion?

def truncate_to_three_digits():
    """
    Create an FST that will truncate a soundex string to three digits
    """

    # Ok so now let's do the second FST, the one that will truncate
    # the number of digits to 3
    f2 = FST('soundex-truncate')

    # Indicate initial and final states
    f2.add_state('start')
    f2.add_state('digit1')
    f2.add_state('digit2')
    f2.add_state('digit3')
    
    f2.initial_state = 'start'
    f2.set_final('digit1')
    f2.set_final('digit2')
    f2.set_final('digit3')

    # Add the arcs
    for letter in string.letters:
        f2.add_arc('start', 'start', (letter), (letter))

    for n in range(10):
        f2.add_arc('start', 'digit1', (str(n)), (str(n)))
        f2.add_arc('digit1', 'digit2', (str(n)), (str(n)))
        f2.add_arc('digit2', 'digit3', (str(n)), (str(n)))
        f2.add_arc('digit3', 'digit3', (str(n)), ())

    return f2

    # The above stub code doesn't do any truncating at all -- it passes letter and number input through
    # what changes would make it truncate digits to 3?

def add_zero_padding():
    # Now, the third fst - the zero-padding fst
    f3 = FST('soundex-padzero')

    f3.add_state('1')
    f3.add_state('a')
    f3.add_state('1a')
    f3.add_state('1b')
    f3.add_state('2')
    
    f3.initial_state = '1'
    f3.set_final('2')

    for letter in string.letters:
        f3.add_arc('1', '1', (letter), (letter))

    
    f3.add_arc('1', '1a', (), ('0'))
    f3.add_arc('1a', '1b', (), ('0'))
    f3.add_arc('1b', '2', (), ('0'))        
    
    for number in xrange(10):
        f3.add_arc('1', '1a', (str(number)), (str(number)))
        f3.add_arc('1a', '1b', (str(number)), (str(number)))
        f3.add_arc('1b', '2', (str(number)), (str(number)))

    return f3

    # The above code adds zeroes but doesn't have any padding logic. Add some!

if __name__ == '__main__':
    user_input = raw_input().strip()
    f1 = letters_to_numbers()
    f2 = truncate_to_three_digits()
    f3 = add_zero_padding()

    if user_input:
        print("%s -> %s" % (user_input, composechars(tuple(user_input), f1, f2, f3)))
