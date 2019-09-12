import os

def clear_screen():
	if os.name == 'nt':
		os.system('CLS')
	else:
		os.system('clear')
