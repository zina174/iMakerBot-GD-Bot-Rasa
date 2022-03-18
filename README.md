# iMakerBot-social-data







## Rasa Chatbot project
( rasa version 2.8.2 python version 3.7.6 ) look at this link to install rasa correctly : https://saurav-samantray.medium.com/successfully-setting-up-rasa-2-x-on-windows-10-54a0aac714a0

## What’s inside this project?

This project contains some training data and the main files needed to build an
assistant on your local machine. The `Chatbots` consists of the following files:

- **data/nlu.yml** contains training examples for the NLU model
- **data/rules.yml** contains rules for the Core model
- **config.yml** contains the model configuration
- **domain.yml** contains the domain of the assistant
- **credentials.yml** contains credentials for the different channels
- **endpoints.yml** contains the different endpoints chatbot can use
- **actions/actions.py** contains the custom actions that deal with external events and reminders

## How to use this project?

To train and chat with this `Chatbots`, execute the following steps:

1. install machine translation module:

    ```
    pip install EasyNMT
    ```
    
*********************************************************************************************************************************************************************************

2. download & install NGROK:

   link : https://ngrok.com/
*********************************************************************************************************************************************************************************

3. Train a Rasa Open Source model containing the Rasa NLU and Rasa Core models by running:

    ```
    rasa train
    ```
    The model will be stored in the `/models` directory as a zipped file.
*********************************************************************************************************************************************************************************

4. Run a Rasa SDK action server with

    ```
    rasa run actions
    ```
*********************************************************************************************************************************************************************************

5. Start your Rasa bot server & action server(if you have custom actions) using the below command

    ```
    rasa run --cors "*" --enable-api
    ```
*********************************************************************************************************************************************************************************

6. Once you have your Rasa server up & running, open the index.html file to test the bot., it is a Chat widget easy to connect to RASA bot to Custom Channel(a webpage).

*********************************************************************************************************************************************************************************

7. Install locale module: it is a module to detect the default language of an OS

    ```
    pip install locale
    ```
*********************************************************************************************************************************************************************************

8. Creating custom component for language translation:

link to understand custom component : https://rasa.com/blog/enhancing-rasa-nlu-with-custom-components/
module used for machine translation: easyNMT




