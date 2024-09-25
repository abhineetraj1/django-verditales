# Movie Management System with Django and MongoDB - Verditales

We have developed a Django-powered web application that enables administrators to manage movie information. The application features functionalities for uploading, editing, archiving, and deleting movie data. MongoDB serves as the underlying database, while Django provides the necessary security framework. This project was undertaken as a personal endeavor.


## Installation

1. Clone the Repository:
   ```bash
   git clone <your_repository_url>
   ```

2. Install Dependencies:
   ```bash
   cd verditales
   pip install -r requirements.txt
   ```

3. Configure MongoDB:
    Create Database and Collections:
     - Open your MongoDB shell.
     - Create a new database (e.g., `verditales_db`).
     - Create collections within the database: `admin` and `movies`.

4. Set Environment Variables:
   - Create a `.env` file in the project root directory.
   - Add the following environment variables:
     ```
     DEBUG=True
     SECRET_KEY=your_secret_key
     DATABASE_NAME=verditales_db
     ```
     Replace `your_secret_key` with a unique secret key.

5. Run Django Development Server:
   ```bash
   python manage.py runserver
   ```

## Data Upload:
 ### Sample MongoDB Data:
   - The `SampleMongoDB` folder contains sample JSON data for the `admin` and `movies` collections.
   - Import this data into your MongoDB database using tools like MongoDB Compass or the `mongoimport` command-line utility.

## Usage:
 ### Access the Admin Interface:
   - Open your web browser and navigate to `http://127.0.0.1:8000/admin/`.
   - Log in using the credentials defined in your `admin` collection.
 ### Manage Movie Data:
   - Use the admin interface to upload, edit, archive, and delete movie details.

## Note:
 For production deployment, consider using a production-ready web server and database.
 Implement appropriate security measures to protect your application and data.
 Customize the application to fit your specific needs and requirements.

## Additional Information:
 Django Documentation: [https://docs.djangoproject.com/en/5.1/](https://docs.djangoproject.com/en/5.1/)
 MongoDB Documentation: [https://www.mongodb.com/](https://www.mongodb.com/)



## Programming languages and tools used:-
<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" alt="mongodb" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Developer
*  [abhineetraj1](https://github.com/abhineetraj1)