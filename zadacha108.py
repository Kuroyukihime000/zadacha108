input_data = open('input.txt', 'r')
data = input_data.read()
                     
output_data = open('output.txt', 'w')
output_data.write(str(data)) 

input_data.close()
output_data.close()