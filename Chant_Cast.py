def menu():
    print("USE MAGIC:")
    print('(1) SPELLCAST \n(2) Buff/Debuff \n(3) Summoning \n(4) Spellblade \n(0) CLOSE')
    school = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')

    if school == 1:
        spellcast()
    elif school == 2:
        buffdebuff()
    elif school == 3:
        summoning()
    elif school == 4:
        spellblade()
    elif school == 0:
        return
    else:
        menu()


def spellcast():
    print("SPELL TYPE:")
    print('(1) ATTACK \n(2) SUPPORT \n(3) BACK')
    style = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')

    if style == 1:
        attack()
    elif style == 2:
        support()
    elif style == 3:
        menu()
    else:
        spellcast()


def attack():
    print("ATTACK MAGIC ELEMENTS:")
    print('(1) FIRE \n(2) WATER \n(3) ICE \n(4) LIGHTNING \n(5) EARTH \n(6) WIND \n(0) BACK')
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')

    if element == 1:
        fire()
    elif element == 2:
        water()
    elif element == 3:
        ice()
    elif element == 4:
        lightning()
    elif element == 5:
        earth()
    elif element == 6:
        wind()
    elif element == 0:
        spellcast()
    else:
        attack()


def support():
    print("Support MAGIC:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def buffdebuff():
    print("BUFF/DEBUFF MAGIC:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def summoning():
    print("SUMMONING:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def spellblade():
    print("SPELLBLADE:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def fire():
    print("FIRE SPELLS:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def water():
    print("WATER SPELLS:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')

def ice():
    print("ICE SPELLS")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def lightning():
    print("LIGHTNING SPELLS:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def earth():
    print("EARTH SPELLS:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def wind():
    print("WIND SPELLS:")
    element = int(input('ENTER CHOICE: '))
    print('-------------------------------------------------------------------------------------')


def main():
    menu()


main()
