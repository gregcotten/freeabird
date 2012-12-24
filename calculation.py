import itertools, csv, os, copy

def all_combinations(list):
	list_all_combinations = []
	for i in range(1, len(list)):
		for j in itertools.combinations(list, i):
			tuple = []
			for k in j:
				if k is not None:
					tuple.append(k)
			list_all_combinations.append(tuple)
	return list_all_combinations

def product_to_list(product):
	list_products = []
	for i in product:
		list_products.append(i)
	return list_products
<<<<<<< HEAD
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("Data")

list = []
with open("freebirds_caloric_info_freebird_burrito.csv") as data:
	reader = csv.reader(data, delimiter=",")
	for row in reader:
		list.append(row)

exclusive_list = [] #right now just different tortillas should be exclusive
inclusive_list = [] #everything else can supposedly be mashed together in a burrito
for i in range(1,5): #hardcode first four options (tortillas) are the exclusive options
	exclusive_list.append(list[i])
for i in range(5, len(list)): #hardcode rest of options as inclusive anything goes
	inclusive_list.append(list[i])

inclusive_all_combinations = all_combinations(inclusive_list)

#get all possible combinations of burritos
all_combinations = []
for i in exclusive_list:
	for j in inclusive_all_combinations:
		lst = []
		for k in j:
			lst.append(k)
		lst.insert(0,i)
		all_combinations.append(lst)

less_than_fivehundredcalories = []

for combination in all_combinations:
	calorie_sum = 0
	for item in combination:
		calorie_sum += int(item[2])
	if calorie_sum <= 500:
		less_than_fivehundredcalories.append(combination)

print "All Combinations: " + str(len(all_combinations)) + "\n500 Calories or less: " + str(len(less_than_fivehundredcalories))	
=======
	
def imap(function, *iterables):
	# imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
	iterables = map(iter, iterables)
	while True:
		args = [next(it) for it in iterables]
		if function is None:
			yield tuple(args)
		else:
			yield function(*args)
	
#exclusive means we can only choose one from the list
list1_exclusive = [1,2,8]
list2_exclusive = [3,4,7]
list3_exclusive = [12,6,5]

#inclusive means it can be anything from the list - any amount, order doesn't matter
list4_inclusive = [8, 10, 20, 30, 50]

product_of_exclusives = product_to_list(itertools.product(list1_exclusive, list2_exclusive, list3_exclusive))

list4_all_combinations = all_combinations(list4_inclusive)



for i in product_to_list(itertools.product(product_of_exclusives, list4_all_combinations)):
	print i
	print imap(pow, (2,3,10), (5,2,3)) #Why doesn't this result in "32 9 1000"?
	
>>>>>>> Added imap function