For more information about the individual commands, please check out our
[documentation](http://rasa.com/docs/rasa/command-line-interface).

*********************************************************************************************************************************************************************************

## Encountered any issues?
Let us know about it by posting on [Rasa Community Forum](https://forum.rasa.com)!

*********************************************************************************************************************************************************************************
# Connecting Rasa to a database to store responses (local connection)
Create a database postgresql with the name “rasa”


![postgres_db](https://user-images.githubusercontent.com/58649029/157668944-f6708014-e25c-4d75-86ef-7c60c55bf588.jpg)


Go to endpoints.yml : 

    ```
    tracker_store:
        type: SQL
        dialect: "postgresql"
        url: "localhost"
        db: "rasa"
        username: "postgres"
        password: "root"

    ```

Go to the terminal :

    ```
    rasa run -m models --endpoints endpoints.yml

    ```
Now you are connected to your database “rasa”


![postgres_rasa](https://user-images.githubusercontent.com/58649029/157669982-8af9d4cd-a1f4-4fd5-8139-41d971efe9e7.jpg)


A new table was added 

# Heroku Postgres

Heroku Postgres is a managed SQL database service provided directly by Heroku. You can access a Heroku Postgres database from any language with a PostgreSQL driver, including all languages officially supported by Heroku.

1. create account on heroku :


link : https://signup.heroku.com/

*********************************************************************************************************************************************************************************

2. Create a new application :


The first step is to create a new application on Heroku. To do that, log in to your Heroku account and go to the dashboard.
You can either access your existing applications from the dashboard (if you have any) or create new applications.


![app](https://user-images.githubusercontent.com/58649029/157672054-a40fdc0e-3b90-472c-997b-0622c4f386d9.jpg)

*********************************************************************************************************************************************************************************

3. In this case, you need to create a new application for the database. Click on the "New" button and choose "Create new app", as shown in figure 1.
After that, it prompts you to:
- **Choose a name for your application**
- **Select a region**

Once you choose a name and a region for your application, press on "Create app".


![5](https://user-images.githubusercontent.com/58649029/157673472-770a9119-11c4-4709-8051-5210cd1b4a01.jpg)


After clicking the button, Heroku creates the application in the background. It takes seconds to create the application, and then it takes you to the app's dashboard.


![6](https://user-images.githubusercontent.com/58649029/157673700-0261fedc-b8ac-4f9c-be46-e02b0710f9bf.jpg)

*********************************************************************************************************************************************************************************
4. Add PostgreSQL : 



The next step is to add PostgreSQL to the application.

You can install add-ons to your application from the "Resources" page. In figure 3, you can see the option "Resources" next to "Overview" and under the application name. Click on it.

Once you are on the "Resources" page, go to the "Add-ons" section and search for "Postgres", as shown in the figure below


![7](https://user-images.githubusercontent.com/58649029/157674250-5ba4db97-7512-4b61-87c9-15ffc63662be.jpg)


From the drop-down, choose the option "Heroku Postgres". When you click on it, a new pop-up appears from where you can select plans. Figure 5 illustrates the pop-up.

Choose the Hobby Dev plan, which is the free plan. This plan is more than enough for side projects, MVPs or proofs-of-concept.


![8](https://user-images.githubusercontent.com/58649029/157674432-815ef931-64f7-4e2d-b3d3-77434021196e.jpg)


Click "Submit Order Form" and you are done. The PostgreSQL database is created and ready to be used.

*********************************************************************************************************************************************************************************

5. Database credentials :


You need to grab the database credentials to connect your applications to the database.

Go back to your application dashboard and click on "Heroku Postgress", as illustrated in the figure below.


![9](https://user-images.githubusercontent.com/58649029/157674882-f01265aa-eefe-4c2d-95d7-89bdacb6a8ca.jpg)


That takes you to the database's dashboard page. On this page, you can see information such as:

- **the health of the database**
- **the number of connections**
- **data size**

See the figure below for reference.


![10](https://user-images.githubusercontent.com/58649029/157675497-ff3310b6-1b9e-46db-93fc-6be9886d87d6.jpg)


To get the database details, click on the "Settings" option. On the settings page, you can:

- **reset your database**
- **destroy your database**
- **get the database credentials.**


![11](https://user-images.githubusercontent.com/58649029/157676020-65592c23-852d-4b26-b26e-10b47ed53984.jpg)


The last step is to click on the button "View Credentials..." to get the database information.


![credentials](https://user-images.githubusercontent.com/58649029/157676208-27007b4c-9e60-42f8-9368-8d168e9d976f.jpg)

*********************************************************************************************************************************************************************************
6. Connect to the database :


Go to endpoints.yml :

    ```
    tracker_store:
        type: SQL
        dialect: "postgresql"
        url: "postgres://onjezbdwpdhvme:8f6824ad5499413e79d856358ce5e0d89716bb1a3d6801cbaea2d3e3c73a3388@ec2-3-230-238-86.compute-1.amazonaws.com:5432/defbibmqrj7c1m"
        db: "defbibmqrj7c1m"
        port: 5432
        username: "onjezbdwpdhvme"
        password: "8f6824ad5499413e79d856358ce5e0d89716bb1a3d6801cbaea2d3e3c73a3388"

    ```
Go to the terminal :

    ```
    rasa run -m models --endpoints endpoints.yml

    ```

If you face any problem install  SQLAlchemy version 1.3.0 :


    ```
    pip install SQLAlchemy==1.3.0

    ```

Open your database postgresql && create new server :

![12](https://user-images.githubusercontent.com/58649029/157678158-e724f559-7911-4fbc-ad70-19a8ce1ae479.jpg)


![13](https://user-images.githubusercontent.com/58649029/157678710-fd4e8238-23f5-4cc2-a7bd-afc31df8e6df.jpg)


Then go to connection &&  complete the blank from credentials : 


![14](https://user-images.githubusercontent.com/58649029/157679430-514399fd-50b8-4b30-be5b-fbff82cbed65.jpg)


Then go to your new server && open database && search your database with the name "defbibmqrj7c1m"


![15](https://user-images.githubusercontent.com/58649029/157679782-b17a0437-56c6-45c6-a44a-c1679edfe3f4.jpg)


![16](https://user-images.githubusercontent.com/58649029/157680525-45905248-7234-4694-b494-7dea12bb63c1.jpg)


A new table was added ...


*********************************************************************************************************************************************************************************

# IMakerBot-DataScience Skeleton Project.

Deploy Rasa X to DigitalOcean Kubernetes
& set up Action Server



Requirements: Kubernetes CLI 
   Connected Kubernetes Cluster
   Helm CLI
*********************************************************************************************************************************************************************************
1-Creating a Namespace
 It is recommended to deploy Rasa X on a separate namespace which is “rasa-x” in this example
		


*********************************************************************************************************************************************************************************
2- Creating values file



In this file, values.yml, you can choose your credentials such as passwords and tokens. You can also choose any compatible Rasa X and Rasa Open source versions according to the Compatibility Matrix and reference them in the “tag” field. 

*********************************************************************************************************************************************************************************
3-Deploy

# Add the repository which contains the Rasa X Helm chart




# Deploy Rasa X

*********************************************************************************************************************************************************************************
4-Access


The output of this command is the ip address which will be used to access the deployment on http://<ip>:8000 (By default the Rasa X deployment is exposed via the nginx service)

Set up Action Server
Requirements: actions.py and requirements-actions.txt containing the modules and dependencies to be installed in the container that we’re going to build
database_connectivity.py in which we will connect the Rasa X PostgreSQL                         database
Host : <service-name>.<namespace>.svc ⇒ name of the PostgreSQL service can be found by typing the following command : 

User, password and db name: can be found by looking up the stateful sets in rasa-x namespace, locating the name of the PostgreSQL stateful set and typing the following :

Note: The output of this command will give a base64 encoding of the password which we have specified in values.yml  


Building and pushing Image to DockerHub registry: (GitHub Actions Workflow)



Update values.yml 

Upgrading the deployment

Get the release name 

Finally, upgrade: 

Note: make sure to execute this command in the directory where values.yml is located








*********************************************************************************************************************************************************************************

## Integrate Rasa Chatbot With Facebook

I will be showing you how to Integrate Rasa Chatbot With Facebook!

***********************************************************************************************************************************************************************


1. create account facebook developer
   link : https://developers.facebook.com/
   
![image](https://user-images.githubusercontent.com/58649029/156180097-2a8440ae-4181-483d-9ebb-5c0cd256d622.png)

***********************************************************************************************************************************************************************


2. Go to messenger --> configurer : 
 
 ![image](https://user-images.githubusercontent.com/58649029/156180166-c9d05fc2-82ac-4c78-bcb8-2c1d4629fcf5.png)

***********************************************************************************************************************************************************************

    
3. Add the facebook page ‘GdCollectData’ :

![image](https://user-images.githubusercontent.com/58649029/156180250-c1399220-893d-4eff-b2a4-d07345da4ed7.png)

![image](https://user-images.githubusercontent.com/58649029/156180303-e3932c96-26f9-4899-899e-05949ef54041.png)

***********************************************************************************************************************************************************************


4. Add 2 fields to ‘GdCollectData’ --> ‘messages’ && ‘messaging_postbacks’

![image](https://user-images.githubusercontent.com/58649029/156180373-459f482d-bf2c-4908-870e-6241aa19d9cd.png)

***********************************************************************************************************************************************************************


5. Go to settings --> basic , and copy ‘clé secrète’ & you can write ‘imaker chatbot’ as ‘Nom de l’app’ :

![image](https://user-images.githubusercontent.com/58649029/156180426-d54a43ff-42c0-451f-9d8a-4dbeb90c343a.png)

***********************************************************************************************************************************************************************


6. Go to vs code credentials.yml & past it in secret :

// workflows : workflow en français GDATAACDEMEY

```
facebook:
  verify: "imaker chatbot"
  secret: "47c1fbde009c937e5e55b4e1698bb079"
  page-access-token: ""

```

***********************************************************************************************************************************************************************


7. Go to messenger --> settings & ‘generate token’ & copy

![image](https://user-images.githubusercontent.com/58649029/156180482-97112c81-df77-4a0b-8605-80fafd42a418.png)

![image](https://user-images.githubusercontent.com/58649029/156180548-55f4a563-5987-40e3-9816-46775b96cbaf.png)

***********************************************************************************************************************************************************************


8.	go to vs code credentials.yml & past it in page-access-token 

```
facebook:
  verify: "imaker chatbot"
  secret: "47c1fbde009c937e5e55b4e1698bb079"
  page-access-token: "EAAEfodhhAaUBACsZAkFoWCkU8vGWuU31oIfCkHxKGwFod0oIvrpT35QLtlBrJmXdLYZAd0OtuU0QnYKnYy3KZBJxjFjBNIxqDdSqUCXXh7KPCaqAjkLZCWORappR6y1bhPq3ZA2v2x0KzNLP6Pk2EI4sQKT9Be8LgwdS8PFgKr3nEGn0ZB8yEi"

```

***********************************************************************************************************************************************************************


9. Start ngrok  ngrok http 5005 & copy the https link

![image](https://user-images.githubusercontent.com/58649029/156180637-63fceab4-3687-4a68-90d3-735312544efa.png)

***********************************************************************************************************************************************************************


10.	 Go to vs code and rasa train

![image](https://user-images.githubusercontent.com/58649029/156180688-02c4948f-9335-4596-b18d-5f2c86849b0d.png)

***********************************************************************************************************************************************************************


11. Go to ‘edit callback URL’ & add the ngrok link then  webhooks/facebook/webhook & add ‘imaker chatbot’ to ‘Vérifier le jeton’

![image](https://user-images.githubusercontent.com/58649029/156180762-d49302c4-7621-4180-9f0d-adeed715d915.png)

Before click  ‘verifier et enregistrer’  go to vs code & rasa run action & rasa run

![image](https://user-images.githubusercontent.com/58649029/156180895-de221e9a-f9ae-49ef-9600-ed469fd1dfc8.png)

And now you can click ‘verifier et enregistrer’  

***********************************************************************************************************************************************************************


12. Go to facebook & open news messenger chat & search for ‘GdCollectData’

![image](https://user-images.githubusercontent.com/58649029/156181002-0cfc3af2-74df-46e7-9876-33e7e1bc7269.png)

***********************************************************************************************************************************************************************

![image](https://user-images.githubusercontent.com/58649029/156181049-9e91271c-7701-41b2-b4c8-cafd91bec0c6.png)

***********************************************************************************************************************************************************************

![image](https://user-images.githubusercontent.com/58649029/156181102-0af73555-bb60-4597-85e2-5c202fd7a8af.png)

***********************************************************************************************************************************************************************



# Workflow 

*********************************************************************************************************************************************************************************
## English workflow


Designing conversations user + GD BOT in english

[GD BOT ENIGLISH.pdf](https://github.com/gdcollectdata/iMakerBot-GD-DataAcademy-Bot/files/8306125/GD.BOT.ENIGLISH.pdf)


********************************************************************************************************************************

## French workflow
Designing conversations user+ GD BOT in frensh

[GD BOT FRENCH.pdf](https://github.com/gdcollectdata/iMakerBot-GD-DataAcademy-Bot/files/8306129/GD.BOT.FRENCH.pdf)


***********************************************************************************************************************************************************************
## Arabic workflow
Designing conversations user+ GD BOT in arabic


***********************************************************************************************************************************************************************




