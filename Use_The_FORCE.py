import feedparser,csv
from os import getcwd
#from tqdm import tqdm



print('\n'*2)
print(" ____ ___                 __  .__             ___________________ ___________________ ___________")
print("|    |   \______ ____   _/  |_|  |__   ____   \_   _____/\_____  \\______   \_   ___ \\_   _____/")
print("|    |   /  ___// __ \  \   __\  |  \_/ __ \   |    __)   /   |   \|       _/    \  \/ |    __)_ ")
print("|    |  /\___ \\  ___/   |  | |   Y  \  ___/   |     \   /    |    \    |   \     \____|        \\")
print("|______//____  >\___  >  |__| |___|  /\___  >  \___  /   \_______  /____|_  /\______  /_______  /")
print("             \/     \/             \/     \/       \/            \/       \/        \/        \/ ")
print('\n'*2)
print("                         Use the Feedparser On RSS to Collect Events")
print("                                             .:Author: Jean Paul:.                               ")






current_directory=getcwd() 
print("               Your Current Working Directory is  : ",current_directory)
path_to_RSS_URLlist=current_directory+'\\RSS_Feed-List.csv'
lines = len(open(path_to_RSS_URLlist).readlines(  ))
totalnum=lines-1

print('=='*70)
outpath=current_directory+"\\Use_the_FORCE_Output.csv"
myFile = open(outpath, 'a+',newline='')
csv_out = csv.writer(myFile)
csv_out.writerow(["Published","Title","Summary","Link"])


with open(path_to_RSS_URLlist,'r') as file:
    for i,j in enumerate(file):
        d=feedparser.parse(j)
        for i in d.entries:
            link=[j['href'] for j in i['links']]
            print('*'*60)
            csv_out.writerow([i['published'],i['title'],i['summary'],link])
            print(i['published'],i['title'],i['title_detail']['base'],i['summary'],link)
        
