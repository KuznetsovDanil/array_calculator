from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Radiobutton  
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

arr = []
time_gen = 0.0
time_count = 0.0

def generation():
	global arr
	global time_gen
	gen_begin = time.time()
	type = ""
	if selected.get() == 1:
		type = "int"
	else:
		type = "float"
	oper = combo.get()
	operators = ['+', '-', '*', "/"]
	n = 0
	if txt.get().isdigit():
		n = int(txt.get())
	min = pow(10, 50)
	max = pow(10, 50)
	try:
		if txt1.get().isdigit():
			min = int(txt1.get())
		elif txt1.get()[0] == "-":
			if txt1.get()[1:].isdigit():
				min = -int(txt1.get()[1:])
		if txt2.get().isdigit():
			max = int(txt2.get())
		elif txt2.get()[0] == "-":
			if txt2.get()[1:].isdigit():
				max= -int(txt2.get()[1:])
	except Exception:
		pass
	arr.clear()
	if n <=100000000:
		if oper in operators and n != 0 and abs(min) < pow(10, 50) and abs(max) < pow(10, 50) and min<=max:
			try:
				if type == 'int':
					arr = [round(random.random()*(max-min)+min) for i in range(n)]
					if oper != "/":
						for i in range(n):
							if arr[i] == 0:
								arr[i] = 1
				elif type == 'float':
					arr = [random.random()*(max-min)+min for i in range(n)]
					if oper != "/":
						for i in range(n):
							if arr[i] == 0.0:
								arr[i] = 1.0
			except MemoryError:
				messagebox.showerror('Внимание!', 'Недостаточно памяти!')
			except Exception:
				messagebox.showerror('Внимание!', 'Ошибка при генерации!')
		else:
			messagebox.showerror('Внимание!', 'Неверный ввод данных!')
	else:
		messagebox.showerror('Внимание!', 'Слишком большой массив!')
	time_gen = time.time() - gen_begin
	txt3.delete(1.0, END)
	txt3.insert(INSERT, type)
	txt4.delete(1.0, END)
	txt4.insert(INSERT, oper)
	txt5.delete(1.0, END)
	txt5.insert(INSERT, str(n))
	txt6.delete(1.0, END)
	txt6.insert(INSERT, str(round(time_gen, 7)))

if_file = 0
if_auto = 0

def if_write():
	global if_file
	if chkb.get() == 0:
		if_file = 0
	elif chkb.get() == 1:
		if_file = 1

def if_test():
	global if_auto
	if chkb.get() == 0:
		chkb1.set(0)
	if chkb1.get() == 0:
		if_auto = 0
	elif chkb1.get() == 1:
		if_auto = 1

