import time, itertools, hashlib, re
from math import log

########################
guides="(((())))()((((((((())()(()))(()((((()(()(((()((()((()(()()()()()))(((()(()((((((((((())(()()((())()(((())))()(()(()((()(()))(()()()()((()((()(((()()(((((((()()())()((((()()(((((()(())()(())((())()()))()(((((((())(()())(()(((())(()))((())))(()((()())))()())((((())))(()(((((()(())(((()()((()((()((((((((((())(()())))))()))())()()((((()()()()()()((((((())())(((()())()((()()(((()()()))(((((()))(((()(()()()(()(()(((())()))(()(((()((())()(()())())))((()()()(()()(((()))(((()((((()(((((()()(()())((()())())(()((((((()(()()))((((()))))())((())()()((()(()))))((((((((()))(()()(((())())(())()((()()()()((()((()((()()(((())))(()((())()((((((((()((()(()()(((())())())))(())())))()((((()))))))())))()()))()())((()())()((()()()))(()()(((()(())((((())())((((((((()()()()())))()()()((((()()))))))()((((()(((()))(()()())))((()()(((()))()()())())(((())((()()(())()()()(((())))))()())((()))()))((())()()())()())()()(()))())))())()))(())((()(())))(()(())(()))))(()(())())(()(())(()(()))))((()())()))()((((()()))))())))()()())((())()((()()()))()(((()(()))))(())()()))(((()())))))))))(((())))()))())()))))()()(((())))))))()(()()(()))((()))))((())))((()((())))())))()()(()))())()(()((()())(()(()()())())(()()))()))))(()())()()))()()()()))(()(()(()))))))()(()))()))()()(()((())(()(())))()(((())(())())))))()(()(()))))()))(()()()(())()(()(())))()))))()()(((((())))))())()())())())()())()))))()))))))))())()()()()()()())))()))((())()))())))()((())()))))()))())))))))())()()()))()()(()((((()(((((((()(())((()())((()()))()))))(())))()()()(())((())()())))(())))(())))(((()()))()(())(((()(()))((())))())()))((((()))())()))))))))()(())())))(()))()(()()))())()()(())())))())()()(()())))()((()())(()(())(())))))))))))))(()))))()))))))()()())(()(((((()(()())))())()))(()))()))(()()))()())(()))())()(())((()()))))))())))())()(((())))(()(()))()()))()(()))))))((()())(()))))))()())))()()))))))))((((((((()()()(()))))))()())))())))()()((())()))((())(())))())())))()()()((()((()(())))())()(())))))))))()())))()()()()()()))()))((())())(()(()))))))(()()))()))(())))()))))))))))))(()))))))))()))))()))()())()))()()))))))()))))((()))))(()))())()(())))(()())((((()())))()))))(()))()(()()(())))))())))))()))))))())))())))))())))())())))())(()))))(())()(())))())()))((()()))))))())))((())))))))())))(())))))()()())))))())))))()))))))()))()()()(()(((()())())())(()))())))))((()(())(()))))))))(())))()()()())())(()))))()()()))()))())())())()(())))()(((()((((())))))))()))))))))))))))))))))((())()())(()))))()()))))))(()()(())())))())))((())))((())))))))))))))()))))()(()))))))())))))()))(()()())(()())))))))))()))))))(())))))()()))()())(((())))()))(()))))))))(())())))())))())())())()()))((())()(())()())()))()())(())(()))))()())))(()(((()))))))()(()())()()()))()))))))))()()()(())()())()(((((()))()())())(()))))()()()(())))())))()((()())))(()))())()(()())())(()))()()))((()()))((()()()()())))(())()))(()(())))((()()))))))))())))))))())()()))))))))))))))))(())()(())(())()())())()))()(()))))())())))))()())()(()))()()(())))(())())))))(()))))))))))))))())())(())(())))(((()))()))))())((())(()))())))))))())))))())))()))()))))))))))))())()))))()))))((()))(())))()(())))(())()))()))())))())))))))()(()())())))()()())))(())))))(()))))))))))))(()))()))()))())))(((()()()(())((()())))()())(((()))(())()))((()()()())))())(())(()))))()(((((())))(()))())())))))))((((()()()))())())()(()(()())))))))))()())())))(())))()())(((()(())())()()))())())))))))((()())((()()(()))(()(())))()))()))(()))(()))()()(()(((())((((()))()(()))((())()(()(()())()(()))()())))))(()))()))())()())))())))(())))((())(()())))))()))(())(()))()())()(()()((()(()))))))()(())(()())(())()))(((())()))(()()(()()()))))(()(())))()))))())))))())(()()()()()()(((())))(()()))()((())(((((()()())))(()))(()))()()))(((())())()(((()()()()))))(()))(())())))()())(()()())())))))))()))))((())))()())(()))(()(()))())))))())(())))))()()())())()))()()(())))(()))(())((((((())(()))(()))())()))(()()(())))()))(()()))()))()(())))(())))((()(()))(())()()())())))(((()()())(())()))))))()(((()(((((()()(((())(())))())()((()))))((()())()(())(((())))(((()((()(()(()))(()()))())(()))(())(())))()))))))((((()))()((((()(()))()))()()))))()(()(()))()(()((()(((()(()()(((()))))()(((()(()(()(((()(()())())()()(()(()())())(()((((())(()))()))(((((()()())(())()((()()())))()()(((()()))()((((((((()(())))())((()))))(())))(()))))((()((((()()(())(((((()))(((((((((((((()())))((((()(((()((())())()))((()))()(()()((()()()()(()()(()(()(((())()(()((((((()((()()((())()((((()((()()(()()())((()()()((()((())()(()(((()((())((((())(()))((()(()))(()())()((((((((()(((((((((((()))(()(((()(()()()((((())((())()())()))(())((())(()))(((()((()(())))(()))))((()()))))((((()(()(()())(()(())((((((((()((((()((()(((((()))())()(()))(()()((()(())(((((()(())()(((((()()))))))()(((())()(()()((((())()((())((()(((())(((()))((()()((((()(())))))((()((((()((()((()(((())((()))(((((((()(((()((((((((())()))((((())(((((()((((((((()(((()((()(((()()(((()((((((()()(()((((((((()()(()(()(())((((()())()))))(((()))((((())((((()())((()(())()((()((((((()((((((()(())))()())(((())())())()(())()(()())((()()((((())((((((())(()(((((()((((())()((((()(()(())(()())(((())()((())((((()))()((((((())(()(((()(((()((((((()(((()))(()()())())((()((()())()((((())(((()(()(((((((((())(())))()((()()()()(())((()))(((((((()(((((((((()(()))))(()((((((((()((((()((()()((((((()()(((((((()(()(())()(())((()()()((()(((((()())()(((((()())()()((()(()())(()()()(((()()(((((()((((((()()((()(()()()((((((((((((()((((((((()()(((()())))()(((()()(())())((((()((((()((((()()()(())(())((()(()(((((((((((((((()(())(())))))()()))((()(((()(())((()(((()(()()((((()()(((()(((()(((((()()((()(()(((()))((((((()((((((((()((()((())(((((()(((())(())())((()()))((((())()()((()(((()(((((()()(((()))(((()(()(((((((((((((()))((((((((()(((()))))())((((((((((((())((())((()())(((())((())(()((((((((((()(((())((()()(()((())(((((((((((()))((((((((((((()(()())((()((()((()(()(((()((((((((()()(()((()(()(((()))((()))(((((((((((((()(())((((((())(((()(())(()(()(()((()()))((((()((((()((((())))())((((()((((()))((((((()((((((()((()(((())))((())(()))(()((()((((()((()(((()()))((((()()()(((((((())(((())(()))())((((()())(((()(((((((((((()(()(()((()(((((((((((((((()()((((()((((((((()(((()()((()((((()))(((()(())((((((()((((())()((((()((()))(())()(()(((()((())())((((((()(()(())())(((())(()(()())(((((()((()((())()())(())))(((()(())))))))(((()(((()))()((()(((()()((()())()()))())))(((()))(()(((()(((((((((()(()(((((()()(((()())()()))))()(((()))(((()(()(()(()(()))()(())()))(()(((())))(()))))))))))(())((()((())((()(())()(())((()()((((()()((()()))((())(((()((()(())(())))()(()(((((()((()))())()(((((()()(((()(()((((((())(()))(())()))((()(()()))(())())()))(((())))(()((()(((())(())())))((()()((((((((((((((()((()(()()(()(((()))())()()((()()()(())(()))(()())(((())((())()(())()()(()()(())))((()(((()))))(((()()(()()))())((()((())()))((((()()()())((())))(((()(())(((((()(((((()((()(()((((()()(((()()()(((()())(((()()((((())(()))(((()))(())())((()))(((()((()))(((()()((())((()(((((()((((()()())((()))()((((()((()(()()()("

