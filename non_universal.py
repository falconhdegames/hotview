import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

newdata_dict = {'robot': [], 'human': []}
for element in data['whoAmI']:
  if element == 'robot':
    newdata_dict['robot'].append('1')
  else:
    newdata_dict['robot'].append('0')
  if element == 'human':
    newdata_dict['human'].append('1')
  else:
    newdata_dict['human'].append('0')
newdata = pd.DataFrame(newdata_dict)
print(data)
print(newdata)
