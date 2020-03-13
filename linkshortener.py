import pyshorteners

url = input("Please Enter the URL: ")

s = pyshorteners.Shortener()
print("Your Shortened URL is here -> ",s.tinyurl.short(url))
