import  re
my_file = open("access.log", "r")
for line in my_file:
    line
repdata = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', line)
print(repdata)
my_file2 = open("output.txt", "w")
my_file2.write(repdata)
my_file2.close()

