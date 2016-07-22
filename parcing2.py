import re
my_file = open("access.log", "r")
my_file2 = open("output.txt", "w")

result = []
for i in range(5):
    line = my_file.readline()
    ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line)
    date = re.findall('\W\d{1,2}\W\w{1,3}\W\d{1,4}\W\d{1,2}\W\d{1,2}\W\d{1,2}\s\W\d{1,4}\W', line)
    print("IP =", ip, " ", "DATE =", date, " ")
    result.append(str(ip) + " " + str(date) + "\n")

for n in result:
    my_file2.write(n)


my_file2.close()




