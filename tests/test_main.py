from lib.main import *

def test_main():
	assert(main() == 0)

def test_add_ints():
	assert(add_ints(1, 3) == 4)
