import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
num="+91"
info=str(input("enter your phone num : "))
num=num+info
ch=phonenumbers.parse(num,"CH")
print("your num from ",geocoder.description_for_number(ch,"en"))
sd=phonenumbers.parse(num,"RO")
print("your carrier is",carrier.name_for_number(sd,"en"))