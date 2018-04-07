def readFile():
    file = open('kursjual.txt')
    val, list = file.readlines(), []
    for line in val:
        sublist = line.split()
        list.append(sublist)
    return list
    file.close()


def bubleSort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if int(list[j][3]) > int(list[j + 1][3]):
                list[j], list[j + 1] = list[j + 1], list[j]


def writeFile(list):
    file = open('kursjualurut.txt', 'w')
    for x in range(len(list)):
        file.write('%s %s %s %s %s\n'
        % (list[x][0], list[x][1], list[x][2], list[x][3], list[x][4]))
    file.close()


if __name__ == '__main__':
    thelist = readFile()
    bubleSort(thelist)
    writeFile(thelist)