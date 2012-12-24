def subset_sum_recursive(numbers,target,partial):
    s = sum(partial)
    
    #check if the partial sum is less than or equal to target
    if s <= target: 
		print "sum(%s) <=%s"%(partial,target)
		print s		#print combination sum

		
    if s >= target:
        return # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum_recursive(remaining,target,partial + [n])


def subset_sum(numbers,target):
    subset_sum_recursive(numbers,target,list())


# define the calorie list
calorieList = [3,9,8,4,5,7,10]

# define the max calorie count
maxCalories = 15

# define starting number of successful combinations
#successfulCombos = 0

if __name__ == "__main__":
    subset_sum(calorieList,maxCalories)
