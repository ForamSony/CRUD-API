# try:
#     a = 2
#     b = 20
#     c = b/a
#     print(c)
# except:
#     print("We can't divide by zero")


# try:
#     a = [1,2,3]
#     print(a[6])
# except:
#     print("index error")


try:
    #a = [1,2,3]
    #print(a[6])

    a = 10
    b = 5
    c = a/0
    print(c)

    d = "darta"
    e = b + d

except ZeroDivisionError:
    print("Can't Divide by zero")

except TypeError:
    print("Type Mismatch")

except Exception as e:
    print(f"Error please solve {e}")

else: # execute with try
    print('no exception')

finally:
    print("Always execute this block")