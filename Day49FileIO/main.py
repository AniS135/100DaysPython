# Reading A File

# f = open('Day49FileIO\myfile.txt', 'r')

# # print(f)
# # r (read mode) is a default mode
# # w (write mode), If file doesn't exist then it will create file
# # a (append mode), If we want to append content in file, else work same as w
# # x (create), this mode creates a file and throws error if already exist
# # t (text)
# # b (binary)

# text = f.read()
# print(text)

# f.close()

# Wrirting A File

# f = open('Day49FileIO\myfile.txt', 'a')
# f.write('Hello World!')

# f.close()

with open('Day49FileIO\myfile.txt', 'w') as f:
    f.write('I am inside in file')
