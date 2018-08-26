import os 

def rename_files():
	file_path = r'C:\Users\ASUS\Desktop\OMAC\UDACITY-OneMillionArabCoders\MiniProject_Secret_Message\alphabet'
	files_list = os.listdir(file_path)
	current_dir = os.getcwd()
	os.chdir(r'C:\Users\ASUS\Desktop\OMAC\UDACITY-OneMillionArabCoders\MiniProject_Secret_Message\alphabet')
	for file_name in files_list:
		new_name = file_name.translate(None, "0123456789")
		os.rename(file_name,new_name)
	os.chdir(current_dir)


print  rename_files()
os.system('pause')