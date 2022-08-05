import sys
import lahore
import murree
import dubai



option = str(sys.argv[1])

if option=="-e":
    year = str(sys.argv[2])
    city = sys.argv[3]
    if city == "/lahore":
        lahore.year_wise_result(year)
    elif city=="/dubai":
        dubai.year_wise_result(year)   
    elif city=="/murree":
        murree.year_wise_result(year)    

    else:
        print("Invalid")
        quit()


elif option == "-a":
    year_mon = sys.argv[2]
    city = sys.argv[3]
    if city=="/dubai":
        dubai.month_wise_result(year_mon[:4], year_mon[5:])

    elif city=="/lahore":
        lahore.month_wise_result(year_mon[:4], year_mon[5:])    

    elif city=="/murree":
        murree.month_wise_result(year_mon[:4], year_mon[5:])

    else:
        print("Invalid")
        quit()

elif option == "-c":
    year_mon = sys.argv[2]
    city = sys.argv[3]
    if city=="/dubai":
        dubai.graph(year_mon[:4], year_mon[5:])

    elif city=="/lahore":
        lahore.graph(year_mon[:4], year_mon[5:])    

    elif city=="/murree":
        murree.graph(year_mon[:4], year_mon[5:]) 
    else:
        print("Invalid")
        quit()
               

else:
    print("Invalid Option")
    quit()
