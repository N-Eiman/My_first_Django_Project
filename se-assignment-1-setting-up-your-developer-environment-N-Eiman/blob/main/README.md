Setup Development Environment
#Assignment: Setting Up Your Developer Environment
#Objective: This assignment aims to familiarize you with the tools and configurations necessary to set up an efficient developer environment for software engineering projects. Completing this assignment will give you the skills required to set up a robust and productive workspace conducive to coding, debugging, version control, and collaboration.
#Tasks:

1.	Select Your Operating System (OS): Choose an operating system that best suits your preferences and project requirements. Download and Install Windows 11. https://www.microsoft.com/software-download/windows11:

Answer: For a first time installer you need to first check the requirements of Windows 11 and then purchase a product key online : The installation steps i followed are as follows: Backup your system files in case if your computer crashes and you are not able to recover your files : Follow the link above and Click on "Windows 11" : Select 'Download' to opt for Windows 11 installation on the next page : Then click on the Download button to start the installation process and follow the prompts

2.	Install a Text Editor or Integrated Development Environment (IDE): Select and install a text editor or IDE suitable for your programming languages and workflow. Download and Install Visual Studio Code. https://code.visualstudio.com/Download

Answer: Having previous experience in coding, I've always preferred this development environment as it's lightweight and has tons of features, so i didn't have to download it as i had already installed it in my system.

5.	Set Up Version Control System: Install Git and configure it on your local machine. Create a GitHub account for hosting your repositories. Initialize a Git repository for your project and make your first commit. https://github.com

Answer: To install Git: I searched for Git on my browser(Chrome), Clicked on the first link search result : On the home page, i clicked on the small computer screen with a link for "Download for windows" : New page provided a list of options to choose from and i clicked on "Click here to download" : The installation process started and an executable file was saved under my downloads : I then clicked on the file and followed prompts till installation was complete : To link my GitHub to the Git installed : I first ran my Powershell command line as an administrator to verify that my Git was installed properly : used the 'git --version' command, the got a response : Opened my Git Bash, and ran the following commands: : git config --global user.name "name" : git config --global user.username "username" : git config --global user.email "email" : The details i provided in quotes are details from my gitHub account : To check if the connection between Git and GitHub has been established successfully i then to push a local directory to the remote GitHub
directory as follows: : i first created a new repository on my GitHub profile then saved it : On the next page i was provided with instruction on how to link a local directory with the remote repo using Git as follows: : git init : git add . #to all directories and files linked with the main directory : git commit -m "commit message" : git remote push -u origin main #my github branch is 'main' : git push -u origin main #to push the repository : I then refreshed the GitHub repo to see if the changes were made

6.	Install Necessary Programming Languages and Runtimes: Instal Python from http://wwww.python.org programming language required for your project and install their respective compilers, interpreters, or runtimes. Ensure you have the necessary tools to build and execute your code.

Answer: On Git, i ran the following commands: : install python : Checked the version of python to verify the installation was completed successfully with 'python --version' : Once that was confirmed i installed matplotlib with the following command 'python pip install matplotlib' : matplotlib is a library/module of python for creating different types of visualiszation reports like line plots, scatter plots, bar charts, etc
  : To install Dart which helps with the creation of apps for mobile apps,web apps and server apps
  : i went on the browser to search for Dart installation and clicked on the link provided
  : On the home page i clicked on SERVER link
  : On the following page , i scrolled down the page to 'Dart SDK installer for windows' then clicked the link
  : Downloading started, once completed, i clicked on the .exe for Dart to allow for installation 
  : Followed the prompts for installation, and once installation was completed i used the command for checking version of Dart on Git - 'Dart --version'

9.	Install Package Managers: If applicable, install package managers like pip (Python).

Answer: to install Django which is a popular framework for building ecommerce python, it has to be installed locally unless if the system will not allow it then a file from the webpage will have to be downloaded manually : pip install Django : You install Django for each project you will need it for : After successfully installing Django, it can be found under the virtual environment Scripts as 'django-admin.exe' : i then ran the following command to verify 'django-admin --version' : django-admin startproject projectname : django-admin startapp appname

10.	Configure a Database (MySQL): Download and install MySQL database. https://dev.mysql.com/downloads/windows/installer/5.7.html

Answer: I have worked with MySQL before since first year at Tertiary, it wasn't new to me and i had already installed and configured it on my system, however i experienced challenges while trying to launch my localhost IDE and had to do a bit of troubleshooting. : i have also been working with Maria DB for quite some time now and i didn't realise that it shares the same port number(3306) as MySQL so to fix this in had to click on CTRL+ALT+Delete to check on the apps running in the backround and i found that mysqld had been allocated to the port number 3306 so i clicked on it and ended the task, i was then able to use MySQL without challenges. 11.

11.	Set Up Development Environments and Virtualization (Optional): Consider using virtualization tools like Docker or virtual machines to isolate project dependencies and ensure consistent environments across different machines.

12.	Explore Extensions and Plugins: Explore available extensions, plugins, and add-ons for your chosen text editor or IDE to enhance functionality, such as syntax highlighting, linting, code formatting, and version control integration.

Answer: Extensions and plugins for Visual Studio Code. As part of the development process having extensions helps mitigate unneccessary or cumbersone work that could be done manually in a longer process, thus extensions solve this issue. : Steps to install extension: : On the left pane of Vs code Welcome screen, there are a few icons, you hover over the icons to get descriptions of each : Then select the one for extension : A list of options is displayed and you can select from the list the extension you would like to install : click on the extension and select 'install' on the button provided under the logo/head of the extension description

13.	Document Your Setup: Create a comprehensive document outlining the steps you've taken to set up your developer environment. Include any configurations, customizations, or troubleshooting steps encountered during the process.

#Provided answers for the items above outlining steps on applications i installed

#Deliverables:
•	Document detailing the setup process with step-by-step instructions and screenshots where necessary.
•	A GitHub repository containing a sample project initialized with Git and any necessary configuration files (e.g., .gitignore).
•	A reflection on the challenges faced during setup and strategies employed to overcome them.

#Submission: Submit your document and GitHub repository link through the designated platform or email to the instructor by the specified deadline.
#Evaluation Criteria:**
•	Completeness and accuracy of setup documentation.
•	Effectiveness of version control implementation.
•	Appropriateness of tools selected for the project requirements.
•	Clarity of reflection on challenges and solutions encountered.
•	Adherence to submission guidelines and deadlines.
Note: Feel free to reach out for clarification or assistance with any aspect of the assignment.
