from tkinter import *
from bs4 import BeautifulSoup
import requests as rq
from tkinter import font
from tkhtmlview import HTMLLabel
from urllib.request import urlopen
from tkinter import messagebox

r = Tk()

r.grab_set()

r.geometry('800x800')

r.title('Covid-19 Informer')
r.iconbitmap('pics//c19.ico')

cnts = []

info = Menu(r)

r.config(menu=info)

connected = True

try:
	urlopen('https://www.google.com')
except:
	messagebox.showerror('No internet!', 'Sorry! You do not have internet connection! The app will close now')
	r.deiconfiy()
	r.destroy()
	r.quit()
	connected = False

if connected:
	totalsource = rq.get('https://www.worldometers.info/coronavirus').text.encode('utf-8')


	def	create_another(tc, td, tr):
		top = Toplevel()
		top.iconbitmap('pics//c19.ico')
		top.title('Covid-19 Informer')
		top.geometry('900x220')
		top.config(bg='black')
		l = Label(top, fg='white',bg='black',font=('Helvetica', 22),text=f'These are the total stats of the coronavirus from all over the world!\n\n\nTotal cases: {tc},\nTotal deaths: {td},\nTotal recoveries: {tr}\n')
		l.grid(row=0,column=0)

	def totalCases():
		sp = BeautifulSoup(totalsource, 'lxml')
		totaldata = sp.find_all('div', id='maincounter-wrap')
		for i in totaldata:
			if i.h1.text == 'Coronavirus Cases:':
				total_cases = i.div.span.text
			if i.h1.text == 'Deaths:':
				total_deaths = i.div.span.text
			if i.h1.text == 'Recovered:':
				total_recovered = i.div.span.text

		create_another(total_cases, total_deaths, total_recovered)

	def about():
		top = Toplevel()
		top.iconbitmap('pics//c19.ico')
		top.title('Covid-19 Informer')
		top.geometry('535x500')
		top.config(bg='black')
		Label(top, fg='white',font=('Helvetica', 22), bg='black',text='Product Details\n\n').grid(row=0,column=0, padx=20, pady=20)
		Label(top, fg='white',font=('Helvetica', 22), bg='black',text='App-name : Covid-19 Stats-giver\nApp-license under : Adistar-964\nApp-creator : Ali\nApp created at : 24 Sep 2020\ndata taken from : www.worldometers.info').grid(row=1, column=0)

	def cntav():
		global cnts
		top = Toplevel(bg='black')
		top.iconbitmap('pics//c19.ico')
		top.title('Covid-19 Informer')
		top.geometry('500x500')
		top.resizable(False, False)
		bs = BeautifulSoup(totalsource, 'lxml')
		var = bs.find(attrs={"id":"main_table_countries_today"})
		val = var.find_all('tbody')[0].find_all('tr')
		for i in val:
			s = i.find_all('td', style="font-weight: bold; font-size:15px; text-align:left;")
			if s:
				for j in s:
					if j.a:
						cnts.append(j.a.text)

		scroll = Scrollbar(top, orient=VERTICAL)
		my_list = Listbox(top, width=37, height=20,
					yscrollcommand=scroll.set,
					font=('Helvetica', 18))
		my_list.pack(pady=10, side=LEFT, fill=BOTH)
		scroll.config(command=my_list.yview)
		scroll.pack(side=RIGHT, fill=Y)
		for i in cnts:
			my_list.insert(END, i)

	def helpp():
		top = Toplevel()
		top.iconbitmap('pics//c19.ico')
		top.title('Covid-19 Informer')
		top.geometry('920x500')
		Label(top, font=('Helvetica', 20),text="This will only tell you about what to do if your in need of serious help!\n\n\n").pack()
		Label(top, font=('Roboto', 16),text='If your country is not found, then check our available countries at "information>countries available"').pack()
		Label(top, font=('Roboto', 16),text='If you are still getting the same or the other issues, then report them to us').pack()

	info_bar = Menu(info, tearoff=False)
	info.add_cascade(label='more-info', menu=info_bar)
	info_bar.add_command(label='total cases', command=totalCases)

	our_bar = Menu(info, tearoff=False)
	info.add_cascade(label='information', menu=our_bar)
	our_bar.add_command(label='about us', command=about)
	our_bar.add_command(label='countries available', command=cntav)
	our_bar.add_command(label='Help', command=helpp)


	fontTitle = font.Font(family="Helvetica",size=30,weight="bold") 
	Label(r, text='  Covid-19 Stats-giver', 
			font=fontTitle,
			fg='gray31').grid(row=0, column=0)

	ent = Entry(r, width=20, borderwidth=4,
				 font=('Roboto', 24),
				  highlightbackground='black',
				  highlightthickness=2)

	ent.grid(row=1, column=0,padx=20, pady=40)

	string = '             '
	Label(r, text=string).grid(row=1, column=2)

	def tellStats():
		global cnts
		country = ent.get().lower().strip()

		url = f'https://www.worldometers.info/coronavirus/country/{country}'

		src = rq.get(url).text.encode('utf-8')
		soup = BeautifulSoup(src, 'lxml')

		total = soup.find_all("div",
					 id="maincounter-wrap")
		deaths = ''
		cases = ''
		recovered = ''
		for i in total:
			if i.h1 != None:
				if i.h1.text == 'Deaths:':
					deaths = i.div.span.text.strip()
				if i.h1.text == 'Coronavirus Cases:':
					cases = i.div.span.text.strip()
				if i.h1.text == 'Recovered:':
					recovered = i.div.span.text.strip()
		text = StringVar()
		stats = Label(r, width=60,
					  font=('Roboto', 16))
		if cases:
			stats.config(text = 'cases are ' + cases+ ', recoveries are ' + recovered + ', deaths are ' + deaths )
		else:
			if len(ent.get().strip()) == 0:
				stats.config(text = "Provide a Country's name to get its stats!")
			elif country not in cnts:
				stats.config(text = 'Incorrect country name entered!')
		stats.grid(row=2, column=0, columnspan=4) 
	btn = Button(r, text='check', padx=45,
				 pady=5,
				 font=('Roboto', 14),
				  bg='black', fg='white',
				  command=tellStats)

	btn.grid(row=1, column=1, padx=20)

	r.mainloop()