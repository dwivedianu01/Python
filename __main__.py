print ("Hi, I am always executed")
 
def read():
    print("func() in __main__.py")

if __name__ == "__main__":
    print ("Executed when run directly")
else:
    print ("Executed when imported")

#read()
