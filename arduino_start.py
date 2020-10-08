from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

it = util.Iterator(board)
it.start()
