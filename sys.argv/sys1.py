import sys
import mysys

clear_screen()


sa = sys.argv
if len(sa)<2:
	sys.exit()
with open(sa[1],'r',encoding='utf-8') as file:
	for line in file:
		print(line)
