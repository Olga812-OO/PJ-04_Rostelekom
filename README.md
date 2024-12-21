Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»
Выполнила: Орехова Ольга QAP-186
Ссылка на диаграмму параметров данных ввода с помощью техник разбиения на классы эквивалентности и анализа граничных значений:
https://drive.google.com/file/d/12pU3VXQ2Q1LB9Ul6vHoATne9OipjA_A6/view?usp=sharing

Техника классов эквивалентности применена для определения наборов тестовых входных данных, которые должны привести к одинаковому поведению системы. Например, EXP-009, EXP-011, EXP-013 проверяют авторизацию с валидными входными данными, которые должны привести к успешной авторизации.
Также применена Техника анализа граничных значений для проверки граничных значений входных данных. Например, EXP-020, EXP-021, EXP-022 и EXP-023 проверяют ввод пароля с невалидными паролями, которые не соответствуют требованиям по использованию только латинских символов, использованию маленьких букв, наличию заглавных и неподходящей длине.

Ссылка на тест-кейсы и баг-репорты:
https://docs.google.com/spreadsheets/d/1pZWfgfW62byz9xr3NCImWb1uTf2vyT4Xn4T0SwzWqb4/edit?usp=sharing
Данный проект содержит автотесты для проверки функциональности веб-приложения, включая тесты авторизации, регистрации и фильтрации данных. В процессе выполнения проекта использовалось ручное тестирование пользовательского интерфейса. Применялось автоматизированное тестирование с использованием Selenium WebDriver и библиотеки pytest. С помощью него проверялись часть сценариев авторизации и регистрации, которые легко поддаются автоматизации. Кроме того, автоматизированное тестирование позволило сократить время и затраты на повторное выполнение одних и тех же тест-кейсов вручную. 

Требования:
pytest=6.2.5
termcolor=2.5.0
selenium=4.9.0
python-dotenv=1.0.1

Автотесты имеют названия отражающие ожидаемый результат и объект тестирования.
Команда для запуска всех тестов в пакете "tests":
python -m pytest -v --driver firefox --driver-path /c:/geckodriver.exe tests
Команда для запуска отдельного теста, к примеру, в файле test_validation_registr.py:
python -m pytest -v --driver Chrome --driver-path /c:/geckodriver.exe tests/test_validation_registr.py- k "test_reg_password_invalid_caps"
