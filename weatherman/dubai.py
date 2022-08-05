import csv


def year_wise_result(year):
        maximum_temp=[]
        minimum_temp=[]
        maximum_humid=[]
        max_temp_date = []
        min_temp_date=[]
        max_hum_date=[]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for i in range(len(months)):
            with open(f"dubai\\Dubai_weather_{year}_{months[i]}.txt", "r") as file:
                csvreader = list(csv.reader(file))
                #for i in csvreader:
                # print(i)


            max_temp=[]
            for i in range(1, len(csvreader)-1):
                max_temp.append(csvreader[i][1])

              
            maxTemp = max(max_temp)
            date_max_temp = max_temp.index(maxTemp) + 1
            maximum_temp.append(maxTemp)
            max_temp_date.append(date_max_temp)

            min_temp=[]
            for i in range(1, len(csvreader)-1):
                min_temp.append(csvreader[i][3])

            #print(min_temp)  
            minTemp = min(min_temp)
            date_min_temp = min_temp.index(minTemp) + 1
            minimum_temp.append(minTemp)
            min_temp_date.append(date_min_temp)


            max_hum=[]
            for i in range(1, len(csvreader)-1):
                max_hum.append(csvreader[i][7])

            #print(max_hum)  
            maxHum = max(max_hum)
            date_max_hum = max_hum.index(maxHum) + 1
            maximum_humid.append(maxHum)
            max_hum_date.append(date_max_hum)

           

        maximum_temp_int = []
        maxi_temp = list(filter(None, maximum_temp))
        
        for i in range(len(maxi_temp)):
            
            maximum_temp_int.append(int(maxi_temp[i])) 

        minimum_temp_int = []
        mini_temp = list(filter(None, minimum_temp))
        for i in range(len(mini_temp)):
            minimum_temp_int.append(int(mini_temp[i])) 
            
        maximum_hum_int = []
        maxi_hum = list(filter(None, maximum_humid))
        for i in range(len(maxi_hum)):
            maximum_hum_int.append(int(maxi_hum[i]))     

    # print(min_temp)
    # print(max_hum)
        index_max_temp = maximum_temp.index(str(max(maximum_temp_int)))
        index_min_temp = minimum_temp.index(str(min(minimum_temp_int)))
        index_max_hum = maximum_humid.index(str(max(maximum_hum_int)))

       
        print(f"Highest: {max(maximum_temp_int)}C on {months[index_max_temp]} {max_temp_date[index_max_temp]}")
        print(f"Lowest: {min(minimum_temp_int)}C on {months[index_min_temp]} {min_temp_date[index_min_temp]}")
        print(f"Humid: {max(maximum_hum_int)}% on {months[index_max_hum]} {max_hum_date[index_max_hum]}")

   



def month_wise_result(year, month):

        with open(f"dubai\\Dubai_weather_{year}_{month}.txt", "r") as file:
                csvreader = list(csv.reader(file))
            # for i in csvreader:
                #  print(i)


        max_temp=[]
        for i in range(1, len(csvreader)-1):
            max_temp.append(csvreader[i][1])

            #print(max_temp)  
    
        

        min_temp=[]
        for i in range(1, len(csvreader)-1):
            min_temp.append(csvreader[i][3])

            #print(min_temp)  
    
        


        mean_hum=[]
        for i in range(1, len(csvreader)-1):
            mean_hum.append(csvreader[i][8])

            #print(max_hum)  
        
        sum_h_temp=[]
        new_temp = list(filter(None, max_temp))
        for i in range(len(new_temp)):
            sum_h_temp.append(int(new_temp[i]))

        sum_l_temp=[]
        new_l_temp = list(filter(None, min_temp))
        for i in range(len(new_l_temp)):
            sum_l_temp.append(int(new_l_temp[i]))

        sum_hum=[]
        new_hum = list(filter(None, mean_hum))
        for i in range(len(new_hum)):
            sum_hum.append(int(new_hum[i]))

        avg_h_temp = sum(sum_h_temp) / len(sum_h_temp)
        avg_l_temp = sum(sum_l_temp) / len(sum_l_temp)
        avg_hum = sum(sum_hum) / len(sum_hum)            

        
        print(f"Highest Average: {avg_h_temp}C")
        print(f"Lowest Average: {avg_l_temp}C")
        print(f"Average Humidity: {avg_hum}%")

    


def graph(year, month):
    try:
        print(f"{month} {year}")
        with open(f"dubai\\Dubai_weather_{year}_{month}.txt", "r") as file:
            csvreader = list(csv.reader(file))
            # for i in csvreader:
                #  print(i)


        max_temp=[]
        for i in range(1, len(csvreader)-1):
            max_temp.append(csvreader[i][1])

            #print(max_temp)  
    
        

        min_temp=[]
        for i in range(1, len(csvreader)-1):
            min_temp.append(csvreader[i][3])

            #print(min_temp)  
    
        for i in range(len(max_temp)):
            num = int(max_temp[i])
            num2 = int(min_temp[i])
            print(f"\033[1;37;40m {i+1}" + " \033[1;31;40m +" * num +  " \033[1;34;40m +" * num2 + f"\033[1;37;40m {min_temp[i]}C-{max_temp[i]}C")  
            
    except:
        pass


#year_wise_result(2006)
#month_wise_result(2006, "Jul")
#graph(2006, "Jan")
