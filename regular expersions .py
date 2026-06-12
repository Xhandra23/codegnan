'''
#regular expression (RegEx)
#-------------------------
s
--> RegEx is a sequence of char that from a searching pattern...
-->this can be used to cheeck if a string contian the specified search pattern

-->python has  a built-in package called 're' which can be used to work with RegEx..

functions in re
---------------
1.Findall
2.search
3.fullmatch

metachar
--------
[]-->a-z,A-Z,0-9 and any specified squence..
.--> here each dot is one char
^-->this look for the, string is starting with specified squence or not
$-->this look for the ,string is ending with specified squence or not
*--> zero or more
?-->zero or one
+-->one or more
{}-->


special squence
-----------------
\S-->No space
\s--> only spaces
\D--> Non-digits
\d-->only-digits
\w-->matchs any word char(letters,digits,underscore)
\W-->non words


'''
'''
import re
w= "fdjklw fdlkslkngfl rrejfln,mgdrlksj dnfslkknfdls fgnlnslkd"
print(re.findall('[k-m]',w))

'''
'''
import re
w= " Python is fdjklw fdlkslkngfl rrejfln,mgdrlksj chandhuu dnfslkknfdls fgnlnslkd"
print(re.search('cha...u',w))
'''
'''
import re
w= "fdjklw fdlkslkngfl rrejfln,mgdrlksj  sai dnfslkknfdls fgnlnslkd"
print(re.findall('^fdjklw',w))
print(re.findall('lkd$',w))
print(re.findall('s.*i',w))
print(re.findall('s.?i',w))
print(re.findall('s.+i',w))
print(re.findall('s.{3}',w))
print(re.findall('\S',w))
print(re.findall('\w',w))'''

import re
mobile=input("enter  10 digit mobile num:")
how= re.fullmatch('[6-9][0-9]{9}',mobile)
if how :
    print(f"{mobile} is indian mobile number")
else:
    print(f"{mobile} is not indian")
