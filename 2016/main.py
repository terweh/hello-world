import itertools, time
from collections import namedtuple

########################

def day1():
    return

########################

def day2():
    return

########################

def day3_2():
    return

########################

def day4():
    return

#########################

def day5():
    return

##################################

def day6():
    return

##################################
def day7():
    return

##################################

def day8():
    return

##################################

def day9():
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

def day14():
    return

##################################

def day15():
    discs=[]
    Disc = namedtuple('Disc', 'pos start')
    for line in open("input_15.txt"):
        x=line.strip().split()
        discs.append(Disc(int(x[3]),int(x[11].strip("\."))))
    j=0
    #print(discs)
    for i in itertools.count(0):
        if (i+discs[j].start) % (discs[j].pos) ==0:
            j+=1
        else:
            j=0
        if j==len(discs): # for part 1: if j==len(discs)-1:
            print(i-len(discs))
            break
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

def day20(number, two):
    return

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

def day24():
    return


if __name__ == '__main__':
    tic = time.perf_counter()
    #day1(guides)
    #day2()
    #day3_1()
    #day3_2()
    #day4()
    #day5()
    #day6()
    #day7()
    #day8()
    #day9()
    #day10()
    #day11()
    #day12()
    #day13()
    #day14()
    day15()

    #day20(29000000, False)
    #day20(290, True)
    
    #day24()

    print("")
    print("_"*80)
    print(time.perf_counter() - tic)
    