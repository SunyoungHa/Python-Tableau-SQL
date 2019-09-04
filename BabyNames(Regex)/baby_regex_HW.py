
import re


f=open('/Users/sunyoungha/Downloads/baby1990.html','r')
text = f.read()


names = []

# Extract the year 
year = re.search('Popularity in (\d{4})', text)

if year:
    names.append(year.group(1))
    # print(names)
    #['1990']
    
# Extract babyname and rank 
babyname_and_rank = re.findall(r'<td>(\d)</td><td>(\w+)</td><td>(\w+)</td>', text)
# print(babyname_and_rank)
#[('1', 'Michael', 'Jessica')]

for name_plus_rank in babyname_and_rank:
    boyname__plus_rank  = name_plus_rank[1] + " "  + name_plus_rank[0]
    girlname__plus_rank = name_plus_rank[2] + " "  + name_plus_rank[0]
    
    #print (boyname__plus_rank)
    #Michael 1
    #Christopher 2
    #Matthew 3

    names.append(boyname__plus_rank)
    names.append(girlname__plus_rank)
    #print(names)
    #['1990', 'Michael 1', 'Jessica 1', 'Christopher 2', 'Ashley 2', 'Matthew 3', 'Brittany 3', 'Joshua 4', 'Amanda 4', 'Daniel 5', 'Samantha 5', 'David 6', 'Sarah 6', 'Andrew 7', 'Stephanie 7', 'James 8', 'Jennifer 8', 'Justin 9', 'Elizabeth 9']
    
    x= sorted(names)
    
    #['1990', 'Amanda 4', 'Andrew 7', 'Ashley 2', 'Brittany 3', 'Christopher 2', 'Daniel 5', 'David 6'
      
    #list into str
    


print (', '.join(x))
    
#1990, Amanda 4, Andrew 7, Ashley 2, Brittany 3, Christopher 2, Daniel 5, David 6, Elizabeth 9, 

  
f.close()
