def return_100():
    return 100


def return_param(param):
    return param


def hello_world():
    return "Hello World"
try:
    print("Podaj pierwsza liczbe: ")
    input1 = int(input())
    print("Podaj druga liczbe")
    input2 = int(input())
    print("Podaj operacje: (1=sum, 2=diff, 3=multiply, 4=divide")
    input_operation = input()
except SyntaxError:
    input1 = None
    input2 = None
    input_operation = None


def calc_sum(a, b):
    print("Pierwsza liczba: " + str(a) + " Druga liczba: " + str(b))
    suma = a + b
    print("Suma: " + str(suma))
    return suma


def calc_diff(a, b):
    print("Pierwsza liczba: " + str(a) + " Druga liczba: " + str(b))
    roznica = a - b
    print("Roznica: " + str(roznica))
    return roznica


def calc_multi(a, b):
    print("Pierwsza liczba: " + str(a) + " Druga liczba: " + str(b))
    mnozenie = a * b
    print("Mnozenie: " + str(mnozenie))
    return mnozenie


def calc_divide(a, b):
    print("Pierwsza liczba: " + str(a) + " Druga liczba: " + str(b))
    dzielenie = a/b
    print("Dzielenie:" + str(dzielenie))
    return dzielenie


if input_operation == 1:
    calc_sum(input1, input2)
elif input_operation == 2:
    calc_diff(input1, input2)
elif input_operation == 3:
    calc_multi(input1, input2)
elif input_operation == 4:
    calc_divide(input1, input2)
else:
    print("Please provide correct operation code")