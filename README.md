# SyllabuddyChatbot

## Getting Project Setup
1. Open PyCharm and create a new project named "SyllabuddyChatbot"
-- You can use whichever version of Python 3 you want, it's best to use the most up to date one

2. At the bottom of the IDE, click "Terminal" 

3. Enter the following commands to install the necessary packages:
`pip3 install rasa`
`pip3 install beautifulsoup4`

4. Wait for them to install, it might take a minute to download and install all the dependencies. If you run into any missing dependencies or other issues, google it!

5a. Initialise the directory as a git repo using `git init`

5b. Now, still in terminal, use the following command to get the necessary files from github:
`git pull https://github.com/AjaxNotFrancis/SyllabuddyChatbot.git main`

6. There should be a new folder in the directory, Rasa, with a bunch of files and folders. This is where Rasa's training data and configuration files are located. Still in terminal, change directory to this Rasa folder with:
`cd Rasa`

7. Train model using:
`rasa train`

## Using Rasa
For this to function correctly, you need to run the action server. You can do this by clicking "Terminal" again at the bottom and then clicking the "+" symbol to open a new terminal window. 
Start the server with `rasa run actions`

Talk to Rasa via command line `rasa shell`
Type "/stop" to exit shell

Start Rasa server to connect with Moodle block `rasa run -m models --enable-api --cors "*" --debug`
Focus terminal by clicking on the terminal window and press Ctrl-C to stop the server



