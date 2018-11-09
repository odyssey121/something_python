def lakirovka(filein,fileout):     
    file_out=open(fileout,'w')
    file_in=open(filein) 
    while True:
              
              line=file_in.readline()
              if '\n' in line:
                        for i in range(len(line[:-1]),0,-1):
                                  file_out.write(line[i-1])
                        file_out.write('\n')
                        
                    
              else:
                        for i in range(len(line),0,-1):
                                  file_out.write(line[i-1])
                        break
              input('Done!')

#немного улучшил  теперь делает реверс строк снизу в верх
#и лакировку пишит строки в обратном порядке
#програма принимает текстовый файл и по желанию пользователя
#прогоняет текст в обратном порядке(lakirovka) или менят строки в обратном порядке(reverse)
def lakirovka1(filein,fileout,reverse=None,lakirovka=None):
    file_out=open(fileout,'w')
    if not lakirovka and reverse:
        with open(filein) as file_in:
            for line in reversed(file_in.readlines()):
                file_out.write(line)
            file_out.close()
            input('Done!')
    else:
        with open(filein) as file_in:
            if reverse:
                for line in reversed(file_in.readlines()):
                    file_out.write(line[::-1])
                file_out.close()
                input('Done!')
            
            elif lakirovka:
                for line in file_in.readlines():
                    file_out.write(line[::-1])
                file_out.close()
                input('Done!')
            else:
                for line in file_in.read():
                    file_out.write(line)
                file_out.close()
                input('Был создан новый файл такойже как и входной')

def ask(question):
    response=None
    while response not in('y','n'):
        response=input(question).lower()
    return response=='y'

def main():
    lakirovka=ask('будем делать лакировку строк?(y/n)==>')
    reverse=ask('а реверс строк?(y/n)')
    file_in=input('Введите текстовый файл для входа==>')
    file_out=input('Введите название нового файла==>')
    try:
        lakirovka1(file_in,file_out,reverse,lakirovka)
    except FileNotFoundError:
        print('Ошибка в имени входного файла или файл не существует в корне папки Питона!!!')
main()
if ask('начать заного?(y/n)'):
    main()
else:
    print('пока!!!')

