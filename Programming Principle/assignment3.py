import csv
import sys
from operator import itemgetter
import matplotlib.pyplot as plt

def main():
   
    print('Enter the dataset filename or just press Enter to accept default.')

    # take user input with while loop
    while True:
        filename = input("File name (carbon.csv)")
        if filename != 'carbon.csv' and filename != '':
            print('ERR: That file was not found.')
        else:
            try: # try - except to prevent catch errors
                csv_file = open('/Users/cwall/Desktop/carbon.csv','r')
                csv_reader = csv.reader(csv_file)                
            except: 
                print('ERR: That file was not found.')
                

            print('----------------')
            print('Main Menu')
            print('----------------')
            print("(1) CO2 emissions breakdown \n(2) Maximun emissions per GPD"+
            "\n(3) Top 10 GHG countries\n(4) Energy consumption distribution \n(5) Exit")

            # user input 
            choice = input('Enter your choice: ')
            labels = csv_reader.__next__()
            data = [] # list to contain data for graphing

            # execute if for choice 1
            if  choice == '1':
                while True:
                    country_name = input('Please enter the country name: ')
                    found = False
                    for line in csv_reader:
                        name = line[0]
                        if country_name.lower() == name.lower(): # check user input
                            found = True
                            print(country_name.title(), ' CO2 emissions breakdown')
                            
                            chart_label = []
                            sum = 0.0
                            # looping from line 2 to 7 for carbon gas
                            for n in range(2,7):
                                if line[n] == '':
                                    continue
                                # get labels from the first line
                                label = labels[n].split('_')[0].capitalize() #get the gas name from the labels
                                value = round(float(line[n])*10**9/float(line[11]),2)
                                # count total gas per person
                                sum+=value
                                print(label,':', value)
                                data.append(value) # listing the value in data []
                                chart_label.append(label)
                            # print the out put
                            print('Total:', sum, 'kg per person')
                            print('Pie chart opens in a new window. Close it to continue...')
                            # use pie chart for graphing with data[] and chart label
                            plt.pie(data,labels =chart_label,normalize = True)
                            plt.title(country_name.title()+ ' CO2 emissions breakdown')
                            plt.show()
                    break 
                        #  if country name is not found, print error messages
                    if (not found): 
                        print('ERR: That is an invalid or unknown country.')
                
            # execute for choice 2
            elif choice =='2':
                for line in csv_reader:
                    ghg = line[8]
                    if ghg == '': # if has no value, continue the program
                        continue
                    # assign value of line[0] and line[12] to variable name and gdp
                    name = line[0]
                    gdp = line[12]
                    # calculate ghg per dollar
                    ghg_per_dollar = round((float(ghg)*10**9)/float(gdp),2)
                    data.append((name, ghg_per_dollar))
                data.sort(key=itemgetter(1),reverse=True) #sorting the data list
                # print the output
                print('The highest total -GHG(greenhouse gas) emissions per dollar of GDP country is ',data[0][0])
            
            # execute choice 3 
            elif choice == '3':
                print('Choose the greenhouse gas: \n1. Methane\n2. Nitrous Oxide\n3. Total')
                option = input('Select one:')
                # declare the highest greenhouse gas country names and its values 
                highest_country = []
                highest_gas_value = []
                # option 1 for methane gas
                if option =='1': 
                    for line in csv_reader:
                        methane = line[9]     
                        if methane =='':
                            continue
                        population = line[11]
                        name = line[0]
                        # calculate methane gas per capita
                        methane_per_capita = round((float(methane)*10**9)/float(population),2)
                        data.append((name,methane_per_capita))
                    data.sort(key=itemgetter(1),reverse=True)
                    # taking 10 highest country
                    for n in range(10):
                        highest_country.append(data[n][0])
                        highest_gas_value.append(data[n][1])
                    # print out the result
                    print('Bar chart opens in a new window. Close it to continue...')
                    # create bar chart
                    plt.bar(highest_country,highest_gas_value, color = 'maroon')
                    bar_width = 1
                    plt.ylabel('Total (tonnes per year)')
                    plt.xticks(rotation=30)
                    plt.title('Top 10 per-capita greenhouse gas emissions in 2016')
                    plt.show()

                # execute option 2
                elif option =='2': 
                    for line in csv_reader:
                        nitrous_oxide = line[10]     # assign line[10] to nitrous_oxide 
                        if nitrous_oxide =='': # continue the program if have none value
                            continue
                        population = line[11]
                        name = line[0]
                        # calculate nitrous oxide per capita
                        nitrous_oxide_per_capita = round((float(nitrous_oxide)*10**9)/float(population),2)
                        data.append((name,nitrous_oxide_per_capita))
                    data.sort(key=itemgetter(1),reverse=True)
                    # print out 10 highest country
                    for n in range(10):
                        highest_country.append(data[n][0])
                        highest_gas_value.append(data[n][1])

                    print('Bar chart opens in a new window. Close it to continue...')
                    ax = plt.bar(highest_country,highest_gas_value, color = 'maroon')
                    plt.ylabel('Total (tonnes per year)')
                    plt.xticks(rotation=30)
                    plt.title('Top 10 per-capita greenhouse gas emissions in 2016')
                    plt.show()
                
                #execute option 3
                elif option =='3': 
                    for line in csv_reader:
                        methane = line[9]
                        nitrous_oxide = line[10]   
                        if methane =='' and nitrous_oxide=='': # skip if value is none
                            continue
                        population = line[11]
                        name = line[0]
                        #  calculate total per capita
                        total_per_capita = round(((float(methane)+float(nitrous_oxide))*10**9)/float(population),2)
                        data.append((name,total_per_capita))
                    data.sort(key=itemgetter(1),reverse=True)
                    for n in range(10):
                        highest_country.append(data[n][0])
                        highest_gas_value.append(data[n][1])
                    #  draw bar chart
                    print('Bar chart opens in a new window. Close it to continue...')
                    ax = plt.bar(highest_country,highest_gas_value, color = 'maroon')
                    plt.ylabel('Total (tonnes per year)')
                    plt.xticks(rotation=30)
                    plt.title('Top 10 per-capita greenhouse gas emissions in 2016')
                    plt.show()        
                else:
                    print('ERR: Invalid choice.') #print error if user input invalid 
            #  execute choice 4
            elif choice =='4':
                for line in csv_reader:
                    energy_consumption = line[13]
                    population = line[11]
                    #calculate energy consumption per capita
                    energy_consumption_percapita = round((float(energy_consumption)*10**6)/float(population),2)
                    data.append(energy_consumption_percapita)
                print('Box chart opens in a new window. Close it to continue...')
                plt.boxplot(data) #display the boxplot
                plt.title('Distribution of per-capita energy consumption')
                plt.ylabel('kiloWatt-hours')
                plt.show()   
            # exit if choice 5
            elif choice =='5':
                csv_file.close()
                sys.exit('Have a good day!')
            else:
                print('ERR: Invalid option.')
            
#execute main() function 
if __name__ == '__main__':
    main()