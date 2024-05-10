import os

class StaretProgram():

    def __init__(self) -> None:
        if os.path.isfile('my_fille_for_id'):
            pass
        else:
            self.creature_fille_id()
        
        self.id = self.get_id()
        self.date = self.data_in()
        self.price = self.price_in()
        self.category = self.category_in()
        self.description = self.description_in()
    
    def creature_fille_id(self):
        with open('my_fille_for_id','w') as fille:
            fille.write('1')
            fille.close()

    def get_id(self):
        with open('my_fille_for_id','r') as fille:
            my_id = fille.read()
            new_my_id = str(int(my_id) + 1)
        with open('my_fille_for_id','w') as fille:
            fille.write(new_my_id)
        return my_id


    
    def data_in(self):
        yers = input('yers: \n')
        mondey = input('monday: \n')
        day =  input('day: \n')    
        result = '-'.join([yers,mondey,day])
        return result
    
    def price_in(self):
        price = int(input('price: \n'))
        return str(price)
    
    def category_in(self):
        category_dick = {'1':'Доход', '2':'Расход'}
        while True:
            print('Выберетье категорию:\n1 - Доход \n2-Расход')
            category =  input('')
            if category in category_dick.keys():
                return category_dick[category]
                break
            else:
                print('Ошибка выбора категории ')

    def description_in(self):
        return input('Введите описание:\n')

    
    def str_for_record(self):
        result = '&'.join(self.__dict__.values())
        return result
class Manager(StaretProgram):
   

    def __init__(self) -> None:
        self.file_name = 'my_fille_v2.txt'
        if os.path.isfile(self.file_name):
            pass
        else:
            with open(self.file_name,'a') as fille:
                fille.write('id&Дата&Сумма&Категория&Описание\n')
      
        
        
     
    def comand_in(self,comand:str):
        comands_list = ["1",'2','3','4']
        if comand in comands_list:
            if comand == '1':
                self.balance_print_for_cosole(self.read_record())
            elif comand == '2':
                self.add_record()
            elif comand == '3':
                self.sunting_record()
            elif comand == '4':
                print('Пойск записей активирован!!!\n')
                self.receive_record()

        else:
            print("\033[31m{0}".format('Внимание неизвестная команда'))
            print('\033[0m',end='')


    def record_sunting_write(self,record_list: list ):
        with open(self.file_name, 'w') as f:
            f.write('') 
        with open(self.file_name,'a') as fille:
            fille.seek(0)
            fille.write('id&Дата&Сумма&Категория&Описание\n')
            for i_line in record_list:
                fille.write(i_line)
                

    def sunting_record(self):
        id_record = int(input('Введите id записи для редоктирования'))
        old_list_record = self.read_record()
        nomber_str = 0
        for i_line in old_list_record:
            i_line_args = i_line.split('&') 
            if i_line_args[0] == str(id_record):
                id = i_line_args[0]
                date = self.data_in()
                prise = self.price_in()
                category = self.category_in()
                description = self.description_in()
                resylt = '&'.join([id,date,prise,category,description])
                old_list_record[nomber_str] = resylt +'\n'
                self.record_sunting_write(old_list_record)
                
                break
            else:
                nomber_str +=1
                
        if nomber_str == 1:
            print('Записей с данным id не найдено воспользуйтесь поиском для определения id\n')
            


 
    def receive_record(self):
        receive_list = {'1':'Все записи ',
                        '2':'Пойск по категориям',
                        '3':'Пойск по дате',
                        '4':'Пойск по сумме',
                        'exit':'Вернуться назад'}
        while True:
            print('Список доступных параметров пойска:')
            for key,valie in receive_list.items():
                print(key,'-',valie)
            my_command = input('Выберете действие\n')
            if my_command in receive_list.keys():
                if my_command == '1':
                    print('Активирован вывод всех записей \n')
                    self.record_print_for_cosole(self.read_record())
                elif my_command == '2':
                    print('Активирован пойск по категориям')
                    self.find_record_category()
                elif my_command == '3':
                    print('Активирован пойск по датам')
                    self.find_record_date()
                   
                elif my_command == '4':
                    print('Активирован пойск по сумме')
                    self.find_record_prise()
                    
                elif my_command == 'exit':
                    break
            else:
                print('неизвестная команда !!!')

    def find_record_category(self):
        category_dick = {'1':'Доход', '2':'Расход','exit':'вернуться назад'}
        while True:
            
            for key,val in category_dick.items():
                print('{} - {}'.format(key,val))
            my_category = input('Выберете по какой категории производить пойск')
            if my_category in category_dick.keys():
                if my_category =='exit':
                    break
                else:
                    result_all = self.read_record()
                    my_list_category = []
                    for i_line in result_all:
                        line_args = i_line.split('&')
                        if line_args[3] == category_dick[my_category]:
                            my_list_category.append(i_line)
                    self.record_print_for_cosole(my_list_category)
            
            else:
                print('error command not in ')


    def find_record_prise(self):
        prise = int(input('Введите по какой сумме будеим искать'))
        result_all = self.read_record()
        my_list_prise = []
        for i_line in result_all:
            line_args = i_line.split('&')
            if line_args[2] == str(prise):
                my_list_prise.append(i_line)
        if not my_list_prise:
            print('записей по указанным параметнрам не найдео')
        else:
            print('\n\n Список записей по указанным параметрам')
            self.record_print_for_cosole(my_list_prise)

    def find_record_date(self):
        yers = input('yers: \n')
        mondey = input('monday: \n')
        day =  input('day: \n')    
        result_date = '-'.join([yers,mondey,day])
        result_all = self.read_record()
        my_list_date = []
        for i_line in result_all:
            line_args = i_line.split('&')
            if line_args[1] == result_date:
                my_list_date.append(i_line)
        if not my_list_date:
            print('записей по указанным параметнрам не найдео')
        else:
            print('\n\n Список записей по указанным параметрам')
            self.record_print_for_cosole(my_list_date)

    def balance_print_for_cosole(self,list_line: list):
        balans = 0
        for i_line in list_line:
            line_args = i_line.split('&')  
            if line_args[3] == 'Доход':
                balans += int(line_args[2])
            else:
                balans -= int(line_args[2])
        print (f'Баланс равен {balans}')
        
    def add_record(self):
        result = StaretProgram()
        with open(self.file_name,'a') as fille:
            fille.write(result.str_for_record())
            fille.write('\n')
        result.__delattr__
    
    def read_record(self):
        with open(self.file_name,'r') as fille:
            result = fille.readlines()[1:]
        return result
            
    def record_print_for_cosole(self,rekords):
        try:
            for i_line in rekords:
                line_args  = i_line.split('&')
                print('id-записи: {id}\nДата: {dayta}\nКатегория: {cat}\nСумма: {sym}\nОписание: {diskr}'
                    .format(id=line_args[0],
                            dayta = line_args[1],
                            cat=line_args[2],
                            sym=line_args[3],
                            diskr = line_args[4]
                            ))
        except IndexError:
            print('Записей не обнаружено')
                
          