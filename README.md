# CS-4320-Internet-Programming
Python programming projects for CS 4320 (Kennesaw State University). Projects are based on python and Unix environments, as well as other web scripting languages.  

Client/Server Using Sockets

Create two Python scripts: one a server; the other a client that will use the server. You will use the loan function module you created in the last assignment. Do not include those functions directly into your server code, but import them into the server.1

Server

The server will listen on port 12321. It will carry out loan computations using the functions you created in Assignment #1. Requests are in one of two formats:

Payment format: The request is a string beginning with capital ‘P’ and followed by an initial balance, a single space, an annual interest rate (in decimal), a single space and a number of months.
Balance format: The request is a string beginning with capital ‘B” and followed by a month number, a single space, an initial balance, a single space, an annual interest rate (in decimal), a single space and the monthly payment
For example, a payment request might be in the form

    P10000 0.1 12
This is a loan with an initial balance of 10000, an annual interest rate of 10% and a term of 12 months.

A balance request might be in the form

    B13 10000 0.1 879.1588723000987
This is for month 13 with an initial balance of 10000, an annual interest rate of 10% and a monthly payment of 879.1588723000987.

The server will create a response to the client for each request. The first character of the response will indicate the type of response:

‘E’ indicates an error response. The remainder of the response is an error message
‘B’ indicates a response to a balance request. The remainder of the response is the balance remaining on the loan at the end of that month (the remainingBalance function)
‘P’ indicates a response to a payment request. The remainder of the response is the monthly payment that will pay off the loan in the time specified.
The response to the example payment request would be

    P879.1588723000987
The response to the example balance request would be2

    B-3.296918293926865e-11
Server Error Checking

The server should respond properly in the case of an erroneous request. Not only should the server not ‘crash’ but the server should send back an appropriate error response to the client.

For example, the request string

    P10000 .10 24a
should result in a response something like this:

    Einvalid format numeric data
Note the ‘E’ that flags this as an error message.

Include error checking in the server. Also document the error checking by including a string at the end of the server code that describes the errors caught. That string might look something like this (to start with):

'''
Invalid numeric format

Wrong number of fields in request

'''
Client

You are strongly urged to write small clients that will test aspects of your server as you work on that. Once you are satisfied that you can send a payment request and get a good result and also send a balance request and get a good result then work on the client described here.

The client script will accept three command line arguments: the initial balance; the annual interest rate as a percentage; and, the number of months in the term of the loan. So, if your script is named loan_client.py, it might be invoked from the command line as

loan_client.py  10000  10 12
for a loan with an initial balance of $10,000 borrowed at an annual rate of 10% due in 12 months.

The client will send a payment request to the server with the given input parameters. Then, the client will take the payment amount and send to the server a balance request where the month number is one more than the term of the loan. The client should print the payment amount (suitably labeled) formatted to two decimal places. The client should print the balance amount (suitably labeled) as received.

Note that, with sane input, the balance printed should be very close to 0.

If either response to the client is an error, the client should print the error message and immediately halt.
