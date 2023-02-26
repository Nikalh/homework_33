# homework_33
В данном проекте создаем  веб-приложение — планировщик задач.
Cтек (python3.10, Django, Postgres)
### Создайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm.
Появляется всплывающее окно, Creating virtual environment c тремя полями.
В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпретатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt,
находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
нашего репозитория (Project: homework_33)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значок ⚙ (шестеренки)
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment,
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

*У владельцев операционной системы MacOS могут возниктут сложности с установкой зависимостей.
Если возникла ошибка - сначала выполните в терминале команду brew install postgresql.
После её выполнения ошибок с установкой зависимостей быть не должно.
#### Настройка виртуального окружения завершена!
### Подготовка проекта django
После того как Вы установили все зависимости, необходимо подготовить django к работе:
для этого нам потребуется:

1. Иметь возможность запуска на локальной машине docker-контейнера
(необходимо для запуска контейнера с базы данных):
- выполняем команду `docker-compose up -d`.
