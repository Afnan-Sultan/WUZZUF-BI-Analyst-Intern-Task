def remove_columns():
    infile = open("Wuzzuf_Job_Posts_Sample.csv", encoding="utf8")
    outfile= open("Wuzzuf_Job_Posts_Sample_cleaned.csv","w", encoding="utf8")
    weird_values = 'ÃƒËœÃ‚Â£Ãƒâ„¢Ã†â€™ÃƒËœÃ‚ÂªÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â±', 'ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¨Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â§', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¹Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¥ÃƒËœÃ‚Â³Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¹Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â´Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂªÃƒËœÃ‚Â\xadÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â±', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â§ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂªÃƒËœÃ‚Â¬Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¹ ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â£Ãƒâ„¢Ã‹â€\xa0Ãƒâ„¢Ã¢â‚¬Å¾', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â²ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â²Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â§ÃƒËœÃ‚Â¶', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚ÂºÃƒËœÃ‚Â±ÃƒËœÃ‚Â¯Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â© ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¬ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â© ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã†â€™ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â°', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©-ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â£ÃƒËœÃ‚Â³Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â©', 'ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±Ãƒâ„¢Ã¢â‚¬Â¡', 'ÃƒËœÃ‚Â\xadÃƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã‹â€\xa0ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â\xa0', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚Â© ÃƒËœÃ‚Â¨ÃƒËœÃ‚Â¯ÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚Â¯Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â\xa0Ãƒâ„¢Ã¢â‚¬Â¡ Ãƒâ„¢Ã¢â‚¬Â\xa0ÃƒËœÃ‚ÂµÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦ÃƒËœÃ‚ÂµÃƒËœÃ‚Â±', 'Ãƒâ„¢Ã¢â‚¬Â¦Ãƒâ„¢Ã¢â‚¬Â\xa0 ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â¯Ãƒâ„¢Ã¢â‚¬Å¡Ãƒâ„¢Ã¢â‚¬Â¡Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã…Â\xa0Ãƒâ„¢Ã¢â‚¬Â¡-ÃƒËœÃ‚Â§Ãƒâ„¢Ã‹â€\xa0 ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾Ãƒâ„¢Ã¢â‚¬Å¡ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Â¡ÃƒËœÃ‚Â±ÃƒËœÃ‚Â©', 'Ãƒâ„¢Ã†â€™Ãƒâ„¢Ã‚Â\x81ÃƒËœÃ‚Â± ÃƒËœÃ‚Â§Ãƒâ„¢Ã¢â‚¬Å¾ÃƒËœÃ‚Â´Ãƒâ„¢Ã…Â\xa0ÃƒËœÃ‚Â®'
    weird_char = set()
    for index in weird_values:
        for char in index:
            weird_char.add(char)      
    #removed_columns=0
    for line in infile.readlines():
        #line.rstrip()
        content = line.split(sep="\t")
        if content[1][0] not in weird_char:
            outfile.write(line)  
    infile.close()
    outfile.close()

  
def clean_cities():
    infile = open("Wuzzuf_Job_Posts_Sample_cleaned.csv", encoding="utf8")
    cities = [ ]
    for line in infile.readlines():
        line.strip()
        content = line.split(sep="\t")
        cities.append(content[1])      
    temp = 0
    for city in cities:
        symbols=("/", " /", " / ", "/ ", " - ", " -", "- ", "&", "& ", " &", " & ") 
        for symb in symbols:
            if symb in city:
               cities[temp] = city.replace("symb","-")
        if ("ctober" in city  or "6-Oct" in city or "6" in city) and "-" not in city:
            cities[temp] = "6th of October"
        elif ("amadan" in city or "10" in city) and "-" not in city:
            cities[temp] = "10th of Ramadan"
        elif "lex" in city and "-" not in city :
            cities[temp] = "Alexandria"
        elif "All " in city or "all " in city or "any " in city or "Any " in city or "Any" in city or "al " in city:
            cities[temp] = "All Governorates" 
        elif "anso" in city and "-" not in city :
            cities[temp] = "Mansoura"                
        temp +=1
    outfile=open("test.csv","w",encoding="utf8")
    for city in cities:
        write=city+"\n"
        outfile.write(write)
    outfile.close()

def clean_experience():
    infile = open("Wuzzuf_Job_Posts_Sample_cleaned.csv", encoding="utf8")
    exp_years = [ ]
    for line in infile.readlines():
        line.strip()
        content = line.split(sep="\t")
        exp_years.append(content[13])
    min_exp = [ ]
    max_exp = [ ]
    months =["Jan", "Feb","Mar", "Apr","May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec"]
    months_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for exp in exp_years:
        temp = 0
        for month in months:
            if month in exp:
                exp=exp.replace(month,str(months_num[temp]))
            temp += 1
        years = ",".join(char for char in exp if char.isdigit())
        years = years.split(sep="\t")
        years.sort()
        #print(years)
        if len(years) >= 2:
            min_exp.append(years[0])
            max_exp.append(years[len(years)-1])
        else:
            min_exp.append(years[0])
            max_exp.append("NS")
    #print([(min_exp, max_exp)])
    outfile=open("test2.csv","w",encoding="utf8")
    for i in range(len(min_exp)):
        if max_exp[i] != "NS":
            experience_years = str(min_exp[i]) +" to "+ str(max_exp[i])
        else:
            experience_years = str(min_exp[i])
        row = str(min_exp[i]) +","+ str(max_exp[i])+","+experience_years+"\n"
        outfile.write(row)
    outfile.close()   

def validate_tableau(): 
    infile = open("Wuzzuf_Job_Posts_Sample_cleaned1.csv", encoding="utf8")
    vacancies = { }
    temp=0
    for line in infile.readlines():
        line.strip()
        if "city" not in line:
            content = line.split(sep=",")
            #print(temp)
            #print(content[3], content[12])
            temp+=1
            if content[3] in vacancies:
                vacancies[content[3]] += int(content[12])
            else:
                vacancies[content[3]] = int(content[12])        
    for key,value in vacancies.items():
        print(key, ':', value, '\n')
            
#remove_columns()
#clean_cities()
clean_experience()