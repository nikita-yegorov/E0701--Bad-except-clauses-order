try:
    5 / 0
except Exception as e:
    print("Exception")
# unreachable code!
except ZeroDivisionError as zde:
    print("ZeroDivisionError")


try:
    5 / 0
except ZeroDivisionError as zde:
    print("ZeroDivisionError")
except Exception as e:
    print("Exception")






d = {}

try:
    x = d['123']
except KeyError as ke:
    print('KeyError')


try:
    x = d['123']
except Exception as e:
    print("Exception")
except KeyError as e:
    print("ZeroDivisionError")






import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


try:
    assert ('linux' in sys.platform)
    linux_interaction()
except Exception as e:
    pass
except AssertionError as error:
    print('The linux_interaction() function was not executed')


try:
    linux_interaction()
except AssertionError as error:
    print('AssertionError')
    print('The linux_interaction() function was not executed')
except Exception as e:
    pass

















