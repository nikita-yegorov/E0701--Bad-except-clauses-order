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
except Exception as e:
    print("Exception")

try:
    x = d['123']
except Exception as e:
    print("Exception")
except KeyError as ke:
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
except AssertionError as ae:
    print('The linux_interaction() function was not executed')


try:
    linux_interaction()
except AssertionError as ae:
    print('AssertionError')
    print('The linux_interaction() function was not executed')
except Exception as e:
    pass

















