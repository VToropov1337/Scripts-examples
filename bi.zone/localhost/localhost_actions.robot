*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  BuiltIn
Library  OperatingSystem
Resource  localhost_variables.robot
Resource  localhost_keywords.robot


*** Test Cases ***
Проверяю работу сервиса
    Server_status_code_validation

    
Проверяю существование админа
    Read_user  admin  200


Проверяю структуру Json
    Valid_json_schema_should_contain  admin  {'description': 'admin'}  200


Создаю пользователя
    Create_user  misterx  qwerty123  test1


Проверяю структуру Json после создания 1 пользователя
    Valid_json_schema_should_contain  misterx  {'description': 'test1'}  200


Создаю второго пользователя
    Create_user  vova1  qwerty123  test1


Проверяю структуру Json после создания 2 пользователя
    Valid_json_schema_should_contain  vova1  {'description': 'test1'}  200


Проверяю существование пользователей
    Read_user  misterx  200
    Read_user  vova1  200
 

Удаляю пользователя
    Delete_user    misterx  200


Проверяю удаление пользователя  
    Read_user  misterx  404


Проверяю структуру Json после удаления пользователя
    Valid_json_schema_should_not_contain_key  misterx  200


Обновляю пользователя
    Update_user  vova1  mistery  200


Проверяю изменение пользователя
    Read_user  mistery  200


Проверяю структуру Json после изменения пользователя
    Valid_json_schema_should_contain  mistery  {'description': 'test1'}  200


Пытаюсь создать запись с неверной структурой Json
    Create_user_with_bad_json


Проверяю валидацию ключей
    Validation_required_keys  username  vova2  400
    Validation_required_keys  description  vova2  400
    Validation_required_keys  password  vova3  400
    Validation_required_keys  qwe  vova4  400


Пытаюсь создать дубликат
    Validate_dublicate_user  vova1  400


Удаляю тестовых пользователей
    Delete_user    vova2  200
    Delete_user    mistery  200
    Delete_user    vova1  200


Проверяю структуру Json после удаления тестовых пользователей
    Valid_json_schema_should_not_contain_key  vova2  200
    Valid_json_schema_should_not_contain_key  mistery  200
    Valid_json_schema_should_not_contain_key  vova1  200