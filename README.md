# Flask Code Challenge - Hogwarts Classes

For this assessment, you'll be working with a vendors and sweets domain.

In this repo:

- There is a Flask application with some features built out.

To test your app you can:

- Use Postman to make requests

## Setup

The instructions assume you changed into the `code-challenge` folder **prior**
to opening the code editor.

To download the dependencies for the frontend and backend, run:

```console
pipenv install
pipenv shell
```

You can run your Flask API on [`localhost:5555`](http://localhost:5555) by
running:

```console
python server/app.py
```

Your job is to build out the Flask API to add the functionality described in the
deliverables below.

## Models

You will implement an API for the following data model:

![diagram](https://i.imgur.com/It1xwtE.png)

The file `server/models.py` defines the model classes **without relationships**.
Use the following commands to create the initial database `app.db`:

```console
export FLASK_APP=server/app.py
flask db init
flask db upgrade head
```

Now you can implement the relationships as shown in the ER Diagram:

- A `Subject` has many `Student`s through `SubjectEnrollment`
- A `Student` has many `Subject`s through `SubjectEnrollment`
- A `SubjectEnrollment` belongs to a `Subject` and belongs to a `Student`

Update `server/models.py` to establish the model relationships. Since a
`SubjectEnrollment` belongs to a `Subject` and a `Student`, configure the model to
cascade deletes.

Set serialization rules to limit the recursion depth.

Run the migrations and seed the database:

```console
flask db revision --autogenerate -m 'message'
flask db upgrade head
python server/seed.py
```

> If you aren't able to get the provided seed file working, you are welcome to
> generate your own seed data to test the application.

## Validations

Add validation to the `Student` model:

- `age` student cannot be younger than 11 years old and older than 18

Add validation to the `SubjectEnrollment` model:

- `enrollment_year` year has to be before 2023

## Routes

Set up the following routes. Make sure to return JSON data in the format
specified along with the appropriate HTTP verb.

### GET /students

Return JSON data in the format below:

```json
[
  { "id": 1, "name": "Hermione Granger", "age": 12 },
  { "id": 2, "name": "Cedric Diggory", "age": 14 }
]
```

### GET /students/:id

If the `Student` exists, return JSON data in the format below:

```json
{
  "id": 1,
  "name": "Hermione Granger",
  "age": 12,
  "subject_enrollments": [
    {
      "id": 1,
      "enrollment_year": 1997,
      "subject": {
        "id": 2,
        "title": "Herbology"
      },
      "student_id": 1,
      "subject_id": 2
    }
  ]
}
```

If the `Student` does not exist, return the following JSON data, along with the
appropriate HTTP status code:

```json
{
  "error": "Student not found"
}
```

### GET /subjects

Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "title": "Defense Against the Dark Arts"
  },
  {
    "id": 2,
    "title": "Herbology"
  }
]
```

### GET /subjects/<int:id>

If the `Subject` exists, return JSON data in the format below:

```json
{
  "id": 1,
  "title": "Defense Against the Dark Arts"
}
```

If the `Subject` does not exist, return the following JSON data, along with the
appropriate HTTP status code:

```json
{
  "error": "Subject not found"
}
```

### POST /subject_enrollments

This route should create a new `SubjectEnrollment` that is associated with an existing
`Subject` and `Student`. It should accept an object with the following properties
in the body of the request:

```json
{
  "enrollment_year": 2002,
  "student_id": 1,
  "subject_id": 2
}
```

If the `SubjectEnrollment` is created successfully, send back a response with the
following data:

```json
{
  "id": 4,
  "enrollment_year": 2002,
  "subject": {
    "id": 2,
    "title": "Herbology"
  },
  "subject_id": 2,
  "student": {
    "id": 1,
    "name": "Hermione Granger"
  },
  "student_id": 1
}
```

If the `SubjectEnrollment` is **not** created successfully, return the following JSON
data, along with the appropriate HTTP status code:

```json
{ "errors": ["validation errors"] }
```

### DELETE /subject_enrollment/<int:id>

This route should delete an existing `SubjectEnrollment`. If the `SubjectEnrollment` exists
and is deleted successfully, return an empty object as a response:

```json
{}
```

If the `SubjectEnrollment` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Subject Enrollment not found"
}
```
