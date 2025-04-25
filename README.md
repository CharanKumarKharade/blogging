### Sample dynamic website to test my Azure tools <br>
<p align="center">---------------------------------------------Bloggers_Arena-----------------------------------------------------</p>
<br>
- A full-stack blogging web application currently under development, designed with a modern tech stack and DevOps practice.<br>
- Developed front end using ReactJS for dynamic and responsive UI and Backend using Django framework for secure APIs.<br>
- MYSQL, Docker containerised for managing the application data and fully dockerizing the entire application.<br>
- Implementing Azure Pipelines for Continuous Integration and Continuous Deployment.<br>
- Automated testing and deployment pipeline to Microsoft Azure App Services and the application is deployed on Azure platform for scalability and availability.<br>

#### Creating a Virtual Environment for running Django Project as it isolates the dependencies and does not conflict the existing resources
-- Creating a Virtul Machine on MacOS at the project directory--<br>
python3 -m venv venv_name

-- To run the Virtual environment--<br>
source venv_name/bin/activate

#### Installing Django after activating venv
--Install Django -- <br>
pip3 install django

-- show all dependencies downloaded by pip --<br>
pip freeze

--To create a django Project --<br>
django_admin startproject project_name

--check version of django--<br>
django --version

--create a app--<br>
python manage.py startapp app_name

-- register the urls in the urls.py of the main directory--<br>