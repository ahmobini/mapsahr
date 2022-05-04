# Not working correctly. However the math behind it is correct.


class Values:

	def __init__(self, value, weight, Leftcapacity):
		self.value = value
		self.weight = weight
		self.LeftCapacity = LeftCapacity


class FractionalKnapsack:

	@staticmethod
	def SortAndMaximizing(value, weight, LeftCapacity):
		itemValue = []
		for i in range(len(weight)):
			itemValue.append(Values(value[i], weight[i], i))
		itemValue.sort(reverse=True)
		totalValue = 0
		for i in itemValue:
			if weight[i] < LeftCapacity: 
				LeftCapacity -= weight[i]
				totalValue += itemValue

			else:
				fraction = LeftCapacity / weight[i]
				totalValue += itemValue * fraction

		return totalValue		



if __name__ == "__main__":
	weight = [1, 2, 3, 4]
	value = [10, 90, 150, 30]
	LeftCapacity = 60

	maxValue = FractionalKnapsack.SortAndMaximizing(value, weight, LeftCapacity )
	print("Maximum value in Knapsack =", maxValue)10