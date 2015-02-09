__author__ = 'Teddy'

import socket
import Loans


host = socket.gethostname()
port = 12321


def main():
    sock = socket.socket()

    sock.bind((host, port))

    sock.listen(1)
    print("sever listening...")

    while True:

        try:
            (connection, address) = sock.accept()
            print("connection to client successful")
            connection.send(b"thanks for connecting!")


            sock.listen(1)
            print("\nwaiting for request...")
            request = connection.recv(1024)

            if request == '\n':
                request = 'no request'

            print("request from connected client: " + bytes.decode(request))
            response = get_response(bytes.decode(request).lstrip())

            connection.send(str.encode(response))
            print("response sent: ",response)

            connection.close()
            print("+--connection to client closed--+")
            print("\nsever listening...")

        except ConnectionResetError:
            sock.listen(1)
            print("\nsever listening...")
        except ConnectionAbortedError:
            sock.listen(1)
            print("\nsever listening...")


def get_response(request):

    if not request:
        print('+--error: no request--+')
        return('+--Einvalid request--+')
    if request[0] != 'B' and request[0] != 'P':
        print("+--unknown request: no 'B' or 'P'--+")
        return '+--EInvalid request--+'
    elif request[0] == 'B':
        return analyze_balance(request)
    else:
        return analyze_payment(request)


def analyze_balance(request):

    args = request.split(" ")
    args[0] = args[0][1:len(args[0])]

    if len(args) != 4:
        print('+--error: wrong number of parameters in request --+')
        return '+--Ewrong number of parameters in request--+'

    else:
        try:
            month = int(args[0])
            initial_balance = float(args[1])
            rate = float(args[2])
            monthly_payment = float(args[3])
        except ValueError:
            print('+--error: invalid numeric format--+')
            return '+--Einvalid numeric format--+'

    return calculate_balance(month, initial_balance, rate, monthly_payment)


def analyze_payment(request):

    args = request.split()
    args[0] = args[0][1:len(args[0])]

    if len(args) != 3:
        print('+--error: wrong number of parameters in request --+')
        return '+--Ewrong number of parameters in request--+'
    else:
        try:
            initial_balance = float(args[0])
            rate = float(args[1])
            number_of_months = int(args[2])
        except ValueError:
            print('+--error: invalid numeric format--+')
            return '+--Einvalid numeric format--+'

    return calculate_payment(initial_balance, rate, number_of_months)


def calculate_balance(month, initial_balance, rate, monthly_payment):

    if month < 1:
        print('+--error: wrong format for month (must be > 0)--+')
        return '+--Einvalid month parameter--+'
    if rate <= 1E-10:
        print('+--error: wrong format for rate (must be > 0)--+')
        return '+--Einvalid or unexpected rate parameter--+'
    if initial_balance <= 1E-10:
        print('+--error: wrong amount of initial balance (must be > 0)--+')
        return '+--Einvalid or unexpected initial balance parameter--+'
    if monthly_payment <= 1E-10:
        print('+--error: wrong amount of monthly payment (must be > 0)--+')
        return '+--Einvalid or unexpected monthly payment parameter--+'

    try:
        balance = Loans.remaining_balance(month, initial_balance, rate*100, monthly_payment)
        return 'B' + {}.format(str(balance))
    except ZeroDivisionError:
        print('error: user input resulted to division by zero')
        return '+--Eunexpected input--+'


def calculate_payment(initial_balance, rate, number_of_months):
    if initial_balance <= 1E-10:
        print('+--error: wrong amount of initial balance (must be > 0)--+')
        return '+--Einvalid or unexpected month parameter--+'
    if rate <= 1E-10:
        print('+--error: wrong format for rate (must be > 0)--+')
        return '+--Einvalid or unexpected rate parameter--+'
    if number_of_months <= 1E-10:
        print('+--error: wrong format for number of months (must be > 0)--+')
        return '+--Einvalid or unexpected value for number of months--+'

    payment = Loans.compute_monthly_payment(initial_balance, rate*100, number_of_months)
    return 'P' + str(payment)

if __name__ == "__main__":
    main()
