import sys, click
from math import log

#@click.command()
#@click.option('-n', '--number', help='Number to search for')
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')



def division_check(base, divider):
    if base%divider == 0:
        return True
    return False

@click.command()
@click.option('-n', '--number', required=True, type=int, help='Number to search for')
@click.option('--two', is_flag=True)
def crazy_elves(number, two):
    """see https://adventofcode.com/2015/day/20"""
    house=[0]*(number+1)
    
    for elve in range(1,number):
        count=0
        for visiting in range(elve, number, elve):
            house[visiting] += 10*elve if not two else 11*elve
            count+=1
            if count >=50: break
        #print(number-elve)

    for i,m in enumerate(house,start=0):
        if m >= number:
            print("House {} got {} presents.".format(i,m))
            return
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

if __name__ == '__main__':
    crazy_elves()
