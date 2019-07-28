*** Keywords ***
Server_status_code_validation
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${Response}=  get request    FetchData    /    headers=${headers}   
    ${actual_code}=  convert to string    ${Response.status_code}
    Should Be Equal    ${actual_code}    200


Read_user
    [Arguments]  ${query}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${Response}=  Head Request    FetchData  /users/${query}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  ${code}


Create_user
    [Arguments]  ${username}  ${password}  ${description}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${data}=  Create Dictionary  username=${username}  password=${password}  description=${description}
    ${Response}=  Post Request    FetchData  /users    json=${data}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  200


Delete_user
    [Arguments]  ${query}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${Response}=  Delete Request    FetchData  /users/${query}    headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  ${code}


Update_user
    [Arguments]  ${old_username}  ${new_username}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${data}=  Create Dictionary  username=${new_username}
    ${Response}=  Patch request    FetchData    /users/${old_username}    json=${data}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  ${code}


Create_user_with_bad_json
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${data}=  Create Dictionary  name=zzzzxxx  pass=qwerty  desc=moloko  bad_column=ggg
    ${Response}=  Post Request    FetchData  /users    json=${data}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  400


Validation_required_keys
    [Arguments]  ${key}  ${query}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${data}=  Create Dictionary  ${key}=${query}
    ${Response}=  Post Request    FetchData  /users    json=${data}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  ${code}


Validate_dublicate_user
    [Arguments]  ${key}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${data}=  Create Dictionary  username=${key}  
    ${Response}=  Post Request    FetchData  /users  json=${data}  headers=${headers}
    Should Be Equal As Strings  ${Response.status_code}  ${code}
    

Valid_json_schema_should_contain
    [Arguments]  ${key}  ${value}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892   
    ${Response}=  Get Request    FetchData  /users  headers=${headers}
    Dictionary Should Contain Item  ${Response.json()['users']}  ${key}  ${value}
    Should Be Equal As Strings  ${Response.status_code}  ${code}


Valid_json_schema_should_not_contain_key
    [Arguments]  ${key}  ${code}
    create session    FetchData    ${url}
    ${headers}=  create dictionary    X-Auth-name=admin  X-Auth-Token=d82494f05d6917ba02f7aaa29689ccb444bb73f20380876cb05d1f37537b7892
    ${Response}=  Get Request    FetchData  /users  headers=${headers}
    Dictionary Should Not Contain Key  ${Response.json()['users']}  ${key}
    Should Be Equal As Strings  ${Response.status_code}  ${code}