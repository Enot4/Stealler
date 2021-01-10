import os

def Builder():

	dir_file = input('Введите путь к папке со стиллером: ')
	dir_ico = input('Введите путь к значку, который хотите установить: ')

	os.system('pip install pyinstaller')
	goto_dir = 'cd' + dir_file
	os.system(goto_dir)
	pyinst_sys = 'pyinstaller -F -i ' + dir_ico + ' stealer.py'
	os.system(pyinst_sys)

Builder()
