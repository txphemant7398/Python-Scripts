from art10 import logo 
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
   return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operation={
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
}


def calculator():
    print(logo)
    n1=float(input("First no: "))

    for symbol in operation:
        print(symbol)
        
    should_continue=True

    while should_continue:
        operation_symbol=input("operation : ")
        n2=float(input("next number: "))
        calculation=operation[operation_symbol]
        answer=calculation(n1,n2)


        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input(f"type 'y' if you want to continue with {answer} or 'n' if dont want to calculate: ")=="y":
            n1=answer
        else:
            should_continue=False
            calculator()
calculator()