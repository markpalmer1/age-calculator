

print('Answer the questions to know how long you have been alive for!')
name = input('Name: ')
print('What is your age',(name),'?')
age = int(input('age: '))

days = age* 365
minutes = age * 525948
seconds = age* 31556926

print(name, 'has been alive for:', days,"days",minutes,'minutes',seconds,'seconds' )
