


import pickle



file2 = open('TEXT2.TEXT', 'w')



with open('TEXT1.TEXT', 'r') as file1:

    for line in file1:

        for word in line.split():

            if word[0].lower() not in 'aeiou':

                file2.write(word + ' ')



file2.close()



with open('TEXT2.TEXT', 'r') as file:

    print file.read()
    
