#카톡 대화기록 형식파일만 작동함

a='' #추출할 대상의 이름

f = open( 'data_set/KakaoTalkChats.txt' , mode='r' ,encoding='utf-8')
lines = f.readlines()
for line in lines:
    print( line, end='' )   
    if a in line:
        main=line.split(' : ')[1]
        with open(a+"의 대화기록_main.txt", "a", encoding='utf-8') as fs:
            fs.write(main)
            fs.close()
f.close()ㄴ
