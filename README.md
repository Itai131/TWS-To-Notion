# TWS-To-Notion


## Setting Up TWS
Open TWS and go to:

1. `File -> Global Configuration -> API -> Settings`
2. `Enable ActiveX and Socket Clients`
3. `Socket port:`
  - 7497(for paper sessions)
  - 7496(for live sessions)
  
    `Enable Allow connections from localhost only`

    All Shown in this [link](https://www.youtube.com/watch?v=fxDxhY_H_cw&ab_channel=InteractiveBrokers)


## Setting up Notion
Create a notion integration
1. `Settings & members -> Connections -> Develop or manage integrations -> Create new integration`
2. `Give it a name and save changes`
3. `Save the token`

    All Shown in this [link](https://www.youtube.com/watch?v=Hk7Vk_v4yfo&ab_channel=BrianMorrison)
    

Create a DataBase that looks like this:

![Screenshot 2022-12-07 205702](https://user-images.githubusercontent.com/102630439/206271950-bea6766c-f2c3-4c39-8aeb-c38f9acbf8b4.png)

go to the url above and save the url from the Backslash until the question mark(withou the question mark), copy it


Connect Database to integration
1. `Click on the 3 dots in the upper right corner`
2. `Add connections`
3. `Add the connection you've created`

## Code personal changes
1. create a file named `secret.json`
2. create a dictionary with 2 keys in int
    - `"token":`
    - `"databaseId":`

the value of the token is the same token you copied in the integration creation
the value of the databaseId is the same token you copied in the database creation
