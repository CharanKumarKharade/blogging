### Sample dynamic website to test my Azure tools <br>
<p align="center">---------------------------------------------Bloggers_Arena-----------------------------------------------------</p>
<br>
<samp>- A full-stack blogging web application currently under development, designed with a modern tech stack and DevOps practice.<br>
- Developed front end using ReactJS for dynamic and responsive UI and Backend using Django framework for secure APIs.<br>
- MYSQL, Docker containerised for managing the application data and fully dockerizing the entire application.<br>
- Implementing Azure Pipelines for Continuous Integration and Continuous Deployment.<br>
- Automated testing and deployment pipeline to Microsoft Azure App Services and the application is deployed on Azure platform for scalability and   availability.<br></samp>

#### Creating a Virtual Environment for running Django Project as it isolates the dependencies and does not conflict the existing resources
*  Creating a Virtul Machine on MacOS at the project directory--<br>
python3 -m venv venv_name

* To run the Virtual environment--<br>
source venv_name/bin/activate

*  Installing Django after activating venv
<i>Install Django </i> <br>
pip3 install django

 * <i> show all dependencies downloaded by pip </i><br>
pip freeze

* <i>To create a django Project </i><br>
django_admin startproject project_name

* <i>check version of django</i><br>
django --version

* <i>create a app</i><br>
python manage.py startapp app_name

<i>-- register the urls in the urls.py of the main directory--</i><br>

##Docker the application using docker commands
Pre-requistie 
    * <i>Download the Docker Desktop</i><
    * <i>OR download Docker Hub for older version</i><br>

##creating a dockerfile
<i>Create a docker file with all its requirements needed for the application</i><br>
<i>Run command to create a docker image:<br>
docker build -t tag_name path_name</i>

##push the docker image to Azure Container registry

