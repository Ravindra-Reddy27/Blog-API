# Blog-API
This project is a RESTful Blog API built using FastAPI, SQLAlchemy, and PostgreSQL, implementing a one-to-many relationship between authors and posts. It demonstrates clean API design, efficient database querying, and proper relationship handling with cascade delete.



## Tech Stack

- **Language:** Python 3.10+  
- **Framework:** FastAPI  
- **ORM:** SQLAlchemy  
- **Database:** PostgreSQL  
- **Server:** Uvicorn
- **Editor:** VS Code

## Prerequirements 
Make sure you have:

1. **Python 3.10+** installed  
2. **PostgreSQL** installed and running  
3. **Git** installed
4. **VS Code** installed

## Database Setup 

1. Open your system terminal and connect to PostgreSQL:
   
   ` psql -U postgres `
2. Enter your PostgreSQL password when prompted.

   You should see the prompt:

   ` postgres=# `

3. Create the database:

   `CREATE DATABASE blog_db;`

   ( optional ) Check the databases using the `\l` command.
   
4. Exit from PostgreSQL:

    `exit `
5. Build your database connection link:
   
   `postgresql://postgres:YOUR_PASSWORD@localhost:5432/blog_db`

5. Test the database connection from the terminal (replace *YOUR_PASSWORD* with your actual PostgreSQL password):

   `psql postgresql://postgres:YOUR_PASSWORD@localhost:5432/blog_db`

6. If the connection is successful, you will see the database prompt:

   `blog_db=#`


## Cloning and Setup

1. Create a new folder on your system.
   
2. Open the folder in VS Code.
   
3. Open the integrated terminal using the shortcut:

   **ctrl + `**
4. Clone the repository:
   
   `git clone https://github.com/Ravindra-Reddy27/Blog-API.git`


5. Change the directory :

    `cd Blog-API`

6. Create a Python virtual environment:
   
   `python -m venv <VIRTUAL_ENVIRONMENT_NAME>`
   
7. Activate the virtual environment (Windows):
   
   ` <VIRTUAL_ENVIRONMENT_NAME>\Scripts\activate `

8. Install dependencies
   
   `python -m pip install -r requirements.txt`
10. Check your .env file (replace *YOUR_PASSWORD* with your actual PostgreSQL password)

    `DATABASE_URL="postgresql://postgres:YOUR_PASSWORD@localhost:5432/blog_db"`

12. Run the application

    ` python -m uvicorn app.main:app --reload `
13. If everything is correct, you should see something like:

    `Uvicorn running on http://127.0.0.1:8000 (Press CTRL+CLICK to open)`





## Testing the API

* Open the Swagger UI documentation in your browser:

  `http://127.0.0.1:8000/docs`


## Author Side :

### 1. Create an Author [Post]

* Click on the Endpoint: *POST /authors*.
* Click on *Try it out*.
* Enter the name and email values.
* Example
  
  `
  {
  "name": "Ravi Kumar",
  "email": "ravi@example.com"
  }
  `
* Execute the request.
* You should get a response like:

  
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
  201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
  
  `
  {
  "name": "Ravi Kumar",
  "email": "ravi@example.com",
  "id": 7
  }
  `
* Add a few more authors—this will help when testing the Create Post and List Posts endpoints later.

### 2. Get All Authors [GET]

* Click on the Endpoint: *GET /authors*.
* Click on *Try it out*.
* Execute the request.
* You should get a response like:

  
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
  201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body

  `
  [
  {
    "name": "Ravi Kumar",
    "email": "ravi@example.com",
    "id": 7
  },
  {
    "name": "somu",
    "email": "somu@example.com",
    "id": 8
  }
  ]
  `
### 3. Get Author By Id [GET]

* Click on the Endpoint: *GET /authors/{author_id}*.
* Click on *Try it out*.
* Enter the author_id.
   
  Example :

  `author_id : 7`
  
* Execute the request.
* You should get a response like
    * If author_id is there :

  
        Code&nbsp;&nbsp;&nbsp;&nbsp;Details
        
        201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
      
        `
        {
        "name": "Ravi Kumar",
        "email": "ravi@example.com",
        "id": 7
        }
        `

    * If author_id is not there :

  
        Code&nbsp;&nbsp;&nbsp;&nbsp;Details
        
        404&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Error: Not Found
      
        `
        {
        "detail": "Author not found"
        }
        `

### 4. Update The Author [PUT]

* Click on the Endpoint: *PUT /authors/{author_id}*.
* Click on *Try it out*.
* Enter the author_id:
   
  Example :

  `author_id : 7`
  
* Enter the update name and email values.
* Example
  
  `
  {
  "name": "Ravi",
  "email": "ravi@example.com"
  }
  `
* Execute the request.
* You should get a response like:

  
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
  201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body

  `
  {
  "name": "ravi",
  "email": "ravi@example.com",
  "id": 7
  }
  `
* If the author_id is not there you will get 404 Error: Not Found.

### 5. Delete The Author [DELETE]

* Click on the Endpoint: *DELETE /authors/{author_id}*.
* Click on *Try it out*.
* Enter the author_id:
  
  Example :

  `author_id : 8`
  
*  You should get a response like:

  
    Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
    201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Successful Response
  
* If the author_id is not there you will get 404 Error: Not Found.
  
**NOTE :**

If an author is deleted, all posts created by that author are automatically deleted (cascade delete).

