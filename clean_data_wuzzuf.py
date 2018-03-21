def remove_columns():
    '''
    This function makes a first round of cleaning by removing any row with distorted values
    '''
    #reading the file and opening another file for wrting
    infile = open("Wuzzuf_Job_Posts_Sample.csv", encoding="utf8")
    outfile= open("Wuzzuf_Job_Posts_Sample_cleaned.csv","w", encoding="utf8")
    
    #werd values were obtain from running the following command on the job posts file 
        #print(sorted(df.salary_average.value_counts().index.tolist())) after opening the file with pandas package
    weird_values = 'ÃƒËœÃ‚Â£Ãƒâ„¢Ã†â€™ÃƒËœÃ‚ÂªÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â±', 'ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¨Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â§', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¹Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¹Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â´Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂªÃƒËœÃ‚Â\xadÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â±', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â§ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂªÃƒËœÃ‚Â¬Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¹ ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â£Ãƒâ„¢Ã‹â€\xa0Ãƒâ„¢Ã¢â‚¬Å¾', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â²ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â²Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¶', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂºÃƒËœÃ‚Â±ÃƒËœÃ‚Â¯Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â© ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â© ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã†â€™ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â°', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â£ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â\xadÃƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â\xa0', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â© ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â\xa0Ãƒâ„¢Ã¢â‚¬Â¡ Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚ÂµÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0 ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¯Ãƒâ„¢Ã¢â‚¬Å¡Ãƒâ„¢Ã¢â‚¬Â¡Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â¡-ÃƒËœÃ‚Â§Ãƒâ„¢Ã‹â€\xa0 ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã‚Â\x81ÃƒËœÃ‚Â± ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â´Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â®'+'Ø£ÙƒØªÙˆØ¨Ø±', 'Ø§Ø¨Ù‡Ø§', 'Ø§Ù„Ø¥Ø³ÙƒÙ†Ø¯Ø±ÙŠØ© -Ø§Ù„Ù‚Ø§Ù‡Ø±Ø© -Ø§Ù„Ø¥Ø³Ù…Ø§Ø¹ÙŠÙ„ÙŠØ© -Ø´Ù…Ø§Ù„ Ø§Ù„ØªØ\xadØ±ÙŠØ±', 'Ø§Ù„Ø¥Ø³Ù…Ø§Ø¹ÙŠÙ„ÙŠØ©', 'Ø§Ù„Ø§Ø³ÙƒÙ†Ø¯Ø±ÙŠØ©', 'Ø§Ù„ØªØ¬Ù…Ø¹ Ø§Ù„Ø£ÙˆÙ„', 'Ø§Ù„Ø¬ÙŠØ²Ø©', 'Ø§Ù„Ø¬ÙŠØ²Ù‡', 'Ø§Ù„Ø±ÙŠØ§Ø¶', 'Ø§Ù„ØºØ±Ø¯Ù‚Ø©', 'Ø§Ù„Ù‚Ø§Ù‡Ø±Ø©', 'Ø§Ù„Ù‚Ø§Ù‡Ø±Ø© - Ø§Ù„Ø£Ø³ÙƒÙ†Ø¯Ø±ÙŠØ©', 'Ø§Ù„Ù‚Ø§Ù‡Ø±Ø© Ø§Ù„Ø¬Ø¯ÙŠØ¯Ø©', 'Ø§Ù„Ù‚Ø§Ù‡Ø±Ø© Ø§Ù„ÙƒØ¨Ø±Ù‰', 'Ø§Ù„Ù‚Ø§Ù‡Ø±Ù‡', 'Ø§Ù„Ù…Ù†ØµÙˆØ±Ø©', 'Ø§Ù„Ù…Ù†ØµÙˆØ±Ù‡', 'Ø\xadÙ„ÙˆØ§Ù†', 'ÙƒÙ\x81Ø± Ø§Ù„Ø´ÙŠØ®', 'Ù…Ø¯ÙŠÙ†Ø© Ø¨Ø¯Ø±', 'Ù…Ø¯ÙŠÙ†Ù‡ Ù†ØµØ±', 'Ù…ØµØ±', 'Ù…Ù† Ø§Ù„Ø¯Ù‚Ù‡Ù„ÙŠÙ‡ - Ø§Ùˆ Ø§Ù„Ù‚Ø§Ù‡Ø±Ø©'
    
    #extracting only unique characters from weird values 
    weird_char = set("<")
    for index in weird_values:
        for char in index:
            weird_char.add(char) 
    ##print(weird_char)
    
    #remove the rows with distorted data by removing any row that doesn't have enough fielrds, 
    #or any row with enough fildes but with distoted ID or city values 
    ##temp = 0 
    for line in infile.readlines():
        line.strip()
        content = line.split(sep=",")
        ##print(content)
        if len(content) > 2:
            if content[0] != '' and content[1] != '':
                if content[0][0] not in weird_char and content[1][0] not in weird_char:    
                    outfile.write(line)
        ##temp +=1
        ##print(temp)
    
    #closing opened files
    infile.close()
    outfile.close()

