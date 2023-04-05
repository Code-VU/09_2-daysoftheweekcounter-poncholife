def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    #file_name = 'mbox-short.txt'
    fhand = open(file_name)
    dictionary = dict()
    for line in fhand:
        if line.startswith('From '):
            lst = line.split()
            word = lst[2]
            if word not in dictionary:
                dictionary[word] = 1
            else:
                dictionary[word]= dictionary[word] +1
    
    print(dictionary)
            
    fhand.close()
    

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
