def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    try: 
        fhand = open(file_name)
    except:
        print(f'Error, unable to open {file_name}')
        quit()

    daily_email_count = dict()

    for line in fhand:
        if line.startswith('From '):
            words = line.split()
            daily_email_count[words[2]] = daily_email_count.get(words[2],0) + 1

    print(daily_email_count)
    
    fhand.close()



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()