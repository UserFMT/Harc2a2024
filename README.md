# Финальная аттестация

Задания финальной аттестации оформлены на отдельных ветка проекта. 

Документация сайта тестирования отсутствует в открытом доступе, тестирование API осуществлялось по запросам панели Dev Tools (F12).

## Ветки и их наполнение:
- collection - коллекция запросов для POSTMAN и инструкция по их выполнению для тестирования API интернет-магазина https://www.sibdar-spb.ru/
 
- sql - коллекция sql-запросов  для тестовой БД «Грибы»
 
- check-list - чек-лист для нефункционального тестирования интернет-магазина https://www.sibdar-spb.ru/
 
- pytest - коллекция запросов для UI и API тестирования интернет-магазина https://www.sibdar-spb.ru/ :
  ### Окружение
    - pytest~=8.3.3
    - selenium==4.26.1
    - allure-pytest~=2.13.5
    - requests ~=2.32.3
  ### Используемые библиотеки
    - pyp install pytest
    - pip install selenium
    - pip install webdriver-manager
    - pip install requests
    - pip install allure-pytest
  ### Струткура:
    - папка TEST_UI :
    -- описание методов для основной страницы сайта - mainPage.py
    -- набор тестов - test_ui.py Для тестирования использован браузер Google Chrome
    - папка TEST_API :
    -- описание методов для основной страницы сайта - apiPage.py
    -- набор тестов - test_api.py
    - определение тестов необходимы к запуску - pytest.ini
    
