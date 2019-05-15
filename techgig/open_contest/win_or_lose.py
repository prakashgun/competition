''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import fileinput

def strongerVillian(count, villian_energies, hero_energies):
    vill = [int(n) for n in villian_energies.split()]
    vill.sort()
    hero = [int(n) for n in hero_energies.split()]
    hero.sort()

    count = int(count)

    for j in range(count):
        if(vill[j] >= hero[j]):
                return True
    return False

def main():
        lines = fileinput.input()
        testcases = int(lines[0])

        row = 0
        for testcase in range(testcases):
            if strongerVillian(lines[row+1], lines[row+2], lines[row+3]):
                print("LOSE")
            else:
                print("WIN")
            row = row + 3

main()