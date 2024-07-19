from pyad import *
import csv


pyad.set_defaults(ldap_server="CESC.com",username="AD",password="wELCOME@1234")


#tutorial 1  Login Search Part

user=pyad.aduser.ADUser.from_cn("Sreedipta Karmakar")
print(user.get_attribute("useraccountcontrol"))

#tutorial 2  Bulk User Account

with open("user_data.csv") as f1:

    csvrow=csv.reader(f1,delimiter=",")
    i=0
    for row in csvrow:
        if(i>0):
          employeeID=row[1]
          givenName=row[2]
          sn=row[2]
          department=row[3]
          mail=row[4]
          sAMAccountName=row[5]
          company=row[6]
          new_user=pyad.aduser.ADUser.create()
          print(employeeID)
        i=i+1



#tutorial3 Delete Data

with open("user_data.csv")as f1:
   csvrow=csv.reader(f1,delimiter=",")
   i=0
   for row in csvrow:
       if(i>0):
         
           cn=row[5]
           pyad.aduser.ADUser.from_cn(cn).delete()
           print("Deleted user is:" + row[0])

         i=i+1


#tutorial4  Group creation  g_ou=container object

g_ou=pyad.adcontainer.ADContainer.from_dn("Ou")
group=pyad.adgroup.ADGroup.create("test")


#tutorial5 Update Group Membership
group=pyad.adgroup.from_cn("Test_Python")
with open("user_data.csv")as f1:
    csvrow=csv.reader(f1,delimiter=",")
    i=0
    for row in csvrow:
        if(i>0):
           cn=row[5]
           user=pyad.aduser.ADUser.from_cn(cn)
           
           group.add_members([user])
           print(i)
        i=i+1


#tutorial6
with open("group.csv")as f1:
    csvrow = csv.reader(f1,delimiter=",")
    i=0
    with io.open("membership.csv","a",encoding="utf-8") as f2:
        for row in csvrow:
            if(i>0):
             cn=row[0]
             group=pyad.adgroup.ADGroup.from_cn(cn)
             members=group.get_attribute("member")
             print(members)
             if( len(members)>0):
                  member="|".join(mem for mem in members)
                  data=cn+","+member+"\n"
                  f2.write()
            else:
              data=cn+","+"no member"+"\n"
              f2.write(data)

    i=i+1
    f2.close()
f1.close()



#tutorial7 Move Active Directory

user=pyad.aduser.ADUser.from_cn("aalamda")
ou=pyad.adcontainer.ADContainer.from_dn("CN=Users,DC=totaltechnology,DC=com")
user.move(ou)

with open("user_data.csv")as f1:
   csvrow=csv.reader(f1,delimeter=",")
   i=0
   for row in csvrow:
      user=pyad.aduser.ADUser.from_cn(row[5])
      user.move(ou)
      print(i)

      i=i+1

#tutorial8 Manipulation

#sinlgevalued attribute
ad_object=pyad.adobject.ADObject.from_cn("hvybvhu")
pyad.adobject.ADObject.update_attribute(ad_object,"info","")
print(len(ad_object.get_attribute("info")))

#multivalued attribute

ad_object=pyad.adobject.ADObject.from_cn("aalamda")
pyad.adobject.ADObject.append_to_attribute(ad_object,"proxyAddresses",["smtpta.com"])


#Tutorial9 Updating Multiple Attribute Together

user=pyad.aduser.ADUser.from_cn("aalamda")
user.update_attribute(("givenname":"pythonAshlin","sn":"pythonAlam","displayname":"python display"))

with open("user_data.csv") as f1:
     data=csv.reader(f1,delimiter=",")
     for row in data;
         cn=row[5]
         user=pyad.aduser.ADUser.from_cn(cn)
         fn=row[1]
         sn=row[2]
         dep=row[3]
         user.update_attributes({"givenname":"python"+" "+fn,"sn":"python"+""})
         print(f"{i}completed")


         i=i+1


#Tutorial10 Change AD User Password

cn=pyad.aduser.ADUser.from_cn("acharlen")
pyad.aduser.ADUser.set_password(cn, "New@1234")
print(pyad.adobject.ADObject._get_password_last_set(cn))

with open("permissions.csv","r")as f1:
    row=csv.reader(f1,delimiter=",")
    i=0
    for data in row:
        if (i>0) :
            dn=data[0]
            user=pyad.aduser.ADUser.from_dn(dn)
            pyad.aduser.ADUser.set_password(user, "New1234")
            print(pyad.adobject.ADObject._get_password_last_set(user))

        i=i+1


#Tutorial11 get AD User Account Expiration Date
#get account expiration from AD

from pyad import *
from pyad.pyadutils import *
import datetime
user=pyad.aduser.ADUser.from_cn("aalamda")
expirationdate=pyad.pyadutils.convert_datetime(user.get_attribute("accountexpires",False)):
print(expirationdate)



#Tutorial12 Set AD User Account Expiration Date
from pyad import *
import datetime

user=pyad.adobject.ADObject.from_cn("alaamda")

pyad.adobject.ADObject.update_attribute(2025,5,11,0,0)

pyad.adobject.ADObject.update_attribute(user,"accountExpires",str(ed))


#Tutorial13 Connect AD from Local Machine

from ldap3 import Connection, Server
server=Server("62.75.216.81")
con=Connection("62.75.216.81","totaltechnology\\administration","Rambo@3322",auto_bind=True)
print(con.extend.standard.who_am_i())
con.search("DC=totaltechnology,DC=com","{objectcategory=person}")
print(con.entries)




