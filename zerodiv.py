def zerodiv():
    return 5/0

try:
    zerodiv()

except ZeroDivisionError as z:
    print(z)

except Exception as e:
    print(e)
