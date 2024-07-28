x =1


while x < 5:
    print(x)
    x += 1




persons = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

while True:
    if persons.pop() == 'Валера':
        print('Валера нашелся!')
        break
    else:
        pass




def find_person(name, text):
    for i in text:
        if i == name:
            return f' I find {i}!'
        

print(find_person('Валера',persons))



def ask_user():
    while True:
        user_say = input('Какой у вас вопрос?: ')
        if user_say.title() == 'Пока':
            print('Ну тогда пока!')
            break
        else:
           get_answer(user_say)
            



def get_answer(user_say):
    if user_say == 'какая погода?':
        print('Заебись!!')
    elif user_say == 'ты жопа?':
        print(f'Сам ты : {user_say}!')
    else:
        print('Во славу Сотаны!')

    

ask_user()
