from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

#########################
screen_width = 720 / 2
screen_hight = 1280 / 2
#########################
def numer(date,Num = 0):
    srt_date =[]
    allNumbers = ''
    table = ['-','-','-','-','-','-','-','-','-']
    ##цифры даты рождения
    for elem in date:
        srt_date.append(int(elem))
        allNumbers += elem
    ##специальное число, зависящее от года рождения
    if srt_date[4] < 2:
        special_number = -2
        allNumbers += '2'
    else:
        special_number = 19
        allNumbers += '19'
    ##1 число
    first_number = str(sum(srt_date))
    allNumbers += first_number
    if Num == 1:
        return str(first_number)
    ##2 число
    second_number = str(int(first_number[0]) + int(first_number[1]))
    allNumbers += second_number
    if Num == 2:
        return str(second_number)
    ##3 число
    third_number=str(int(first_number) + special_number)
    allNumbers += third_number
    if Num == 3:
        return str(third_number)
    #4 число
    fourth_number=str(int(third_number[0]) + int(third_number[1]))
    allNumbers += fourth_number
    if Num == 4:
        return str(fourth_number)
    ##все цифры
    for number in allNumbers:
        if int(number) != 0:
            if table[int(number)-1] == '-':
                table[int(number)-1] = ''
            table[int(number)-1] += number
    return table

class NumerologyApp(App):
	def build(self):
		main_ground = BoxLayout(orientation = 'vertical', padding = 7)
		num_field = BoxLayout(orientation = 'vertical', padding = 7)
		num_table = GridLayout(rows=3, padding = 7, spacing = 5, orientation = 'tb-lr')
		num_input = BoxLayout(orientation = 'horizontal', padding = 7, size_hint = (1,.2))
		
		self.tinput = TextInput(input_filter='int', size_hint = (.9,1), font_size = 30)
		self.label_table = []
		self.label_info = Label(text='Дата рождения:\n1 число:\n2 число:\n3 число:\n4 число:', halign = 'left', size_hint = (1,.8), font_size = 24)

		for i in range(9):
			self.label_table.append(Label(text='-', font_size = 20))
			num_table.add_widget(self.label_table[i])
		
		num_input.add_widget(self.tinput)
		num_input.add_widget( Button(text = '>', font_size = 30, on_press = self.count, size_hint = (.1,1)) )
		
		num_field.add_widget(num_input)
		num_field.add_widget(self.label_info)
		
		main_ground.add_widget(num_field)
		main_ground.add_widget(num_table)
		
		return main_ground

	def count(self, instance):
		i = 0
		n1 = numer(str(self.tinput.text),1)
		n2 = numer(str(self.tinput.text),2)
		n3 = numer(str(self.tinput.text),3)
		n4 = numer(str(self.tinput.text),4)
		date = self.tinput.text[:2]+'.'+self.tinput.text[2:4]+'.'+self.tinput.text[4:]
		for elem in numer(str(self.tinput.text)):
			self.label_table[i].text = str(elem)
			i+=1
		self.label_info.text = f'Дата рождения: {date} \n1 число: {n1}\n2 число: {n2}\n3 число: {n3}\n4 число: {n4}'

#####################################

if __name__ == '__main__':
	NumerologyApp().run()
