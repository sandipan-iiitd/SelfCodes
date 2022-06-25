#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("This is my first program from ineuron")


# In[2]:


#my name is sandipan


# In[3]:


""""sfsshfsh
fjkgkjgkj
gvhjgklh
dsgdf
gjgk"""


# In[4]:


"""print("fhjgkjg")
print("gkjgjkhkh")
print("hjkhkjh")"""


# In[5]:


a=10


# In[6]:


get_ipython().run_line_magic('whos', '')


# In[7]:


type(a)


# In[8]:


id(a)


# In[9]:


a,b=45,78


# In[10]:


a,b


# In[11]:


print(a,b)


# In[12]:


type(b)


# In[13]:


a,b


# In[14]:


a=True 


# In[15]:


type(a)


# In[16]:


c=True


# In[17]:


d=False


# In[18]:


type(c)


# In[19]:


type(d)


# In[20]:


print(True+True+True+False+True)


# In[21]:


print(False-True+True)


# In[22]:


n=45+6j


# In[23]:


type(n)


# In[24]:


n=45+6j


# In[25]:


type(n)


# In[26]:


n.real


# In[27]:


n.imag


# In[28]:


n=8+7j


# In[29]:


m=5+6j


# In[30]:


m*m


# In[31]:


n*m


# In[32]:


x=str(1)+"sudh"


# In[33]:


type(x)


# In[34]:


get_ipython().run_line_magic('whos', '')


# In[35]:


1+1.0


# In[36]:


int(1.0)


# In[37]:


float(7.8)


# In[38]:


int(7.8)


# In[39]:


x="sudh"+"sudh"+"sudh"


# In[40]:


x


# In[41]:


a=int(input("Enter a number:"))
print("The number is:" , a)


# In[42]:


type(a)


# In[43]:


a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))


# In[44]:


d=(a+b)/c


# In[45]:


c1=8+5j


# In[46]:


x=d+c1


# In[47]:


str(x)+"Sandipan"


# In[48]:


a=int(input("Enter a number less than 34:"))


# In[49]:


if(a<34):
    print("The data is less than 34")
elif(a<100):
    print("The data is lesser than 100")
else:
    print("Not less than 34")


# In[50]:


sal= int(input("Enter the salary of person P1:"))


# In[51]:


if(sal>50000):
    print("Can afford a car")
    if(sal>75000):
        print("It's too high")
    else:
        print("Okayish")
elif(sal>20000 and sal<=50000):
    print("Can afford a bike")
elif(sal>10000 and sal<=20000):
    print("Can afford a cycle")
else:
    print("Can afford nothing")


# In[52]:


a=10
b=20
if (a==10 and b>20):
    print("This is a valid statement")
else:
    print("No output")


# In[53]:


a==10 and b > 20


# In[54]:


a=10
b=20
if (a==10 or b>20):
    print("This is a valid statement")
else:
    print("No output")


# In[55]:


f_name=input("Enter first name:")
l_name=input("Enter last name:")
if(f_name=='Sandipan' and l_name=='Das'):
    print("It's me")
elif (f_name=='Sandipan'):
    print('This is me too')
else:
    print("No it's not me")


# In[56]:


if a == 10:
    print("This is valid")


# In[57]:


for i in (1,10):
    print(i)


# In[58]:


initial_speed=0
final_speed=100
c=0
while(initial_speed<=final_speed):
    print("initial_speed is now:",initial_speed)
    initial_speed=initial_speed+1
    c=c+1
    if(c==10):
        break


# In[59]:


notes=5
i=1
j=1
while(i<notes):
    print(i)
    i=i+1
else:
    while(j<=2):
        print(j)
        j=j+1
    print("Ten rupees not available")


# In[60]:


s="my name is sandipan"


# In[61]:


s[::-1]


# In[62]:


s[10:3:-1]


# In[63]:


s[2:-6]


# In[64]:


for i in s:
    print(i)
    if(i=='s'):
        print("We have got 's' in string")
        break


# In[65]:


for i in s:
    if(i=='n'):
        pass
    print(i)
else:
    if(i=='u'):
        print("The last letter was 'u'")
    print("this is a else condition")


# In[67]:


s=input("Enter the string:")
s1=""
for i in range(len(s)):
    if(s[i]=='n'):
        s1=s1+s[i]
print(s1)


# In[68]:


n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end="")
    print("\r")
        


# In[69]:


for i in range(0,10,2):
    print(i)


# In[70]:


n=7
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(0,2*i-1):
        print("*", end='')
    print("\r")


# In[71]:


l=["Sandipan", 8334912135,"Dumdum"]


# In[72]:


type(l)


# In[73]:


l[0]


# In[74]:


l[1]=7278606803


# In[75]:


l


# In[76]:


l2=list()


# In[77]:


l2


# In[78]:


l2.append(1)


# In[79]:


l2


# In[80]:


l2.append("Sandipan")


# In[81]:


