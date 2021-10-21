import sys
import time

indent = 0

indentIncreasing = True


try:
    while True:
        print(' ' * indent, end='')
        print('**********')
        time.sleep(0.1)  # Pauses for 1/10 of a second

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= indent - 1
            if indent <= 20:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
