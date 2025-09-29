
def target():
    global target
    target = input("Enter company name: ")
    print (target)
    end = target.rsplit(".", 1)[-1]