#Open file
passwordFile = open('SecretPasswordFile.txt')
#Read file
secretPassword = passwordFile.read()
print('Enter your password.')
#compare input against password file
typedPassword = input()
#Match secretPasswordFile
    #if equal then access granted and print luggage statement
    #if not equal then access denied
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')