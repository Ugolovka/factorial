input_data = open("input.txt","r")
data = input_data.read()
a = int(data)
factorial = 1
for i in range(2, a+1):
    factorial *= i
output_data = open("output.txt","w")
output_data.write(str(factorial))
output_data.close()
input_data.close()