def count():
	global arr
	global time_gen
	global time_count
	wait_begin = time.time()
	wait = 0.0
	time_count = 0.0
	s = ""
	type = ""
	if selected.get() == 1:
		type = "int"
	else:
		type = "float"
	oper = combo.get()
	operators = ['+', '-', '*', "/"]
	n = 0
	if txt.get().isdigit():
		n = int(txt.get())
	min = pow(10, 50)
	max = pow(10, 50)
	try:
		if txt1.get().isdigit():
			min = int(txt1.get())
		elif txt1.get()[0] == "-":
			if txt1.get()[1:].isdigit():
				min = -int(txt1.get()[1:])
		if txt2.get().isdigit():
			max = int(txt2.get())
		elif txt2.get()[0] == "-":
			if txt2.get()[1:].isdigit():
				max= -int(txt2.get()[1:])
	except Exception:
		pass
	if n != 0:
		count_begin = time.time()
		res_mantiss, cur_res = float(arr[0]), float(arr[0])
		res_power, cur_pow = 0, 0
		res = ''
		if oper == "+":
			cur_res = sum(arr)
		elif oper == "-":
			cur_res -= sum(arr[1:])
		elif oper == "*":
			for i in range(1, n):
				cur_res *= arr[i]
				if abs(cur_res) >= pow(10.0, 50) or abs(cur_res) < pow(10.0, -20):
					while abs(cur_res) >= 10.0:
						cur_res /= 10.0
						cur_pow += 1
					while abs(cur_res) < 1.0 and cur_res != 0.0:
						cur_res *= 10.0
						cur_pow -= 1
		elif oper == '/':
			for i in range(1, n):
				if arr[i] != 0.0:
					cur_res /= arr[i]
					if abs(cur_res) >= pow(10.0, 50) or abs(cur_res) < pow(10.0, -20):
						while abs(cur_res) >= 10.0:
							cur_res /= 10.0
							cur_pow += 1
						while abs(cur_res) < 1.0 and cur_res != 0.0:
							cur_res *= 10.0
							cur_pow -= 1
				else:
					res_mantiss = 0.0
					res_power = 0
					res = 'Деление на 0!'
		while abs(cur_res) >= 10.0:
			cur_res /= 10.0
			cur_pow += 1
		while abs(cur_res) < 1.0 and cur_res != 0.0:
			cur_res *= 10.0
			res_power -= 1
		time_count = (time.time() - count_begin)
		f = open('array.txt', 'w')
		if if_file == 1:
			try:
				f = open('array.txt', 'w')
				for i in range(len(arr)):
					f.write(str(arr[i]) + "\n")
			except MemoryError:
				messagebox.showerror('Внимание!', 'Недостаточно памяти!')
			except Exception:
				messagebox.showerror('Внимание!', 'Ошибка при записи в файл!')
			finally:
				f.close()
		res_mantiss = cur_res
		res_power = cur_pow
		while res_power in range(1, 12):
			res_mantiss *= 10.0
			res_power -= 1
		while res_power in range(-4, 0):
			res_mantiss /= 10.0
			res_power += 1
		if res_power == 0 and res != "Деление на 0!":
			if type == "int" and oper != "/":
				res = str(int(round(res_mantiss, 0)))
			elif res != "Деление на 0!":
				res = str(round(res_mantiss, 7))
		else:
			res = str(round(res_mantiss, 7)) + " * 10^(" + str(res_power) + ")"
		if if_auto == 1:
			autotest(type, n, min, max, oper, res)
		wait = time.time() - wait_begin
		s = (type + "  " + oper + "  " + str(n) + "  \t" + str(round(time_gen, 7)) + "  \t" + str(round(time_count, 7)) + "  \t" + str(round(wait, 7)) + "  \t" + res + "\n")
	else:
		messagebox.showerror('Внимание!', 'Массив отсутствует!')
	txt4.delete(1.0, END)
	txt4.insert(INSERT, oper)
	txt7.delete(1.0, END)
	txt7.insert(INSERT, str(round(time_count, 7)))
	txt8.delete(1.0, END)
	txt8.insert(INSERT, str(round(wait, 7)))
	txt9.delete(1.0, END)
	txt9.insert(INSERT, res)
	txt10.insert(INSERT, s)
							
def autotest(type, n, min_real, max_real, oper, res):
	global arr
	global time_gen, time_count
	elem, minim, maxim, aver = 0, 0, 0, 0.0
	for i in range(n):
		arr[i] = float(arr[i])
	elem = len(arr)
	minim = min(arr)
	maxim = max(arr)
	if type == "int":
		minim = int(minim)
		maxim = int(maxim)
	aver = sum(arr) / elem
	try:
		tt = open('test.txt', 'a')
		tt.write(str(datetime.datetime.now()) + '\n')
		tt.write('Сгенерировано: ' + str(elem) + " " + type + " для " + oper + '\n')
		if elem == n:
			tt.write('   Верно\n')
		else:
			tt.write('   Неверно\n')
		tt.write('Минимальный: ' + str(minim) + '\n')
		tt.write('Максимальный: ' + str(maxim) + '\n')
		if minim <= maxim and minim >= min_real and maxim <= max_real:
			tt.write('   Верно\n')
		else:
			tt.write('   Неверно\n')
		tt.write('Среднее: ' + str(aver) + '\n')
		tt.write('Генерация: ' + str(time_gen) + ' секунд\n')
		tt.write('Вычисления: ' + str(time_count) + ' секунд\n')
		tt.write('Результат: ' + res + '\n\n\n')
	except MemoryError:
		messagebox.showerror('Внимание!', 'Недостаточно памяти!')
	except Exception:
		messagebox.showerror('Внимание!', 'Ошибка при записи в файл!')
	finally:
		tt.close()
	min_value.delete(1.0, END)
	min_value.insert(INSERT, str(minim))
	max_value.delete(1.0, END)
	max_value.insert(INSERT, str(maxim))
	aver_value.delete(1.0, END)
	aver_value.insert(INSERT, str(aver))

