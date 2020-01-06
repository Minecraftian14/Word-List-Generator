def convertTo1337(nm):
    out = ''
    for c in nm:
        if c.lower() == 'a':
            out += '4'
        elif c.lower() == 'b':
            out += '8'
        elif c.lower() == 'c':
            out += '<'
        elif c.lower() == 'd':
            out += c
        elif c.lower() == 'e':
            out += '3'
        elif c.lower() == 'f':
            out += c
        elif c.lower() == 'g':
            out += '6'
        elif c.lower() == 'h':
            out += c
        elif c.lower() == 'i':
            out += '1'
        elif c.lower() == 'j':
            out += c
        elif c.lower() == 'k':
            out += c
        elif c.lower() == 'l':
            out += '1'
        elif c.lower() == 'm':
            out += c
        elif c.lower() == 'n':
            out += c
        elif c.lower() == 'o':
            out += '0'
        elif c.lower() == 'p':
            out += c
        elif c.lower() == 'q':
            out += c
        elif c.lower() == 'r':
            out += '2'
        elif c.lower() == 's':
            out += '5'
        elif c.lower() == 't':
            out += '7'
        elif c.lower() == 'u':
            out += c
        elif c.lower() == 'v':
            out += c
        elif c.lower() == 'w':
            out += c
        elif c.lower() == 'x':
            out += '*'
        elif c.lower() == 'y':
            out += c
        elif c.lower() == 'z':
            out += c
        else:
            out += c

    return out


choice = input('Do you want to load data from file\n'
               'note, it has some disadvantages?[y/n] ')

names = []
suffix = []
others = []

mode = 'a'
mode1337 = 'no'

mode = input(
    '\nDo you want to generate:\n'
    'all illogical combinations[i/I]\n'
    'all logically possible combinations[a/A]\n'
    'all common structure sharing combinations[s/S]\n'
    'all common combinations[c/C]\n'
    '>>> ').strip()

if choice.lower().startswith('n'):
    print('\nPlease enter the details as required and "nan" if you want to ignore or end.\n'
          'And please, enter in sentence case, where ever possible.')

    print('\nPlease enter all related names.')
    print('<You can enter names of family members, pets, favorite edibles or authors, celebrities, etc>')

    driver = ''
    while True:
        driver = input('>>>').strip()
        if driver == 'nan':
            break
        else:
            names.append(driver)
            names.append(driver.lower())
            names.append(driver.upper())

    date = input('\nPlease enter Date of birth').strip()
    if len(date) == 1:
        suffix.append('0' + date)
    suffix.append(date)
    date = input('\nPlease enter Month of birth').strip()
    if date.isalpha():
        switcher = {}
        switcher = {
            "jan": ['1', '01', 'jan', 'January', 'january'],
            "feb": ['2', '02', 'feb', 'February', 'february'],
            "mar": ['3', '03', 'mar', 'March', 'march'],
            "apr": ['4', '04', 'apr', 'April', 'april'],
            "may": ['5', '05', 'may', 'May'],
            "jun": ['6', '06', 'jun', 'June', 'june'],
            "jul": ['7', '07', 'jul', 'July', 'july'],
            "aug": ['8', '08', 'aug', 'August', 'august'],
            "sep": ['9', '09', 'sep', 'September', 'september'],
            "oct": ['10', 'oct', 'October', 'october'],
            "nov": ['11', 'nov', 'November', 'november'],
            "dec": ['12', 'dec', 'December', 'december'],
        }
        suffix += switcher.get(date[:2], '')
    elif date.isnumeric():
        switcher = {
            '01': "January",
            '02': "February",
            '03': "March",
            '04': "April",
            '05': "May",
            '06': "June",
            '07': "July",
            '08': "August",
            '09': "September",
            '10': "October",
            '11': "November",
            '12': "December",
        }
        suffix.append(date)
        if len(date) == 1: date = '0' + date
        suffix.append(date)
        suffix.append(switcher.get(date, ''))
        suffix.append(switcher.get(date, '').lower())
        suffix.append(switcher.get(date, '')[:3])
        suffix.append(switcher.get(date, '')[:3].lower())
    else:
        print('Qui?')

    print('\nPlease enter all important years, like birth year, same for children, marriage, etc :')

    while True:
        driver = input('>>>').strip()
        if driver == 'nan':
            break
        else:
            suffix.append(driver)

    # choice = input('Do you want to include the most common words? ').strip()
    # if choice.lower().startswith('y'):
    #     others = ['123456', '123456789', 'qwerty', 'password', '1111111', 'abc123', '000000', '1q2w3e4r5t',
    #               'Qwertyuiop']
    choice = input('\nDo you wish to submit any other any information? ').strip()
    if choice.lower().startswith('y'):
        while True:
            driver = input('>>>').strip()
            if driver == 'nan':
                break
            else:
                others.append(driver)

else:
    setup = open('setup.txt', 'r')

    infoBlock = setup.read()
    infoBlock = infoBlock.split('\n')

    d = 0
    for info in infoBlock:
        if info == '':
            d += 1
            continue
        if info.startswith('-'):
            if d == 0:
                names.append(info[1:])
            elif d == 1:
                suffix.append(info[1:])
            elif d == 2:
                others.append(info[1:])
            else:
                print('Wut?')

# print()
# print(names)
# print(suffix)
# print(others)

mode1337 = input('\nDo you want to enable mode 1337? ')

if mode1337.lower().startswith('y'):
    for name in names:
        tem = convertTo1337(name)
        if name != tem:
            names.append(tem)
    for su in suffix:
        tem = convertTo1337(su)
        if su != tem:
            suffix.append(tem)

outFile = open('output.txt', 'a')

if mode.lower() == 'c':
    print('\nWriting common keys')

    for nm in names:
        for su in suffix:
            outFile.write(nm + su + '\n')

        for ot in others:
            outFile.write(nm + ot + '\n')


elif mode.lower() == 's':
    print('\nWriting structure-based keys keys')

    for nm in names:
        outFile.write(nm + '\n')

        for su in suffix:
            outFile.write(su + '\n')
            outFile.write(nm + su + '\n')

        for ot in others:
            outFile.write(ot + '\n')
            outFile.write(nm + ot + '\n')

            for su in suffix:
                outFile.write(nm + su + ot + '\n')
                outFile.write(nm + ot + su + '\n')

elif mode.lower() == 'a':
    print('\nWriting logical keys')
    for nm in names:

        outFile.write(nm + '\n')

        for su in suffix:
            outFile.write(su + '\n')
            outFile.write(nm + su + '\n')
            outFile.write(su + nm + '\n')

        for ot in others:
            outFile.write(su + '\n')
            outFile.write(ot + nm + '\n')
            outFile.write(nm + ot + '\n')

            for su in suffix:
                outFile.write(nm + su + ot + '\n')
                outFile.write(nm + ot + su + '\n')
                outFile.write(su + nm + ot + '\n')
                outFile.write(su + ot + nm + '\n')
                outFile.write(ot + su + nm + '\n')
                outFile.write(ot + nm + su + '\n')
else:
    print('\nWriting illogical keys')

    raw = names + suffix + others

    choice = input('Do you want to allow triplets?')

    for a in raw:
        outFile.write(a + '\n')

        for b in raw:

            if a == b: continue

            outFile.write(a + b + '\n')

            if choice.lower().startswith('y'):

                if a == b or b == c: continue

                for c in raw:
                    outFile.write(a + b + c + '\n')

print('Task completed.')
