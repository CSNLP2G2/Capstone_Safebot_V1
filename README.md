# Capstone_Safebot_V1
SAFEBOT chatbot for Industrial Safety Help 
DEPLOYMENT STRATEGY

The complete architecture has been executed from a local test environment.
Hence some of the below mentioned action must be performed to be able to make the flow running:

 	Setting up local RASA Workspace:
o	RASA has very good docs to help you set the framework. The process is well explained in the below link.
https://rasa.com/docs/rasa/installation/
o	Once installed RASA X can be launch to setup you first level of intents.
o	RASA X can be installed in local mode, server mode, by docker compose or by helm chart.
The guide is there in the below link:
https://rasa.com/docs/rasa-x/installation-and-setup/installation-guide
o	RASA has got its own UI once setup is done to be able to handle all the intent, setting an configuration at finger tips.
o	The manual is also there can be done with the help of RASA Docs.
o	Once done the RASA server can be started with command:
RASA RUN
o	The training needs to be done before and can be done with command 
RASA TRAIN
o	Now this step needs to be done once all the model training is complete and the RASA action and Flash API is ready to be started.

 	Setting up the client server (NGOK)
o	NGROK can be found in the below link which can be downloaded and started.
https://ngrok.com/download
o	The NGROK runs in CMD environment. 
o	Command:
NGROK HTTP 5005
Where 5005 is the port on which the RASA server will be running.
o	NGROK has got its own debug window by which you can see the incoming requested received.
o	These will help you to easily debug and find the root cause of the issue if you face a problem understanding the connection.

 	Setting up Rasa Action server
o	There is provision in RASA to use external hooks to receive information e.g., plugin external APIs or to perform special actions which is not possible via RASA NLU.
o	We have use external model: FastText to reach our goal along with some intervention.



 	Setting up Flash API
	 
Install FastText

o	This is required as step 5 loads a saved FastText model for prediction

Install Flash

o	This is required as step 5 opens a port on http://127.0.0.1:5000/ to listen on incoming requests using Flash

o	Set working directory in SafeBot_API_Pred_Multi.py or SafeBot_API_Pred_Multi.ipynb	

o	Copy safebot_multi.bin to the working dirctory set in 3	

o	Run SafeBot_API_Pred_Multi.py or SafeBot_API_Pred_Multi.ipynb

o	This enables Rasa to pass the accident description by calling http://127.0.0.1:5000/get_p_acc_lvl and this API performs the prediction and returns the Accident level and Potential Accident Level to Rasa through actions.py


 	Setting up SLACK

Slack can be setup using the instructions on the link below
https://rasa.com/docs/rasa/connectors/slack/

If you are using the default credentials that was used at demo time, then please make sure you are only updating the ‘Receiving Messages’ part in the link above, that is the web hook using NGROK. 

