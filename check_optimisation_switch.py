import dis

""" Module docstring """
def return_true_always()-> bool:
    return True

def my_func()-> None:
    """ Function DocString """
    assert return_true_always(), "Assert works"
    if False:
        print("Asset never runs")
    if __debug__:
        print("This wil print only in debug mode")

my_func()

dis.dis(my_func)

