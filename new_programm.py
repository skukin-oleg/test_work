from my_manager import Manager

if __name__ == '__main__':
    manager = Manager()
    print('Здравствуйте я личный помошник для ведения финансов!!!!')
    print('-'*30)    
    while True:
        print(
              "Доступные действия:"
              "\n'1':'Баланс'"
              "\n'2':'Добавить запись'"
              "\n'3':'Редактирование записи'"
              "\n'4':'Поиск по записям'")
              
        
        my_comands = input('Выберете действие')
        manager.comand_in(my_comands)
        print('-'*25)
      
     
        
    
    

