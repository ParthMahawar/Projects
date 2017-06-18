from Tkinter import *
import random

root = Tk()
Money = IntVar()
Money.set(500)
textvar = StringVar()

def begin():
	global Color
	global Number

	try:
		WinLoseLabel.destroy()
		Redo.destroy()
	except:
		print ''
	Start.destroy()
	textvar.set('What would you like to bet on?')
	Text = Label(root, textvariable = textvar)
	Text.grid(row = 1, columnspan = 3)
	Color = Button(text = 'Color', command = ColorBet, width = 25)
	Color.grid(row = 2, columnspan = 3)
	Number = Button(text = 'Number', command = NumBet, width = 25)
	Number.grid(row = 3, columnspan = 3)

def ColorBet():
	global ColEntry
	global Submit

	Color.destroy()
	Number.destroy()
	textvar.set('How much would you like to bet?')
	ColEntry = Entry(root, width = 30)
	ColEntry.grid(row = 2, columnspan = 3)
	Submit = Button(root, text = 'Submit', command = ColorChoice)
	Submit.grid(row = 3, column = 2)

def NumBet():
	global NumEntry
	global NumSubmit

	Color.destroy()
	Number.destroy()
	textvar.set('How much would you like to bet?')
	NumEntry = Entry(root, width = 30)
	NumEntry.grid(row = 2, columnspan = 3)
	NumSubmit = Button(root, text = 'Submit', command = NumChoice)
	NumSubmit.grid(row = 3, column = 2)

def NumChoice():
	global NumMoneyBet
	global Button1
	global Button2
	global Button3

	try:
		NumMoneyBet = int(NumEntry.get())
		NumEntry.destroy()
		NumSubmit.destroy()
		if NumMoneyBet <= 0:
			ColMoneyBet = 0 - ColMoneyBet
		textvar.set('What Number Group would you like to bet on?')
		Button1 = Button(root, text = '0-14', width = 30, command = Group1)
		Button1.grid(row = 2, columnspan = 3)
		Button2 = Button(root, text = '15-29', width = 30, command = Group2)
		Button2.grid(row = 3, columnspan = 3)
		Button3 = Button(root, text = '30-44', width= 30, command = Group3)
		Button3.grid(row = 4, columnspan = 3)
	except:
		print "You can't bet that amount!!!"

def ColorChoice():
	global ColMoneyBet
	global RedButton
	global BlackButton
	global GreenButton

	try:
		ColMoneyBet = int(ColEntry.get())
		ColEntry.destroy()
		Submit.destroy()
		if ColMoneyBet <= 0:
			ColMoneyBet = 0 - ColMoneyBet
		textvar.set('What Color would you like to bet on?')
		RedButton = Button(root, bg = 'red', width = 30, command = red)
		RedButton.grid(row = 2, columnspan = 3)
		BlackButton = Button(root, bg = 'black', width = 30, command = black)
		BlackButton.grid(row = 3, columnspan = 3)
		GreenButton = Button(root, bg ='green', width= 30, command = green)
		GreenButton.grid(row = 4, columnspan = 3)
	except:
		print "You can't bet that amount!!!"

def Group1():
	global GroupChoice
	GroupChoice = 1
	NumBackend()

def Group2():
	global GroupChoice
	GroupChoice = 2
	NumBackend()

def Group3():
	global GroupChoice
	GroupChoice = 3
	NumBackend()

def red():
	global ColorChosen
	ColorChosen = 1
	ColorBackend()

def black():
	global ColorChosen
	ColorChosen = 2
	ColorBackend()

def green():
	global ColorChosen
	ColorChosen = 3
	ColorBackend()

def ColorBackend():
	global WinLoseLabel
	global Redo

	NumberLanded = random.randint(1, 44)
	RedButton.destroy()
	GreenButton.destroy()
	BlackButton.destroy()

	WinLose = StringVar()
	WinLose.set('')

	WinLoseLabel = Label(root, textvariable = WinLose)
	WinLoseLabel.grid(row = 2, columnspan = 3)

	if NumberLanded < 22:
		textvar.set('The Ball Landed On Red.')
		if ColorChosen == 1:
			WinLose.set('You win your bet. Take your money.')
			Money.set(Money.get() + ColMoneyBet)
		else:
			WinLose.set('You lose your bet. I keep your money')
			Money.set(Money.get() - ColMoneyBet)
	
	elif NumberLanded < 44:
		textvar.set('The Ball Landed On Black.')
		if ColorChosen == 2:
			WinLose.set('You win your bet. Take your money.')
			Money.set(Money.get() + ColMoneyBet)
		else:
			WinLose.set('You lose your bet. I keep your money')
			Money.set(Money.get() - ColMoneyBet)

	else:
		textvar.set('The Ball Landed on Green.')
		if ColorChosen == 2:
			WinLose.set('JACKPOT!!! Lucky Dude.')
			Money.set(Money.get() + 20*ColMoneyBet)
		else:
			WinLose.set('You lose your bet. You thought that would work?')
			Money.set(Money.get() - 5*ColMoneyBet)

	if Money.get() > 0:
		Redo = Button(root, text = 'Bet Again', command = begin)
		Redo.grid(row = 3, column = 2)

	if Money.get() <= 0:
		Redo = Button(root, text = 'Quit', command = root.destroy)
		Redo.grid(row = 3, column = 2)
		WinLose.set("You're Bankrupt.")

def NumBackend():
	global WinLoseLabel
	global Redo

	NumberLanded = random.randint(1, 44)
	Button1.destroy()
	Button2.destroy()
	Button3.destroy()

	WinLose = StringVar()
	WinLose.set('')

	WinLoseLabel = Label(root, textvariable = WinLose)
	WinLoseLabel.grid(row = 2, columnspan = 3)

	if NumberLanded < 15:
		textvar.set('The Ball Landed On ' + str(NumberLanded))
		if GroupChoice == 1:
			WinLose.set('You win your bet. Take your money.')
			Money.set(Money.get() + 2*NumMoneyBet)
		else:
			WinLose.set('You lose your bet. I keep your money')
			Money.set(Money.get() - NumMoneyBet)
	
	elif NumberLanded < 30:
		textvar.set('The Ball Landed On ' + str(NumberLanded))
		if GroupChoice == 2:
			WinLose.set('You win your bet. Take your money.')
			Money.set(Money.get() + 2*NumMoneyBet)
		else:
			WinLose.set('You lose your bet. I keep your money')
			Money.set(Money.get() - NumMoneyBet)

	else:
		textvar.set('The Ball Landed On ' + str(NumberLanded))
		if GroupChoice == 3:
			WinLose.set('You win your bet. Take your money')
			Money.set(Money.get() + 2*NumMoneyBet)
		else:
			WinLose.set('You lose your bet. I keep your money')
			Money.set(Money.get() - NumMoneyBet)

	if Money.get() > 0:
		Redo = Button(root, text = 'Bet Again', command = begin)
		Redo.grid(row = 3, column = 2)

	if Money.get() <= 0:
		Redo = Button(root, text = 'Quit', command = root.destroy)
		Redo.grid(row = 3, column = 2)
		WinLose.set("You're Bankrupt.")

CurrentMoney = Label(root, text = 'Current money: $')
CurrentMoney.grid(row = 0, column = 1)
ShowMoney = Label(root, textvariable = Money)
ShowMoney.grid(row = 0, column = 2)
Start = Button(root, text = 'Begin', command = begin, width = 15)
Start.grid(row = 1, columnspan = 3)

root.mainloop()