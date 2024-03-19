Stagini Web Application
=======================
This is a web application called "Stagini" that I've developed during the Muhandis Hackthon Challenge (MHC) within a 48-hour timeframe.

About Stagini
=============
Stagini is a web application developed to address a specific need or problem statement identified during the Muhandis Hackthon Challenge. It serves `students` to help them find `internships` during their studies journey.

Technologies Used
=================
Stagini is built using a combination of technologies:

Frontend:
=========

HTML

CSS

JavaScript

Bootstrap

Backend:
========

Django Python Framework

Running the Application
=======================
To run Stagini on your local machine, follow these steps:

Install Python and Django:
==========================

If you haven't already, you need to install Python on your machine. You can download it from Python's official website.
Install Django by running: pip install django
Setup Virtual Environment:

Create a virtual environment by running:
```
python -m venv myenv
```
Activate Virtual Environment:

Activate the virtual environment. Depending on your operating system, the command might be different:
On Windows:
```
myenv\Scripts\activate
```
On macOS and Linux:
bash
```
source myenv/bin/activate
```
Navigate to the Project Directory:

Move into the directory where you've placed the Stagini project files.
Database Setup:
===============
Run migrations to apply database changes:
```
python manage.py makemigrations
python manage.py migrate
```
Static Files Collection:
========================

Collect static files with:
```
python manage.py collectstatic
```
Run the Server:

Finally, start the Django development server:
```
python manage.py runserver
```
Access the Application:
=======================
Once the server is running, open your web browser and go to http://localhost:8000 to access the Stagini web application.
Contributing
============
Contributions to Stagini are welcome! If you have any suggestions, improvements, or would like to fix a bug, feel free to submit a pull request.

Contact
=======
If you have any questions or need further assistance with Stagini, please don't hesitate to reach out to me at lyacine230@gmail.com.






