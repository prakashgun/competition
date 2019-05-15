''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import fileinput

def max_list(house_count, tickets):
	house_count = int(house_count)
	ticket_list = [int(n) for n in tickets.split()]
	combination = {}
	i = 0

	for ticket in ticket_list:
		i += 1
		combination[str(ticket)] = ticket

		j = 0
		for pair in ticket_list:
			j += 1
			if(j <= i or j == (i+1)):
				continue
			key = str(pair) + str(ticket)
			combination[str(key)] = (pair + ticket)

	return max(combination, key=combination.get)



def main():
	lines = fileinput.input()
# 	inp = """5
# 5
# -1 7 8 -5 4 
# 4
# 3 2 1 -1 
# 4
# 11 12 -2 -1 
# 4
# 4 5 4 3 
# 4
# 5 10 4 -1"""
	
# 	lines = inp.split("\n")
	testcases = int(lines[0])
	row = 0

	for testcase in range(testcases):
		max_value = max_list(lines[row+1], lines[row+2])
		print("max_value", max_value)
		row += 2

main()