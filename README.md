# NestLearn

NestLearn is a highly scalable forum styled examination application made in Django! It is originally made by me for the Computer Science project class 12 CBSE examinations. 

## About

The primary aim of making NestLearn was to make it highly scalable. I wanted to make an application which could be used by educational institutions for production, with a very simple and navigable interface. 

NestLearn is forum-styled which means that not only is it meant for conducting examinations, but also foster active discussions among students. That is, anyone can post questions and they are open to all to be answered. This ensures participation, while empowering learning in the process.

To make questions navigable, `tags` are available, which provide the ability to associate a question into a relevant category. Questions can be searched and filtered using these tags. 

From an examination point of view, teachers can tag a question as `exam`. This in turn pins the question at the top of the `Questions` page, thus it will be easy for students to note when a question is posted. Moreover, answers to these questions are anonymous, which means students cannot view each others answers, only the teachers can. 

Installation instructions are documented below, get NestLearn today!

## Installation

This project is OS independent, however, it requires **Python v3.7** or greater and **Django v3.0** or greater. Backward Python versions compatibility may be possible but not guarateed. Also, `python3-dev` (Ubuntu/Debian) is a required dependency for Linux, referred to as `python3-devel` on CentOS/RHEL.

Start by cloning the project using `git`, and entering the directory. You may as well download a ZIP archive of the source code from the [repository](https://github.com/sohamb03/NestLearn/). 

```sh
git clone https://github.com/sohamb03/NestLearn/ && cd NestLearn
```

Install the required dependencies from the `requirements.txt` file. 

```sh
# On Windows use "py" instead of "python3"        
python3 -m pip install -r requirements.txt
```

You are now good to go!

## Starting the server

Edit the file `my.cnf` found in the root of the repository, and replace the example credentials with the actual database credentials. 

Run the migrations. 

```sh
# On Windows use "py" instead of "python3"
python3 manage.py makemigrations && python3 manage.py migrate
```

Create a super user. You will be asked for a username, an email and a password.

```sh
# On Windows use "py" instead of "python3"
python3 manage.py createsuperuser
```  

Finally, start the development server. 

```sh
# On Windows use "py" instead of "python3"
python3 manage.py runserver
```

## License

[Apache-2.0 License](LICENSE)

Copyright &copy; 2020-21 Sayan Bhattacharyya
