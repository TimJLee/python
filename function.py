def hi():
    print('Hi there!')
    print('How are you?')

hi()

def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi('Tim')

def hi(name):
    print('Hi' + name + '!')

hi('Rachel')


def hi(name):
    print('Hi' + name + '!')

girls = ['Rachel','Monica','Phoebe','Ola','You']
for name in girls:
    hi(name)
    print('Next girl')

for i in range(1,6):
    print(i)

for i in range(0,5):
    hi(girls[i])
    print('Next girl')
