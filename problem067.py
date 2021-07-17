from io import open
from max_path_sum import maxPathSum

triangle_file = open('p067_triangle.txt', 'r')

triangle = []
rows = triangle_file.readlines() # almaceno todas las filas del triángulo en la variable
tempNum = ''
tempRow = []

for i in range(len(rows)):
	for num in rows[i]:
		if num == ' ':
			tempRow.append(int(tempNum))
			tempNum = ''
		elif num == '\n': 
			tempRow.append(int(tempNum))
			triangle.append(tempRow)
			tempRow = []
			tempNum = ''
		else:
			tempNum += num
			if len(rows)-1 == i and rows[i][-2:] == tempNum: # si tempNum reserva el último número de la última fila
				tempRow.append(int(tempNum))
				triangle.append(tempRow)
				tempRow = []
				tempNum = ''

triangle_file.close()

print(maxPathSum(triangle))

# [Finished in 285ms]