def day1(guides):
    floor = 0
    for i,b in enumerate(guides,start=1):
        if b == "(":
            floor+=1
        if b == ")":
            floor-=1
        if floor == -1:
            print(i)
            break

########################

def paper_calculator(l, w, h):
    sides=[l*h, l*w, w*h]
    return sum(sides)*2 + min(sides)

def ribbon_calculator(l, w, h):
    sides=[l, w, h]
    return ( sum(sides) - max(sides) )*2 + ( l * w * h )

def day2():
    paper=0
    ribbon=0
    for line in open("input_2.txt"):
        l,w,h = line.strip("\n").split("x")
        paper += paper_calculator(int(l),int(w),int(h))
        ribbon += ribbon_calculator(int(l),int(w),int(h))

    print(ribbon_calculator(2,3,4))
    print("paper:\t{}".format(paper))
    print("ribbon:\t{}".format(ribbon))

########################

def find_locations(list):
    x=0
    y=0
    locations=[]
    locations.append("0_0")
    for d in list:
        if d == "<":
            x-=1
        elif d == ">":
            x+=1
        elif d == "v":
            y-=1
        elif d == "^":
            y+=1
        else:
            raise EnvironmentError
        locations.append("{}_{}".format(x,y))
    return locations

def day3_2():
    for line in open("input_3.txt"):
        s = line[::2]
        r = line[1::2]
        sList = find_locations(s)
        rList = find_locations(r)
        mylist = sList+rList
        houses=[(i,mylist.count(i)) for i in set(mylist)]
        print(len(houses))