---

## Post side :

### 1. Create a Post [POST]

* Click on the Endpoint: *POST /posts*.
* Click on *Try it out*.
* Enter the title,content and author_id values.
* Example
  
  `
  {
  "title": "8 author title",
  "content": "8 author content",
  "author_id": 8
  }
  `
* Execute the request.
* You should get a response like:

  
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
  201&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
  
  `
  {
  "title": "8 author title",
  "content": "8 author content",
  "id": 6,
  "author": {
    "name": "somu",
    "email": "somu@example.com",
    "id": 8
  }
  }
  `
* If the author_id is not there you will get 400 Bad Request.
* Add a few more posts—this will help when testing later.

### 2. Get All Posts [GET]

* Without author_id :
  
  * Click on the Endpoint: *GET /posts*.
  * Click on *Try it out*.
  * Execute the request.
  * You should get a response like:
  
    
    Code&nbsp;&nbsp;&nbsp;&nbsp;Details
    
    200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
  
    `
    [
    {
      "title": "8 author title",
      "content": "8 author content",
      "id": 6,
      "author": {
        "name": "somu",
        "email": "somu@example.com",
        "id": 8
      }
    }
    ]
    `

* With author_id :
 
  * Click on the Endpoint: *GET /posts*.
  * Click on *Try it out*.
  * Enter the author_id.

    Example :
    
    ` author_id : 8 `
  * Execute the request.
  * You should get a response like:
  
    
    Code&nbsp;&nbsp;&nbsp;&nbsp;Details
    
    200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
  
    `
    [
    {
      "title": "8 author title",
      "content": "8 author content",
      "id": 6,
      "author": {
        "name": "somu",
        "email": "somu@example.com",
        "id": 8
      }
    }
    ]
    `

### 3. Get Posts By post_id [GET]

* Click on the Endpoint: *GET /post/{post_id}*.
* Click on *Try it out*.
* Enter the post_id.

  Example :
    
    ` post_id : 6 `
  
* Execute the request.
* You should get a response like
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
        
  200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body
      
  `
  {
  "title": "8 author title",
  "content": "8 author content",
  "id": 6,
  "author": {
    "name": "somu",
    "email": "somu@example.com",
    "id": 8
  }
  }
  `
* If the post_id is not there you will get 404 Error: Not Found.

### 4. Update The Post [PUT]

* Click on the Endpoint: *PUT /post/{post_id}*.
* Click on *Try it out*.
* Enter the post_id:
  
  Example :
    
    ` post_id : 6 `
  
* Enter the update title and content values.
* Example
  
  `
  {
  "title": "8 title 2 update",
  "content": "8 content 2 update"
  }
  `
* Execute the request.
* You should get a response like:

  
  Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
  200&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Response body

  `
  {
  "title": "8 title 2 update",
  "content": "8 content 2 update",
  "id": 7,
  "author": {
    "name": "somu",
    "email": "somu@example.com",
    "id": 8
  }
  }
  `
* If the post_id is not there you will get 404 Error: Not Found.


### 5. Delete The Post [DELETE]

* Click on the Endpoint: *DELETE /post/{post_id}*.
* Click on *Try it out*.
* Enter the post_id:
  
  Example :
    
    ` post_id : 6 `
  
*  You should get a response like:

  
    Code&nbsp;&nbsp;&nbsp;&nbsp;Details
  
    204&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Successful Response
  
* If the post_id is not there you will get 404 Error: Not Found.

---
## Database Schema & Relationships:
This project uses a relational database with two main tables: Authors and Posts.
###  Authors Table:
The Authors table stores information about users who write blog posts.

#### Fields:
* `id` – Primary key, uniquely identifies each author

* `name` – Author’s name

* `email` – Author’s email address (must be unique)

###  Posts Table:
The Posts table stores blog posts written by authors.

#### Fields:
* `id` – Primary key, uniquely identifies each post

* `title` – Title of the blog post

* `content` – Main text/content of the post

* `author_id` – Foreign key that references Authors.id

### Relationship Between Tables:

* The relationship between Authors and Posts is one-to-many (1 → N).

* One author can write many posts.

* Each post belongs to only one author.

* This relationship is represented using the author_id foreign key in the Posts table.

* If an author is deleted, all posts created by that author are automatically deleted(Cascade Delete).


### Entity Relation Diagram: 

The ERD visually represents:

* **Entities:** Authors and Posts

* Attributes of each entity

* The “**writes**” relationship with 1 (Author) → N (Posts) cardinality

![Alt Text](https://github.com/Ravindra-Reddy27/Blog-API/blob/6fb80ce47be1c1f85faa530ab8bcede617de0752/Blog_API-ER-diagram.png). 


---

## Troubleshooting


**1. ModuleNotFoundError: No module named 'app':**

   * Make sure you are in the project root (same folder as app/).

   * Run:
  
     `python -m uvicorn app.main:app --reload`

**2. Packages not installed or command not found**
    
  If you see errors like:

  * `ModuleNotFoundError: No module named 'fastapi'`

  * `'uvicorn' is not recognized as an internal or external command`

  Solultion is install all dependencies:

  `pip install -r requirements.txt`

**3. Database connection errors :**

  * Check that PostgreSQL is running

  * Confirm your DATABASE_URL in .env is correct

  * Make sure the database (blog_db or your name) exists