def clean_cities():
    '''
    This function performs the second round of cleaning by changng the different typing methods for one city, to a unified value.
    The function is concerned with the most used cities mainly
    '''
    
    #open the cleaned fle resulted from the previous function
    infile = open("Wuzzuf_Job_Posts_Sample_cleaned.csv", encoding="utf8")
    outfile=open("cleaned_cities.csv","w",encoding="utf8")
    
    #loop over city column in the cleaned file, and for each city, check the conditions and change it's name if needed.
    for line in infile.readlines():
        line.strip()
        
        #remove the spaces and different non-alphaperic characters with a uinfied one. 
        content = line.split(sep=",")
        city = content[1]      
        city = city.replace(" ","")
        symbols=('/',"&", '\\')
        for symb in symbols:
            if symb in city: city = city.replace(symb,"-")
            
        #start checkng the conditions for the following cities
        if "ctober" in city  or "Oct" in city or "6" in city:
            city = "6th of October"
        elif ("amadan" in city or "10" in city) and "-" not in city:
            city = "10th of Ramadan"
        elif "lex" in city and "-" not in city :
            city = "Alexandria"
        elif "All" in city or "all" in city or "any" in city or "Any" in city or "al " in city:
            city = "All Governorates" 
        elif "anso" in city and "-" not in city :
            city = "Mansoura" 
        elif city == "Giza-Cairo" or city == "giza-cairo" or city == "Giza-cairo" or city == "giza-Cairo":
            city = "Cairo-Giza"  
        write=city+"\n"
        outfile.write(write)
    
    #close the opened files    
    infile.close()
    outfile.close()

def clean_experience():
    '''
    This function is used to clean the experience column and unify it's content structure. It also perints addtional two column with minimun and maximum experience year for each job to be used when needed
    '''
    
    infile = open("Wuzzuf_Job_Posts_Sample_cleaned.csv", encoding="utf8")
    outfile=open("cleaned_experience.csv","w",encoding="utf8")

    #identifying months in letters and number to correct for excells automatc change for some nummber to dates
    months =["Jan", "Feb","Mar", "Apr","May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec"]
    months_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    #loop over the experience year column in the cleaned file
    for line in infile.readlines():
        line.strip()
        content = line.split(sep=",")
        exp = content[13]
        
        #correct for any date value and convert it to number
        temp = 0
        for month in months:
            if month in exp:
                exp=exp.replace(month,str(months_num[temp]))
            temp += 1
        
        #extract the numbers only -seperated bycomma- from the values that contain text. Split the numbers and sort them.
        years = ",".join(char for char in exp if char.isdigit())
        years = years.split(sep=",")
        years.sort()

        # the first number is the minimun, and the last one is the maximun (in case of different mentiond number of years)
        #unify the values by following this format ( min to max)
        if len(years) >= 2:
            min_exp = years[0]
            max_exp = years[len(years)-1]
        else:
            min_exp = years[0]
            max_exp = " "
        
        #correct for the values that have minimum years only without maximum
        if max_exp != " ":
            experience_years = str(min_exp) +" to "+ str(max_exp)
        else:
            experience_years = str(min_exp)
            
        #the content to be written in the new file 
        row = str(min_exp) +","+ str(max_exp)+","+experience_years+"\n"
        outfile.write(row)
    
    #close opened files    
    infile.close()
    outfile.close()   

#apply the function in this sequence. when the data is extracted, replace/copy the column you nee to your cleaned file. 
remove_columns()
clean_cities()
clean_experience()