import requests
# url="https://shantanuuchak.tech"
# request=requests.get("https://shantanuuchak.tech")
# urls = ["https://shantanuuchak.tech" ,"https://www.unifize.com/"]
# urls=["https://shantanuuchak.tech", "http://innovaccer.com/contact-us","http://www.infogain.com/about/contact-us/"]

# function to splite
def split_data(text):
  return text.split('"')

# remove mailto:
def remove_mailto(text):
  return text.replace("mailto:","")
  
# func to find email list
def find_email(data_list):
  email_list=[]
  for el in data_list:
    if "@"in el and "." in el and not "/" in el:
      # email_list.append(el)
      email_list.append(remove_mailto(el))
  return email_list
  
# function to request to url
def fetch(url):
  res = requests.get(url)
  if res.status_code == 200:
    return res.text
  print("failed with error code{requets.status_code}")
  return ""

# taking point
urls=[]

while True:
  user_input=input("enter a url or N to exit:")
  if user_input=="N":
    print("URL list Ready")
    break
  if "://" not in user_input:
    print("enter a valid url")
  else:
    urls.append(user_input)
    

# x=fetch(urls[0])
# print(x)
  

# perfrom function request
# if requests.status_code==200:
#   data_list=splite_data(requests.text)
#   emails=find_email(data_list)
#   print(emails)
# else:
#   print(f"requets error.try_again {requests.status_code}")

# iterating over url list
# for url in urls:
#   data = fetch(url)
#   data_list = split_data(data)
#   email_list = find_email(data_list)
#   print(email_list)

emails=[]

for url in urls:
  data = fetch(url)
  data_list = split_data(data)
  email_list = find_email(data_list)
  emails.extend(email_list)
  # print(emails)

# unique_emails=[]
# for email in emails:
#   if not email in unique_emails:
#     unique_emails.append(email)
    
# print(unique_emails)

# for sets
email=set(emails)
print(email)

f=open('emails.txt','w')
f.write(str(emails))
f.close()









    


      
 
  
  
  
  
  

    
  
  

  
  
 
    