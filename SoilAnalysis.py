import re

dict = {}
input_file = "input.txt"

def parse(input):
    lines = open(input, "r")
    for line in lines:
        if re.match("(.*)(=)(.*)", line):
            start = 0
            end = 0
            while line[end] != '\n':
                end += 1
                if line[end] == ' ':
                    if line[start: end] != '=':
                        key = line[start: end]
                    #print line[start: end]
                    start = end + 1
            #print line[start: end]
            value = line[start: end]
            dict[key] = value
        else:
            ele = line[0: len(line)]
            if re.match("(.*)(\[)", ele):
                print line[0: len(line)-1] + ' = ' + str(cal__(ele))
            elif re.match("(.*)(\()", ele):
                print line[0: len(line)-1] + ' = ' + str(cal_(ele))
            else:
                print line[0: len(line)-1] + ' = ' + str(cal_sub(ele))

'''def cal(ele):
    if re.match("(.*)(\()(.*)(\))(.*)", ele):
        cal_(ele)
    else:
        cal_sub(ele)
'''

def cal__(ele):
    start = 0
    sum = 0
    for i in range(len(ele)):
        if ele[i] == '[':
            sum += cal_sub(ele[start: i]+'\n')
            start = i + 1
        elif ele[i] == ']' and ele[i+1].isdigit():
            if re.match("(.*)(\()", ele[start: i]):
                sub = cal_(ele[start: i]+'\n')
            else:
                sub = cal_sub(ele[start: i]+'\n')
            if ele[i+2].isdigit():
                sum += sub * float(ele[i+1: i+3]);
                start = i+3
            else:
                sum += sub * float(ele[i+1]);
                start = i+2
        elif ele[i] == '\n':
            sum += cal_sub(ele[start: i]+'\n')
    return sum

def cal_(ele):
    start = 0
    sum = 0
    for i in range(len(ele)):
        if ele[i] == '(':
            sum += cal_sub(ele[start: i]+'\n')
            start = i + 1
        elif ele[i] == ')' and ele[i+1].isdigit():
            sub = cal_sub(ele[start: i]+'\n')
            if ele[i+2].isdigit():
                sum += sub * float(ele[i+1: i+3]);
                start = i+3
            else:
                sum += sub * float(ele[i+1]);
                start = i+2
        elif ele[i] == '\n':
            sum += cal_sub(ele[start: i]+'\n')
    return sum

def cal_sub(ele):
    sum = 0
    i = 0
    sub = 0
    while ele[i] != '\n':
        if ele[i] in dict.keys():
            if ele[i+1].isdigit():
                if not ele[i+2].isdigit():
                    sum += float(dict[ele[i]]) * float(ele[i+1])
                    i += 2
                else:
                    sum += float(dict[ele[i]]) * float(ele[i+1: i+3])
                    i += 3
            else:
                sum += float(dict[ele[i]])
                i += 1
        elif ele[i:i+2] in dict.keys():
            if ele[i+2].isdigit():
                if not ele[i+3].isdigit():
                    sum += float(dict[ele[i: i+2]]) * float(ele[i+2])
                    i += 3
                else:
                    sum += float(dict[ele[i: i+2]]) * float(ele[i+2: i+4])
                    i += 4
            else:
                sum += float(dict[ele[i: i+2]])
                i += 2
    return sum

parse(input_file)