def day3_1():
    for line in open("input_3.txt"):
        mylist=find_locations(line)
        houses=[(i,mylist.count(i)) for i in set(mylist)]
        print(len(houses))

########################

def day4():
    str2hash = "yzbqklnj"
  
    for i in itertools.count(start=1, step=1):
        string = str2hash+str(i)
        result = hashlib.md5(string.encode())
        if result.hexdigest()[:6] == "000000":
            print(string)
            return

#########################

def vowels(string):
    v = re.findall(r"[aeiou]", string)
    if len(v) >=3:
        return True
    return False

def double(string):
    v = re.findall(r"(\w)\1{1}",string)
    if len(v) >=1:
        return True
    return False

def forbidden(string):
    for x in ["ab", "cd", "pq", "xy"]:
        v = re.findall(x,string)
        if len(v) >=1:
            return True
    return False

def double_pair(string):
    v = re.findall(r"(\w).\1{1}",string)
    if len(v) >=1:
        return True
    return False

def spaced_double(string):
    v = re.findall(r"(\w\w).*\1{1}",string)
    if len(v) >=1:
        return True
    return False

def nice_1(string):
    if vowels(string) and double(string):
        if forbidden(string):
            return False
        return True
    return False

def nice_2(string):
    if spaced_double(string) and double_pair(string):
        return True
    return False

def day5():
    count = 0
    for line in open("input_5.txt"):
        if nice_2(line):
            count+=1
    print(count)
    return

##################################
class Light():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.light = False

def map_lights(line, grid):
    c = list(map(lambda x: list(map(lambda y: int(y), x.split(","))), re.findall("\d+,\d+", line)))
    c.append(re.findall("t\w\w\w[ l]\w+ ",line)[0])
    if c[2] == "turn on ":
        for x in range(c[0][0],c[1][0]+1):
            for y in range(c[0][1],c[1][1]+1):
                grid[x][y]+=1
    elif c[2] == "turn off ":
        for x in range(c[0][0],c[1][0]+1):
            for y in range(c[0][1],c[1][1]+1):
                grid[x][y]-=1 if grid[x][y] > 0 else 0
    elif c[2] == "toggle ":
        for x in range(c[0][0],c[1][0]+1):
            for y in range(c[0][1],c[1][1]+1):
                grid[x][y] += 2
    else:
        raise EnvironmentError
    return grid

