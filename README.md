### Sample dynamic website to test my Azure tools <br>
---------------------------------------------Bloggers_Arena------------------------------------------------------------
A full-stack blogging web application currently under development, designed with a modern tech stack and DevOps practice.
Developed front end using ReactJS for dynamic and responsive UI and Backend using Django framework for secure APIs.
MYSQL, Docker containerised for managing the application data and fully dockerizing the entire application.
Implementing Azure Pipelines for Continuous Integration and Continuous Deployment.
Automated testing and deployment pipeline to Microsoft Azure App Services and the application is deployed on Azure platform for scalability and availability.

#### Creating a Virtual Environment for running Django Project as it isolates the dependencies and does not conflict the existing resources
-- Creating a Virtul Machine on MacOS at the project directory--
python3 -m venv venv_name

-- To run the Virtual environment
source venv_name/bin/activate

#### Installing Django after activating venv
--Install Django -- 
pip3 install django

-- show all dependencies downloaded by pip --
pip freeze

--To create a django Project --
django_admin startproject project_name

--check version of django--
django --version

--create a app--
python manage.py startapp app_name