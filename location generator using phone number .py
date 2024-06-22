import phonenumbers 
from  phonenumbers import geocoder
phone_number1=phonenumbers.parse("9719513810 ")
# phone_number2=phonenumbers.parse("enter country code and mobile number")
# phone_number3=phonenumbers.parse("enter country code and mobile number")
# phone_number5=phonenumbers.parse("enter country code and mobile number")

# print("\n phonr numbers locations\n")
print(geocoder.description_for_number(phone_number1,"en"));
# print(geocoder.description_for_number(phone_number2,"en"));
# print(geocoder.description_for_number(phone_number3,"en"));
# print(geocoder.description_for_number(phone_number5,"en"));



