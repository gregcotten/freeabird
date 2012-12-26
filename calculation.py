import itertools, csv, os, copy
from time import time

def calorie_count(combination):
	cal_count = 0
	for item in combination:
		cal_count+=int(item[2])
	return cal_count

def all_combinations_from_list(list):
	list_all_combinations = []
	for i in range(1, len(list)):
		for j in itertools.combinations(list, i):
			tuple = []
			for k in j:
				if k is not None:
					tuple.append(k)
			list_all_combinations.append(tuple)
	return list_all_combinations
	
def all_combinations_with_cal_less_than_or_equal_to(list,cal_count):
	combinations_less_than = []
	for i in range(1, len(list)):
		for j in itertools.combinations(list, i):
			tuple = []
			for k in j:
				if k is not None:
					tuple.append(k)
			cal_sum = 0
			for item in tuple:
				cal_sum+=int(item[2])
			if cal_sum <= cal_count:
				combinations_less_than.append(tuple)
	return combinations_less_than	

def product_to_list(product):
	list_products = []
	for i in product:
		list_products.append(i)
	return list_products

def do_optimized_calculation(filename,max_cal):
	start = time()
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	os.chdir("Data")

	data_list = []
	with open(filename) as data:
		reader = csv.reader(data, delimiter=",")
		for row in reader:
			data_list.append(row)

	exclusive_list = [] #right now just different tortillas should be exclusive
	inclusive_list = [] #everything else can supposedly be mashed together in a burrito
	for i in range(1,4): #hardcode exclusive options
		exclusive_list.append(data_list[i])
	for i in range(5, len(data_list)): #hardcode rest of options as inclusive anything goes
		inclusive_list.append(data_list[i])

	inclusive_all_combinations = all_combinations_from_list(inclusive_list)


	all_combinations = []
	less_than_maxcal_combinations = []
	for i in exclusive_list:
		for j in inclusive_all_combinations:
			combination = []
			for item in j:
				combination.append(item)
			combination.insert(0,i)
			if calorie_count(combination) <= max_cal:
				less_than_maxcal_combinations.append(combination)
			all_combinations.append(combination)
	end = time()
	print filename + " stats:"
	print "All Combinations: " + str(len(all_combinations))
	print "500 Calories or less: " + str(len(less_than_maxcal_combinations))
	print "Time: " + str(end-start) + " seconds"
	print ""

if __name__ == "__main__":
    less_than_maxcal_combinations = do_optimized_calculation("freebirds_caloric_info_freebird_burrito_monster_burrito.csv",500)