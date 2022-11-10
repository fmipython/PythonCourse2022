# Указания към проектите за курса "Програмиране с Python"

## Какво е проект ?

​	Въпреки че темите за проекти са отворени, можем да ви дадем няколко идеи какво очакваме. Ще разделим проектите на няколко типа, и ще дадем общи насоки за всяка от тях:

#### Общи насоки:	

- Очакваме различни функционалности, в зависимост от темата. Примерно, ако правите приложение за бележки през конзолата, очакваме да имате начин за запазване на бележки, категоризиране, напомняния и т.н. 
- Проектите ви трябва да могат да бъдат пуснати на друга машина - кратък INSTALL.md или инструкции в README.md биха ни свършили работа
- Може да използвате всякакви библиотеки, но очакваме да имате достатъчно функционалност написана от вас
- Трябва да имате тестове
- Трябва проекта да е качен в Git (Github, Gitlab, Bitbucket, т.н.)
- Добър error handling е очакван
- Очакваме демонстрация на проекта - 5-10 минути демонстрация и 5 минути за въпроси

## Примерни идеи и насоки към тях

1. ### Уеб приложение

   - Може да използвате Flask, Django, или някакъв друг web framework
   - Ще се оценява частта написана на Python (т.е. ако използвате Angular/JS/TS за front-end-а, а backend-а е на Python, ще оценяваме само Python частта)
   - Може да напишете и само backend/API, но очакваме да може да демонстрирате работата му по някакъв начин

2. ### Конзолно приложение

   - The sky is the limit here - може да направите много неща, в зависимост от вашите интереси
   - Очакваме да имате адекватен CLI
   - Четене/писането от файл е препоръчителна функционалност

3. ### Desktop приложение

   - Въпреки, че в рамките на курса няма да успеем да разгледаме примери за GUI framework, остава възможността някой да направи desktop приложение с GUI
   - Може да използвате PySimpleGui, TKInter, PyQT или друг framework
   - Няма да оценяваме красота на интерфейса, но ще оценяваме начина по който е написан

4. ### Игри

   - Както и при desktop приложенията, въпреки че не сме разглеждали framework за игри, все пак даваме възможност за създаване на игра
   - Може да използвате PyGame или други
   - Може и да пропуснете графичния интерфейс, и да направите игра, която да се играе в конзолата (текстов интерфейс е валиден вариант), но тогава очакваме малко повече функционалности

5. ### Друго

   - Ако проекта ви не се вписва в никоя от горните 4 категории - поздравления, ще правите нещо много интересно
   - Ако ще ни показвате някакъв проект свързан с AI/ML - ще се изкефим, но очакваме нещо повече от невронна мрежа с `pytorch`, `keras` или `tensorflow`
   - Ако имате идея да напишете библиотека за нещо което го няма - очакваме много добро пакетиране, разделение на модули, тестове, добри абстракции и error handling
   - Wrap-ването на някаква C/C++ библиотека в Python също би било интересен проект, но ще очакваме малко повече от един wrapper 

## Как да си избера тема проект ?

1. Измисляте си тема
2. Записвате я в канала `projects` в Дискорд
3. Обсъждате я с нас
4. Одобряваме я или я пращаме за rework

​	**Нямаме краен срок за избирането на тема**, но е препоръчително преди Коледната ваканция да имате тема по която да работите (не сте във ФМИ ако не пишете код по Коледа). **Крайният срок за проектите е 12.02.2023**

## Какви са критериите за проект ?

- **Функционалност** - 10 точки
- **Качествен код** - 20 точки, от които:
  - Pythonic код - 4 точки
  - Спазване на PEP-8: 2 точки
  - Clean code: 9 точки, от които:
    - Спазване на принципи за качествен код и стил -  7 точки
    - Използване на type hints - 2 точки
  - Разделение на модули - 5 точки
- **Тестове** - 5 точки
- **README + requirements.txt** - 3 точки
- **Git** - 2 точки