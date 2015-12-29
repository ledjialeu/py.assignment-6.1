#Write code using find() and string slicing to extract the number
#at the end of the line below.
#Convert the extracted value to a floating point number and print it out
text = "X-DSPAM-Confidence:    0.8475" # Given the string named text
ant = text.find('0') # we find the position of 0
pos = text.find('5') # we do the same with 5
host = text[ant:pos + 1] # Using string slicing, we extract the portion of the our string
num = float(host) # We convert the extracted value to a floating point number
print num # we print the number
