def wait(function):
    def working():
        print("wewaea")     # this does something before actual function call
        function()
        print("wfawfwaf")   # this does something after function call
    return working

@wait               # this is another function which adds some functionality on top of other function
def show():
    print("awoooo")

show()

def p():
    print("awooo")
"""this 2 lines below can be written as decorator     @wait"""
new_fun = wait(p)
new_fun()