l2


# In[82]:


l2.append([3,4,5])


# In[83]:


l2


# In[84]:


l2.append(8+5j)


# l2

# In[85]:


l2


# In[86]:


for i in l2:
    print(i,"->",type(i))
    if(type(i))==list:
        sum=0
        for j in i:
            print(j,"->",type(j))
            sum=sum+j
print('The sum of elements in the inner list:',sum)


# In[87]:


l2[0:3]


# In[88]:


s="Sandipan"
for i in s:
    print(i, end="")


# In[89]:


a="Sandipan"


# In[90]:


b="Sandy"


# In[91]:


a


# In[92]:


b


# In[93]:


c


# In[94]:


get_ipython().run_line_magic('whos', '')


# In[ ]:





# In[97]:


len(c)


# In[98]:


b="Sachin Tendulkar"


# In[99]:


c=0
for i in b:
    c=c+1
print("The length of the string is:",c)


# In[100]:


b


# In[101]:


x=list(b)


# In[102]:


x[0]


# In[103]:


x[0]='b'


# In[104]:


x


# In[105]:


str(x)


# In[106]:


print(x)


# In[107]:


s="Sandy"


# In[108]:


s*3


# In[109]:


s.find("a")


# In[111]:


s[-1:-10:-1]


# In[112]:


for i in s:
    print(i)


# In[113]:


s


# In[114]:


len(s)


# In[118]:


s[::-1]


# In[119]:


s[0]


# In[120]:


s[0]='x'


# In[123]:


s=input("Enter a string:")


# In[125]:


c=0
l=len(s)
for i in s:
    if(i=='a'):
        c=c+1
        if(c==1):
            break
print("Total no. of a's are:",c)


# In[126]:


s.find('a')


# In[129]:


s.index('and')


# In[130]:


s='My name is'


# In[131]:


s


# In[132]:


f=s.find('name')


# In[133]:


f


# In[135]:


for i in range(len('name')):
    print(f+i)


# In[136]:


s.count('name')


# In[137]:


s.split()


# In[141]:


type(s.split('n'))


# In[142]:


s


# In[143]:


s.upper()


# In[144]:


s.lower()


# In[145]:


s.swapcase()


# In[146]:


reversed(s)


# In[147]:


for i in reversed(s):
    print(i)


# In[148]:


s[::-1]


# In[149]:


s=" sandipan "


# In[150]:


s.strip()


# In[151]:


s="sa ndipan"


# In[154]:


s.lstrip()


# In[155]:


s="My name is Sandipan"


# In[160]:


s=s.replace("Sandipan","Sandy")


# In[161]:


s


# In[162]:


s.center(20,'b')


# In[163]:


s="My name is Sandipa\tn"


# In[164]:


s


# In[165]:


s.expandtabs()


# In[166]:


a="We all are a part of Full Stack"


# In[167]:


a


# In[168]:


a.lower()


# In[169]:


a.count('a')


# In[173]:


x=len(a)
for i in range(x):
    if(a[i]=='a'):
        print(i)


# In[174]:


a.replace('a','ineuron')


# In[175]:


a.split()


# In[178]:


for i in range(x,0):
    print(a[i])


# In[179]:


s="Sandipan"


# In[180]:


s.isupper()


# In[181]:


s.isnumeric()


# In[182]:


s.isalpha()


# In[183]:


s.endswith('n')


# In[184]:


s.istitle()


# In[187]:


a="This is a full stack batch"


# In[189]:


def length(str):
 c=0
 for i in a:
     c=c+1
 print("The length of the string is:",c)


# In[193]:


st=input("Enter a String:")


# In[195]:


x=length(st)


# In[200]:


for i in range(0,len(s)):
    print(s[-i])


# In[204]:


s="Sandipan"
vowel="AaEeiIoOuU"


# In[205]:


ch=len(s)-1
while(ch>=0):
    print(s[ch])
    ch=ch-1


# In[206]:


for i in s:
    if i in vowel:
        print(f'{i} is a vowel')
    else:
        print(f'{i} is not a vowel')


# In[228]:


s=input("Enter a string to be checked:")
s1=""
x=len(s)
ch=x-1
while(ch>=0):
    s1=s1+s[ch]
    ch=ch-1
print(s1)
if(s==s1):
    print("The string is palindrome")
else:
    print("The string is not palindrome")
    


# In[229]:


if(s==s1):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")


# In[230]:


l=["sandipan",56,87,99]


# In[231]:


l


# In[232]:


type(l)


# In[233]:


l[0]


# In[234]:


l[3:6]


# In[242]:


p=len(l)-1
l1=list()
while(p>=0):
    l1.append(l[p])
    p=p-1
print(l1)


# In[236]:


len(l)


# In[243]:


l[::-1]


# In[244]:


l+list("sudh")


# In[245]:


l.append("sudh")


# In[246]:


l


# In[247]:


"sandipan" in l


# In[ ]:




