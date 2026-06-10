'''
Error Handling
--------------
try block
---------
--> the try block,test a block of code for error

except block
------------
--> the expect block let hand if the code contain error...
eg.
try :
   print(12/0)
except:
    print("hsgfgffelmfdm,,")

else block
-----------
--> this will be excuted ,if the try block has no error in the code...
eg.
--
try :
    print("sfkjfkj,")
except:
    print("jjlslt")
else:
    print("jdlkflktylklt;;")

finally block
-------------
-->this will be excuted either try block contain error or not...




'''

try :
    print(4+"a")
    print(a)
except NameError:
    print("jjlslt")
except TypeError:
    print("jjdfj")
else:
    print("jdlkflktylklt;;")
finally:
    print("kjhdfskjdjjdsls")