import time
import datetime
import random
import math
window=Tk()
window.title("Калькулятор массивов") 
window.geometry('1000x500')
lbl = Label(text="Тип")
lbl.grid(column=0, row=0)
selected = IntVar()
rad1 = Radiobutton(window, text='Целыe', value=1, variable=selected)  
rad2 = Radiobutton(window, text='Дробные', value=2, variable=selected)
rad1.grid(column=1, row=0)  
rad2.grid(column=2, row=0) 
lbl1 = Label(text="Оператор:")
lbl1.grid(column=0, row=1)
combo = Combobox(window, width=23)  
combo['values'] = (' ', "+", "-", "*", "/")  
combo.current(0)  
combo.grid(column=2, row=1)
lbl2 = Label(text="Элементов:")
lbl2.grid(column=0, row=2)
txt = Entry(window, width=25)  
txt.grid(column=2, row=2)
lbl3 = Label(text="Минимальный:")
lbl3.grid(column=0, row=3)
txt1 = Entry(window, width=25)  
txt1.grid(column=2, row=3)
lbl4 = Label(text="Максимальный:")
lbl4.grid(column=0, row=4)
txt2 = Entry(window, width=25)  
txt2.grid(column=2, row=4)
chkb = IntVar()
chkb.set(0)
chk = Checkbutton(window, text="Вывод в файл", variable=chkb, onvalue=1, offvalue=0, command=if_write)
chk.grid(column=4, row=0)
chkb1 = IntVar()
chkb1.set(0)
chk1 = Checkbutton(window, text="Автотест", variable=chkb1, onvalue=1, offvalue=0, command=if_test)
chk1.grid(column=5, row=0)
testing = Label(text="Автотест:")
testing.grid(column=4, row=3)
min_label = Label(text="min")
min_label.grid(column=5, row=2)
max_label = Label(text="max")
max_label.grid(column=5, row=3)
aver_label = Label(text="среднее")
aver_label.grid(column=5, row=4)
min_value = Text(window, width=25, height=1)
min_value.grid(column=6, row=2)
max_value = Text(window, width=25, height=1)
max_value.grid(column=6, row=3)
aver_value = Text(window, width=25, height=1)
aver_value.grid(column=6, row=4)
btn = Button(text="Генерация", command = generation)
btn.grid(column=0, row=6)
btn1 = Button(text="Вычисление", command = count)
btn1.grid(column=1, row=6)
lbl5 = Label(text="Тип")
lbl5.grid(column=0, row=8)
lbl6 = Label(text="Оператор")
lbl6.grid(column=1, row=8)
lbl7 = Label(text="Элементов")
lbl7.grid(column=2, row=8)
lbl8 = Label(text="Генерация")
lbl8.grid(column=3, row=8)
lbl9 = Label(text="Работа")
lbl9.grid(column=4, row=8)
lbl10 = Label(text="Файл, тест")
lbl10.grid(column=5, row=8)
lbl11 = Label(text="Результат")
lbl11.grid(column=6, row=8)
txt3 = Text(window, width=6, height=1)  
txt3.grid(column=0, row=9)
txt4 = Text(window, width=3, height=1)  
txt4.grid(column=1, row=9)
txt5 = Text(window, width=18, height=1)  
txt5.grid(column=2, row=9)
txt6 = Text(window, width=10, height=1)  
txt6.grid(column=3, row=9)
txt7 = Text(window, width=10, height=1)  
txt7.grid(column=4, row=9)
txt8 = Text(window, width=10, height=1)  
txt8.grid(column=5, row=9)
txt9 = Text(window, width=30, height=1)  
txt9.grid(column=6, row=9)
txt10 = scrolledtext.ScrolledText(window, width=120, height = 15, font = ('Calibri', 8))  
txt10.grid(column=0, row=10, columnspan = 15)
window.mainloop()