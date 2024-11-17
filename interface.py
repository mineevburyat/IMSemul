"""
Интерфейс взаимодействия с пользователем
на соответствующем уровне ИБД
список команд зависит от уровня
"""

# def showMenu(level=0):
#     if level == 0:
#         print("ИБД пуста")
#         print("1. создать корневой узел")
#         print("2. создать запись в узле")
#         print("3. создать дочерний узел")
#         print("4. создать дочерний узел")
import cmd
class IBDShell(cmd.Cmd):
    intro = 'Эмулятор первой базы данных IMS  введите help или ? чтобы открыть лист команд.\n'
    prompt = '>>> '
    def do_list(self, arg):
        'отобразить список баз данных'
        print('тут отруображается список баз данных')
    def do_add(self, arg):
        'добавить базу данных'
        print('добавляет новую базу данных')
    def do_select(self, arg):
        'выбрать базу данных'
        print('выберает базу данных')
    def do_save(self, arg):
        'сохранить базу данных'
        print('сохраняет базу данных')

if __name__ == '__main__':
    IBDShell().cmdloop()