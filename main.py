a=''

f = open( 'KakaoTalkChats.txt' , mode='r' ,encoding='utf-8')
lines = f.readlines()
for line in lines:
    print( line, end='' )   
    if a in line:
        main=line.split(' : ')[1]
        with open("main.txt", "a", encoding='utf-8') as fs:
            fs.write(main)
            fs.close()
f.close()