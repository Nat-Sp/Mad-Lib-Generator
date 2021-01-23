from tkinter import *
#Create a window
root = Tk()
root.geometry('300x300')
root.title('Mad Libs Generator')
Label(root, text = 'Havae Fun!', font = 'arial 20 bold').pack()
Label(root, text = 'Pick a story to get started!', font = 'arial 15 bold').place(x = 40, y = 80)

#Define function

def madLib1():
    adjective = input('Adjective: ')
    noun = input('Noun: ')
    animal = input('Animal: ')
    noise = input('Noise: ')
    print(adjective + ' Macdonald had a ' + noun + ', E-I-E-I-O\n' +
          'and on that ' + noun + ' he had an ' + animal + ', E-I-E-I-O\n' +
          'with a ' + noise + noise + ' here\n' +
          'and a ' + noise + noise + ' there\n' +
          'here a ' + noise + ', there a ' + noise + ',\n' +
          'everywhere a ' + noise + noise + ',\n' +
          adjective + ' Macdonald had a ' + noun + ', E-I-E-I-O.')

def madLib2():
    color = input('Color: ')
    noun1 = input('Noun (plural): ')
    noun2 = input('Noun: ')
    adjective = input('Adjective: ')
    print('Roses are ' + color + ',\n' +
          noun1 + ' are blue,\n' +
          noun2 + ' is '+ adjective + '\n' +
          'and so are you.')
def madLib3():
    word = input('Silly word: ')
    animal = input('Animal: ')
    instrument = input('Musical instrument: ')
    noun1 = input('Noun: ')
    adjective = input('Adjective: ')
    noun2 = input('Noun: ')
    print('Hey, ' + word + ', ' + word + '!\n' +
          'The ' + animal + ' and the ' + instrument + ',\n' +
          'The cow jumped over the ' + noun1 + ';\n' +
          'The ' + adjective + ' dog laughed\n' +
          'To see such sport,\n' +
          'And the ' + noun2 + ' ran away with the spoon.')

Button(root, text = 'Old Macdonald', font = 'arial 15', command = madLib1(),
       bg = 'ghost white').place(x = 60, y = 120)
Button(root, text = 'Romantic Poetry', font = 'arial 15', command = madLib2(),
       bg = 'ghost white').place(x = 70, y = 180)
Button(root, text = 'The cat and the fiddle', font = 'arial 15', command = madLib3(),
       bg = 'ghost white').place(x = 80, y = 240)

root.mainloop()

