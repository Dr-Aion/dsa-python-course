import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.smallcat("Hello, " + sys.argv[1])
    