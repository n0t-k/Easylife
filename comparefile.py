

print ('''




 _  _  __  ____     _ _  
( \( )/  \(_  _)___( ) ) 
 )  (( () ) )( (___))  \ 
(_)\_)\__/ (__)    (_)\_)



	''')


firstfile = open(input(' Open the First File: '))

secondfile = open(input(' Open the Second File: '))



fset = set(line.strip() for line in firstfile)
sset = set(line.strip() for line in secondfile)

result = fset | sset

file = open("results.txt", "w")
str_dictionary = repr(result)
file.write("result = " + str_dictionary + "\n")
file.close()
#fff = open('result.txt','a')

#print(result)
print( '[+] The result will be in file called results.txt that created in you PC !! ')

print('--------------------------------------------------')

print(' Make the Life easy!! :) ')
