average_1 = [1, 2, 3, 4, 5, 6]
average_2 = [10, 11, 12, 13, 14, 15, 16, 17]
average_3 = [110, 110]

def average(average_list):
    result_average = sum(average_list) / len(average_list)
    print(result_average)
  
average(average_1)
average(average_2)
average(average_3)