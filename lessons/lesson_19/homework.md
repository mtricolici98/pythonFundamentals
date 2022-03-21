# Homework

Use the [following](lesson_19.md#creating-a-database-and-testing) instructions to create your database in DataGrip.

## Foreword

Save all your queries in 1 file. You can send me that file for validation.

If you have any questions, let me know.

## Task

You are creating a database for a company

They need to track the following: Their employees, and their projects.

## Create a table

We need a table to keep track of our employees

We want to record the following data for each employee

* first name: varchar
* last name: varchar
* idnp: char(13) (primary key)
* salary: bigint
* position: varchar

## Insert values into the table

Insert values into your new table.

Example data:

| idnp          | first\_name | last\_name | salary | position            |
|:--------------|:------------|:-----------|:-------|:--------------------|
| 2102031023011 | John        | Smith      | 10500  | Office manager      |
| 2102031012042 | Kenau       | Reeves     | 9400   | Office manager      |
| 2102031011522 | Kathy       | Diaz       | 15000  | Administrator       |
| 2102031681298 | Juan        | Rogers     | 20000  | Director            |
| 2102031138438 | Ruth        | Stewart    | 12000  | Project manager     |
| 2102031384568 | Raymond     | Johnson    | 13000  | Project manager     |
| 2102031684583 | Rebecca     | Bell       | 8000   | Data Analyst        |
| 2102036844852 | Phyllis     | Torres     | 9500   | Sale representative |
| 2102031689912 | Frank       | Harris     | 6700   | Worker              |
| 2102031588321 | Linda       | Taylor     | 12000  | Sale representative |
| 2102031549818 | Jesse       | Wood       | 9000   | Worker              |
| 2102031489458 | Clarence    | Martin     | 9000   | Data Analyst        |
| 2102031693428 | Sandra      | Bryant     | 8000   | Worker              |
| 2102188435892 | Margaret    | Young      | 7000   | Sale representative |
| 2102034588321 | Scott       | Mitchell   | 15000  | Project manager     |
| 2102058123481 | Heather     | King       | 12000  | Worker              |
| 2102095492312 | Kimberly    | Turner     | 18000  | Project manager     |
| 2102065493281 | Walter      | Perez      | 16000  | Worker              |
| 2102065488233 | John        | Bailey     | 6000   | Project manager     |
| 2102031235818 | Judith      | Robinson   | 5000   | Worker              |
| 2102036549932 | Harold      | Anderson   | 8900   | Project manager     |
| 2102067983821 | Douglas     | Scott      | 6000   | Worker              |
| 2102036589891 | Larry       | Jackson    | 12000  | Worker              |
| 2102036981212 | Paul        | Walker     | 10000  | Sale representative |
| 2102031298148 | Keith       | Lopez      | 15000  | Data Analyst        |
| 2102084856231 | Thomas      | Butler     | 17000  | Worker              |
| 2102036594893 | Kathleen    | Clark      | 16000  | Data Analyst        |

## Update salary for a position

The company has had a lot of great success this year, because of this all employees are receiving a salary boost.

* Workers get 500 added to their salary.
* Project managers get 1000 added to their salary.
* Sale representatives get 700 added to their salary.
* Data analysts get 700 added to their salary.
* Administrators get 600 added to their salary.
* Directors get 1000 added to their salary.

```
update table
set column = column + 3
```

Create the necessary queries to make the updates

## Create a new table

Create a new table projects to track the projects of the company

The projects' table should contain the following columns:

* project name: char
* project country: char
* project lead: foreign key to user
* project budget: number
* project year: year

## Add data to the new table

Example data:

| name               | country     | project\_lead | project\_budget | project\_year |
|:-------------------|:------------|:--------------|:----------------|:--------------|
| Canary             | Switzerland | 2102036549932 | 120000          | 2021          |
| Hornets            | England     | 2102031138438 | 240000          | 2021          |
| Mercury            | Germany     | 2102036549932 | 820000          | 2021          |
| Limitless Horizons | Ukraine     | 2102036549932 | 200000          | 2021          |
| Moving Bird        | Moldova     | 2102031384568 | 100000          | 2021          |
| Project Breeze     | Iceland     | 2102034588321 | 15000000        | 2021          |
| Command Program    | Moldova     | 2102095492312 | 500000          | 2022          |
| Project Point      | Germany     | 2102065488233 | 6500000         | 2012          |
| Project Mecha      | France      | 2102031384568 | 1000000         | 2014          |
| Program Pad        | England     | 2102065488233 | 250000          | 2015          |
| Project Synergy    | Germany     | 2102031384568 | 500000          | 2018          |
| Dynamic Program    | Moldova     | 2102031384568 | 6800000         | 2019          |
| Project Zen        | France      | 2102031384568 | 9000000         | 2017          |

## Query the data

### Create a query to show all employees that earn more than 10000

### Create a query to show all project managers that earn more than 13000

### Create a query to show the sum of all project budgets by country.

### Create a query to show the most expensive project

### Create a query to show the year with the most budget

### Create a query to show the which employee (name and last name) managed the projects from the projects table.
