-- Credits: Anatolie Barbaros (https://github.com/abarbaros1/Tekwill_Python_Home_Work/blob/master/home_work_lesson_19/hw_19.sql)
create table employees
(
    idnp       character(13) primary key,
    first_name varchar(255),
    last_name  varchar(255),
    salary     bigint,
    position   varchar(255)
);


insert into employees (idnp, first_name, last_name, salary, position)
values (2102031023011, 'John', 'Smith', 10500, 'Office manager'),
       (2102031012042, 'Kenau', 'Reeves', 9400, 'Office manager'),
       (2102031011522, 'Kathy', 'Diaz', 15000, 'Administrator'),
       (2102031681298, 'Juan', 'Rogers', 20000, 'Director'),
       (2102031138438, 'Ruth', 'Stewart', 12000, 'Project manager'),
       (2102031384568, 'Raymond', 'Johnson', 13000, 'Project manager'),
       (2102031684583, 'Rebecca', 'Bell', 8000, 'Data Analyst'),
       (2102036844852, 'Phyllis', 'Torres', 9500, 'Sale representative'),
       (2102031689912, 'Frank', 'Harris', 6700, 'Worker'),
       (2102031588321, 'Linda', 'Taylor', 12000, 'Sale representative'),
       (2102031549818, 'Jesse', 'Wood', 9000, 'Worker'),
       (2102031489458, 'Clarence', 'Martin', 9000, 'Data Analyst'),
       (2102031693428, 'Sandra', 'Bryant', 8000, 'Worker'),
       (2102188435892, 'Margaret', 'Young', 7000, 'Sale representative'),
       (2102034588321, 'Scott', 'Mitchell', 15000, 'Project manager'),
       (2102058123481, 'Heather', 'King', 12000, 'Worker'),
       (2102095492312, 'Kimberly', 'Turner', 18000, 'Project manager'),
       (2102065493281, 'Walter', 'Perez', 16000, 'Worker'),
       (2102065488233, 'John', 'Bailey', 6000, 'Project manager'),
       (2102031235818, 'Judith', 'Robinson', 5000, 'Worker'),
       (2102036549932, 'Harold', 'Anderson', 8900, 'Project manager'),
       (2102067983821, 'Douglas', 'Scott', 6000, 'Worker'),
       (2102036589891, 'Larry', 'Jackson', 12000, 'Worker'),
       (2102036981212, 'Paul', 'Walker', 10000, 'Sale representative'),
       (2102031298148, 'Keith', 'Lopez', 15000, 'Data Analyst'),
       (2102084856231, 'Thomas', 'Butler', 17000, 'Worker'),
       (2102036594893, 'Kathleen', 'Clark', 16000, 'Data Analyst')
;



update employees
set salary = salary + 500
where position = 'Worker';
update employees
set salary = salary + 1000
where position = 'Project manager';
update employees
set salary = salary + 700
where position = 'Sale representative';
update employees
set salary = salary + 700
where position = 'Data Analyst';
update employees
set salary = salary + 600
where position = 'Administrator';
update employees
set salary = salary + 1000
where position = 'Director';


create table projects
(
    name           varchar(255),
    country        varchar(255),
    project_lead   character(13),
    project_budget bigint,
    project_year year,
    foreign key (project_lead) references employees (idnp)
);



insert into projects (name, country, project_lead, project_budget, project_year)
values ('Canary', 'Switzerland', '2102036549932', 120000, 2021),
       ('Hornets', 'England', '2102031138438', 240000, 2021),
       ('Mercury', 'Germany', '2102036549932', 820000, 2021),
       ('Limitless Horizons', 'Ukraine', '2102036549932', 200000, 2021),
       ('Moving Bird', 'Moldova', '2102031384568', 100000, 2021),
       ('Project Breeze', 'Iceland', '2102034588321', 15000000, 2021),
       ('Command Program', 'Moldova', '2102095492312', 500000, 2022),
       ('Project Point', 'Germany', '2102065488233', 6500000, 2012),
       ('Project Mecha', 'France', '2102031384568', 1000000, 2014),
       ('Program Pad', 'England', '2102065488233', 250000, 2015),
       ('Project Synergy', 'Germany', '2102031384568', 500000, 2018),
       ('Dynamic Program', 'Moldova', '2102031384568', 6800000, 2019),
       ('Project Zen', 'France', '2102031384568', 9000000, 2017)
;

--Query the data

--employees that earn more than 10000
Select *
From employees
Where salary > 10000;

--project managers that earn more than 13000
Select *
From employees
Where 1 = 1
  and position = 'Project manager'
  and salary > 13000;

--the sum of all project budgets by country
Select country
     , sum(project_budget) as budget_by_country
From projects
Group by country
Order by budget_by_country desc;

--the most expensive project
Select name
     , max(project_budget)
From projects;

--the year with the most budget
Select project_year
     , max(project_budget)
From projects;

--which employee (name and last name) managed the projects from the projects table.
Select p.name                                 as project_name
     , emp.first_name || " " || emp.last_name as project_manager
From projects p
         Left Join employees emp on emp.idnp = p.project_lead;