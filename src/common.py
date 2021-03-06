import os

VERSION = (0, 4, 0)
VERSION_STR = '.'.join(str(num) for num in VERSION)

def str_to_tuple(s):
        return tuple(int(x) for x in s.split('.'))

def get_data_dir():
	p = os.path.abspath(__file__)
	p = os.path.dirname(p)
	p = os.path.join(p, 'data')
	return p
