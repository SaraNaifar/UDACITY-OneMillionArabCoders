import time
import webbrowser
print('this program start at ' + time.ctime())

break_number= 3
count_break=0

while(count_break < break_number):
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=8HnLRrQ3RS4')
	count_break+=1