def day6():
    grid =[[0 for y in range(0,1000)] for x in range(0,1000)]
    
    for line in open("input_6.txt"):
        grid = map_lights(line, grid)

    count = 0
    for row in grid:
        for light in row:
            count += light

    print(count)
    return

##################################
test=["123 -> lx",
      "456 -> y",
      "lx AND y -> dp",
      "lx OR y -> e",
      "lx LSHIFT 2 -> f",
      "y RSHIFT 2 -> g",
      "NOT lx -> h",
      "NOT y -> i",
      "dp -> k"]

class Signal():
    def __init__(self, signal, index):
        self.index=index
        if re.fullmatch("\d+",signal):
            self.full=True
            self.signal=int(signal)
        else:
            self.full=False
            s=signal.split(" ")
            if s[0]=="NOT":
                self.gate=s[0]
                self.input=s[1]
            elif len(s)>1:
                self.gate=s[1]
                self.input=[s[0], s[2]]
            else:
                self.gate="EQUAL"
                self.input=s[0]

    def get_signal(self, dict):
        if self.full==False:
            self.full=True
            self.signal=self.generate(dict)
            print(self.index)
        return self.signal

    def get(self,string,dict):
        return int(string) if re.fullmatch("\d+",string) else dict[string].get_signal(dict)

    def generate(self, dict):
        if self.gate=="NOT":
            return NOT(self.get(self.input, dict))
        elif self.gate=="AND":
            return AND(self.get(self.input[0], dict), self.get(self.input[1], dict))
        elif self.gate=="OR":
            return OR(self.get(self.input[0], dict), self.get(self.input[1], dict))
        elif self.gate=="LSHIFT":
            return LSHIFT(self.get(self.input[0], dict), int(self.input[1]))
        elif self.gate=="RSHIFT":
            return RSHIFT(self.get(self.input[0], dict), int(self.input[1]))
        elif self.gate=="EQUAL":
            return self.get(self.input, dict)
        else:
            raise EnvironmentError
        

def to16bin(i):
    return str(bin(i))[2:].zfill(16)

def AND(x,y):
    z=list(to16bin(0))
    x=to16bin(x)
    y=to16bin(y)
    for i in range(16):
        if x[i]=="1" and y[i]=="1":
            z[i]="1"
        else:
            z[i]="0"
    return int("".join(z), 2)

def OR(x,y):
    z=list(to16bin(0))
    x=to16bin(x)
    y=to16bin(y)
    for i in range(16):
        if x[i]=="1" or y[i]=="1":
            z[i]="1"
        else:
            z[i]="0"
    return int("".join(z), 2)

def LSHIFT(x,i):
    x=to16bin(x)
    return int(x[i:]+"0"*i, 2)

def RSHIFT(x,i):
    x=to16bin(x)
    return int("0"*i+x[:-i], 2)

def NOT(x):
    z=list(to16bin(0))
    x=to16bin(x)
    for i in range(16):
        if x[i]=="0":
            z[i]="1"
    return int("".join(z), 2)


def day7():
    dict={}
    for line in open("input_7.txt"):
        #for line in test:
        l=line.strip("\n").split(" -> ")
        dict[l[1]]=Signal(l[0], l[1])
        
    dict["b"].signal=46065
    print(dict["a"].get_signal(dict))
    #for element in dict:
    #    print("{}: {}".format(element,dict[element].get_signal(dict)))
    return

##################################
test8 = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']

def clean(string):
    string = re.sub('\\\\\\\\', '_', string)
    string = re.sub('\\\\\"', '_', string)
    string = re.sub('\\\\x..', '_', string)
    string=string.strip('"')
    return string

def encode8(string):
    string = re.sub('\\\\', r'\\\\', string)
    string = re.sub('"', r'\\"', string)
    return r'"'+string+r'"'

