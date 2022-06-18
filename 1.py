import random
#checking a list being special or not, boolean type
def check_special(main_list):
	temp = []
	#making a new list only with the numbers
	for i in main_list:
		temp.append(i[1:])
	#counting each number
	nums = [temp.count("1"), temp.count("2"), temp.count("3"), temp.count("4"), temp.count("5"), 
	temp.count("6"), temp.count("7"), temp.count("8"), temp.count("9"), temp.count("10"),
	temp.count("11"), temp.count("12"), temp.count("13")]
	#checking the counts
	if 2 in nums and 3 in nums:
		return True
	else:
		return False

#function for the main thing
def run(num_trials):
    all_cards = ["O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "O10", "O11", "O12","O13",
    "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13",
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10", "G11", "G12", "G13",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13"]
    special = 0
    for i in range(num_trials):
    	temp = (random.choices(all_cards, k = 5))
    	if check_special(temp):
    		special += 1
    print('Probability =', special / num_trials)


run(100)
run(10000)
run(1000000)