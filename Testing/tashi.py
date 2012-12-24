import itertools


def all_combinations(list):
	list_all_combinations = []
	for i in range(1, len(list)):
		for j in itertools.combinations(list, i):
			list_all_combinations.append(j)

	return list_all_combinations

def product_to_list(product):
	list_products = []
	for i in product:
		list_products.append(i)
	return list_products
	
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
#	print sum([pair[0] for pair in i])		#sums the first component of each pair
#	print sum(zip(*i)[1])					#sums the first component of each pair
