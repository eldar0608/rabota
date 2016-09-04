import sys
import re

class Parsing:


    def __init__(self):
        pass

    def ip(self):
        result = []
        my_file = open("access.log", "r")
        my_file2 = open("output.txt", "w")
        try:
            for i in range(1000):
                line = my_file.readline()
                ip = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s', line)
                print("IP =", ip, " ")
                result.append(str(ip) + " " + "\n")
            for n in result:
                my_file2.write(n)
        except:
            print("Ошибка попробуйте снова")
        finally:
            my_file2.close()


    def date(self):
        result = []
        my_file = open("access.log", "r")
        my_file2 = open("output.txt", "w")
        try:
            for i in range(1000):
                line = my_file.readline()
                date = re.findall('\W\d{1,2}\W\w{1,3}\W\d{1,4}\W\d{1,2}\W\d{1,2}\W\d{1,2}\s\W\d{1,4}\W', line)
                print("DATE =", date, " ")
                result.append(str(date) + " " + "\n")
            for n in result:
                my_file2.write(n)
        except:
            print("Ошибка попробуйте снова")
        finally:
            my_file2.close()

    def protocols(self):
        result = []
        my_file = open("access.log", "r")
        my_file2 = open("output.txt", "w")
        try:
            for i in range(1000):
                line = my_file.readline()
                protocols = re.findall('\S\GET\s\S\w{1,15}.\w{1,5}\s\w{1,5}\S\d.\d\S', line)
                print("PROTOCOLS =", protocols, " ")
                result.append(str(protocols) + " " + "\n")
            for n in result:
                my_file2.write(n)
        except:
            print("Ошибка попробуйте снова")
        finally:
            my_file2.close()

    def character(self):
        result = []
        my_file = open("access.log", "r")
        my_file2 = open("output.txt", "w")
        try:
            for i in range(1000):
                line = my_file.readline()
                character = re.findall('\ESS\s\w{1,7}\s.\w{1,7}.\s\w.\s\w{1,6}.\s\w{1,4}\s\d{1,6}.\s\w{1,4}\s\d.\d.\d{1,4}.\d{1,4}', line)
                print("PROTOCOLS =", character, " ")
                result.append(str(character) + " " + "\n")
            for n in result:
                my_file2.write(n)
        except:
            print("Ошибка попробуйте снова")
        finally:
            my_file2.close()

def main():
    a = Parsing()
    print("Выберите действия")
    print("Вывести ip адреса нажмите цифру 0 ")
    print("Вывести дату нажмите цифру 1 ")
    print("Вывести протоколы нажмите цифру 2")
    print("Вывести характеристику установки нажмите цифру 3")
    x = int(input("Введите цифру "))
    if x == 0:
        a.ip()
    elif x == 1:
        a.date()
    elif x == 2:
        a.protocols()
    elif x == 3:
        a.character()
    else:
        print("ОШИБКА ПОПРОБУЙТЕ ЕЩЕ РАЗ")



if __name__ == '__main__':
    main()


