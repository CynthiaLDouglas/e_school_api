# Application Title: E-School LMS

As a forever educator, I left the classroom with the goal to bring back tech solutions that would promote access to technology to all students regardless of where, when and how they were born. Now more than ever we need solutions to keep our students learning and growing. E-School LMS will be the tech solution for virtual learning. A virtual one-stop shop, E-School LMS will provide a more organized, interactive space for students and educators to continue on as if they never left the classroom. This early version of the app allows users to create and register for courses. Users are authenticated and able to make changes to their user account. Course are available for view, updating and can be deleted. Registration is open! Students may register for courses using the course id and their student id number.

## Setup Steps

1. [Fork and clone](https://git.generalassemb.ly/ga-wdi-boston/meta/wiki/ForkAndClone) this repository.
2. Run `pipenv shell` to enter virtual environment.
3. Run `pipenv install` to install dependencies.
4. Create a psql database for your project
- Edit settings.sql
- Type psql to get into interactive shell.
- Run CREATE DATABASE "project_db_name"; where project_db_name is the name you want for your database.
5. Open the repository in Atom with `atom .`
6. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
7. Replace all instances of `django_auth_template` with your application name. **This includes the folder included in this repository.**
8. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |


## Important Links

- [Client Repository](https://github.com/CynthiaLDouglas/e_school_client)
- [API Repository](https://github.com/CynthiaLDouglas/e_school_api)
- [Deployed API](https://e-school-lms.herokuapp.com/)
- [Deployed Client](https://cynthialdouglas.github.io/e_school_client/))

## Planning Story

I was very ambitious this time around. I found that there were many things that I had to continue to learn about Django, python, serializers... Ah! - You name it. Many of the things I encountered, I had to relearn the lot of it. I began a very large idea and scaled back thinking that I could potentially acheive developing a learning management system in four days. Initially, my user stories included multiple types of users and multiple resources. I quickly realized I had to use my time to get back to the basics. I spent a large amount of time on the backend working to develop a table that combined information from two existing tables. ForeignKeys were traded for serializers and models we built, deleted and rebuilt. Eventually, working on this idea of having a table that connected two others, I was able to CRUD on a resource that had values that existed in other places! On the front end, I tried my hand at some custom styling and more. This was an excellent learning experience and though I'm not there yet, I believe that experiences like these will help me grow as a developer in the long run.

### User Stories

- As a user, I would like to be able to sign up.
- As a user, I would like to be able to sign in.
- As a user, I would like to be able to sign out.
- As a user, I would like to be able to change password.
- As a user, I would liek to be able to create a new course.
- As a user, I would liek to be able to update a course.
- As a user, I would like to be able to delete a course.
- As a user, I would like to be able to view a single course or multiple courses.

### Technologies Used

- Python
- Django
- PostgreSQL
- cURL
- Psycopg2
- Gunicorn
- WhiteNoise
- Heroku

### Catalog of Routes

| Verb   | URI Pattern            | Controller#Action      |
|--------|------------------------|------------------------|
| POST   | `/sign-up`             | `users#signup`         |
| POST   | `/sign-in`             | `users#signin`         |
| DELETE | `/sign-out`            | `users#signout`        |
| PATCH  | `/change-password`     | `users#changepw`       |
| GET    | `/courses`             | `courses#index`        |
| GET    | `/courses/:id`         | `courses#index`        |
| POST   | `/courses`             | `courses#create`       |
| PATCH  | `/courses/:id`         | `courses#update`       |
| DELETE | `/courses/:id`         | `courses#delete`       |
| GET    | `/registrations`       | `registrations#index`  |
| POST   | `/registrations`       | `registrations#create` |

### Unsolved Problems

#### Still need to:
- Finish building the registration resource on the front end.
- Create a user friendly registration form.
- Create two different views for students and teachers.

#### Would like to eventually:
- Add more resources including assignments and messages between users.
- Separate user types.

## Images

### ERD:
[Click to view `Proposed ERD`](https://i.imgur.com/Pbv7lna.jpg)
<img src="https://i.imgur.com/Pbv7lna.jpg">

[Click to view `Current ERD`](https://i.imgur.com/SKp5ZcP.jpg)
<img src="https://i.imgur.com/SKp5ZcP.jpg">
