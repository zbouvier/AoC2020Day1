
def day1():
    f = open('values.txt', 'r+')
    lines = []
    for line in f.readlines():
        lines.append(int(line.rstrip()))
    f.close()
    #print(lines)
    for val in lines:
        for val2 in lines:
            for val3 in lines:
                if(val + val2 + val3 == 2020):
                    return(str(val*val2*val3))

print(day1())
         