def day8():
    #for line in test8:
    all=0
    decoded=0
    encoded=0
    for line in open("input_8.txt"):
        line=line.strip("\n")
        print(len(line), end=" : ")
        line2=clean(line)
        line3=encode8(line)
        print(len(line3))
        print(line,line3)

        all+=len(line)
        decoded+=len(line2)
        encoded+=len(line3)
    print("part 1: {}".format(all-decoded))
    print("part 1: {}".format(encoded-all))
    return

##################################
test9=["London to Dublin = 464",
       "London to Belfast = 518",
       "Dublin to Belfast = 141"]

def go_broad(visited,list):
    if len(list)>1:
        all=[]
        for city in list:
            visited_local=visited
            list_local=list.copy()
            list_local.remove(city)
            visited_local+="->"+city
            all+=go_broad(visited_local,list_local)
        return all
    else:
        return [visited+"->"+list[0]]

def day9():
    citylist=set([])
    distances={}
    
    for line in open("input_9.txt"):
        line.strip("\n")
        a=line.split(" ")
        citylist.add(a[0])
        citylist.add(a[2])
        distances[a[0]+"-"+a[2]]=int(a[4])
        distances[a[2]+"-"+a[0]]=int(a[4])
    citylist=list(citylist)

    tours=go_broad("",citylist)
    all_dist=[]
    for tour in tours:
        m=tour.split("->")
        dist=0
        for i in range(1,len(m)-1):
            dist+=distances[m[i]+"-"+m[i+1]]
        all_dist.append(dist)
    print(min(all_dist))
    print(max(all_dist))

    return

##################################

def day10():
    return

##################################

def day11():
    return


##################################

def day12():
    return


##################################

def day13():
    return


##################################

def day15():
    return

##################################

def day16():
    return

##################################

def day17():
    return
##################################

def day18():
    return
##################################

def day19():
    return

##################################

def division_check(base, divider):
    if base%divider == 0:
        return True
    return False

def day20(number, two):
    house=[0]*(number+1)
    
    for elve in range(1,number):
        count=0
        for visiting in range(elve, number, elve):
            house[visiting] += 10*elve if not two else 11*elve
            count+=1
            if count >=50 and two: break

    for i,m in enumerate(house,start=0):
        if m >= number:
            print("House {} got {} presents.".format(i,m))
            return

    ## OLD ATTEMPT
    # elve_counter=0
    # elves=set()
    # print("goal:    {}".format(number))
    # biggest=0
    # while elve_counter < number:
    #     elve_counter+=1
    #     elves.add(elve_counter)
    #     visiting_elves = list(filter(lambda e: division_check(elve_counter, e), elves))

    #     gifts = sum(list(map(lambda n: n*10,visiting_elves)))
    #     biggest = gifts if gifts > biggest else biggest
    #     sys.stdout.write("current: {}{}".format(" "*(len(str(number))-len(str(biggest))),
    #                                             biggest))
    #     sys.stdout.flush()
    #     if gifts >= number:
    #         sys.stdout.write('\b'*(1+int(log(gifts))))
    #         print("House {} got {} presents.".format(elve_counter,gifts))
    #         break
    #     sys.stdout.write('\b'*(10+len(str(number))))


##################################

def day21():
    return


##################################

def day22():
    return

##################################

def day23():
    return

##########################################

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    def print(self):
        print(self.x,self.y,self.value)

def generate(n):
    return (n*252533)%33554393

def day24():

    x = 1
    y = 1
    code = 20151125
    table=[]
    tic = time.perf_counter()
    while True:
        table.append(Point(x,y,code))
        code=generate(code)
        y+=1
        x-=1
        if x == 0:
            x=y
            y=1
        if x >= 6100:
            break

    x=0
    y=0
    toc = time.perf_counter()
    print(toc-tic)
    list = [[0 for j in range(1,3100)] for i in range(1,3100)]
    for point in table:
        if point.x == 2978 and point.y == 3083:
            print(point.value)

    toc = time.perf_counter()
    print(toc-tic)


if __name__ == '__main__':
    #day1(guides)
    #day2()
    #day3_1()
    #day3_2()
    #day4()
    #day5()
    #day6()
    #day7()
    #day8()
    day9()

    #day20(29000000, False)
    #day20(290, True)
    
    #day24()