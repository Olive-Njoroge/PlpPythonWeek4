file = open("yapper.txt", "r")
data = file.read()
print(data)

file = open("Yaaaay.pdf", "w",)
data1 = file.write("I'm so happy I learnt file handling")
print(data1)

try:
    with open("sample.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("The file was not found.")
except IOError:
    print("The file cannot be read.")
finally:
    print("yaaaay")