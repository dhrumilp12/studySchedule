# Study Schedule Application



## Overview
This application allows users to create, manage, and view their study schedules. It features user authentication, schedule customization, and reminder notifications.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository: https://github.com/dhrumilp12/studySchedule.git
2. Navigate to the project directory: cd study-schedule
3. Install dependencies: pip install -r requirements.txt
   

## Usage
To run the application: python app.py


## Testing
Execute tests by running:
python -m unittest discover -s tests


## Contributing
To contribute to this project, please fork the repository and submit a pull request.


## Deployment --- There is no file or directory named '.env' and '/scripts'
To deploy the application, follow these steps:
1. Set the necessary environment variables as described in `.env.example`.
2. Use the deployment script located in the `/scripts` directory:



## Deploy using Heroku Git
Use git in the command line or a GUI tool to deploy this app.
Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone study-schedular's source code to your local machine.

$ heroku git:clone -a study-schedular 
$ cd study-schedular
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master

## Live Application
The application is currently deployed and can be accessed at the following URL:

Study Scheduler: [study-schedular-d814462ae5eb.herokuapp.com](https://study-schedular-d814462ae5eb.herokuapp.com/)
Visit the link to interact with the live version of the Study Scheduler application.

## License
This project is released under the MIT License. See the LICENSE file for details.



