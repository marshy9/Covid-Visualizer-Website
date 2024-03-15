<a name="br1"></a> 

Team 10



<a name="br2"></a> 

Tools Used:

●

This product is a COVID-19 data visualizer that allows the

user to view COVID-19 data in a meaningful way; this

application allows the user to view COVID-19 cases, as well as

COVID-19 deaths, on a map of the United States.

The map is divided into cells that correspond to each of the

counties that exist in a particular state.

The user can zoom in and out on the map, as well as hover

over a particular county in order to view the corresponding

information (deaths, cases).

●

Jupyter Notebook to develop a python

script to build the SQLite database

VS Code to develop the HTML, and

Javascript files needed to create our

user interface

●

●

●

●

VS Code to develop the python with

flask for the REST API

●

●

Jira to manage the overall project

Github for file transfer and .csv file

hosting

●

●

●

The data visualizer also includes a legend in order to provide

the user with context for relative levels of cases and deaths

by county.

The map makes use of a color ramp in order to help display

the data in a meaningful way; the darker the color, the higher

concentration of deaths or cases in that particular county.

The application allows users to view prison COVID-19 data via

a state searcher



<a name="br3"></a> 

\-

\-

\-

\-

\-

People need access to live updated maps that represent Covid19 infection rate and death rate

across the US, to determine what places are safe to go to and what places should be avoided.

People Also need Covid19 infection and death rates for prisons, to check the safety of family

members or loved ones that have been incarcerated.

Research could be done on Covid related incidents related to the population compared to

incidents that occur in prisons

The Government could use this software as reference of how effective implemented policies

are against the Covid infection rate.

Healthcare workers can study trends via the search tool to predict where Covid hotspots will

next occur



<a name="br4"></a> 

Rest API

Database

Server

UI



<a name="br5"></a> 

General Steps taken to complete the project:

\-

\-

\-

\-

Step 1: Designed, planned out and analysed the

project in sprint 1.

Step 2: Started with the implementation and testing

of the database (Sprint 2).

Step 3: Moved on to implement and test the UI

(Started at Sprint 2)

Step 4: Finally connected the UI and database

through the use of the REST API.

Architecture

● UI → (HTML / Vega Javascript)

● Server → Local server.

● Rest API → (Python - flask)

● Database → (SQlite3)



<a name="br6"></a> 

Modeling

●

We began by determining that our project would require 3 major components (along with the REST API) in

order to function: the database, the server, and the user interface

●

●

We determined that we wanted a simple database so we began research into SQLite, and PostgreSQL

We found a resource called VEGA that would allow us to use Javascript to create a US map visualization,

and we simultaneously began research into React

Development

●

●

The first step was to begin work on the database; we created a python script that would parse the .csv

files and generate a SQLite database to store the information

Once the database was developed, we began work on the user interface; the first implementation was

done using React and proved to be too robust for use in this project. We shifted our focus to using VEGA

in order to created the map and have it render our dataset.

●

After building the user interface, we created a REST API to relate our database to our user interface. The

REST API performs a GET request such that prison data from the database can be posted on our website.



<a name="br7"></a> 

Code Inspection

● We began creating a list of known bugs, which can be found in our administration manual,

with the hopes that we could determine the root cause and resolve the issues.

● We conducted research about the bugs in order to see if the issues were being caused by

outside factors; for instance, the issue relating to the onClick() function in our HTML

appears to be present for many developers across all web browsers.

Testing process

● The first step was to test the database since this would serve as the backbone of the

project.

● Once we ensured that the database was functional to our standards, we began testing the

user interface to ensure that it would render properly and display the map and its data.

● After the user interface had been established, we tested the REST API to confirm that the

GET request to pull data from the database was working correctly.



<a name="br8"></a> 

\-

Graphical representation of US

map Implemented with the use of

Vega Javascript

\-

\-

Other functionality implemented

through HTML language

Creation of various utilities such as

buttons and console messages

notifying the user that a selection

was processed

Demonstration



<a name="br9"></a> 

\-

\-

\-

Local Server hosted on one

machine.

API was implemented using python

\+ flask.

Used to extract information from

the database, in order to display

prison information regarding a

specific state.

Demonstration



<a name="br10"></a> 

\-

\-

Implemented using sqlite3 and

python

Can run all basic queries (including

creating new tables or dropping

existing ones)

\-

\-

Creation of two distinct tables:

Prison data and COVID data

Allows the user to supply queries to

the local database in sqlite, and

returns the results to the user (in a

visible form)

\-

Used to generate the .db file to be

used by the UI

Demonstration



<a name="br11"></a> 

Link:

https://docs.google.com/document/d/1E

BIc3WRq7fjWBLchLYg3WwmKFF4rwWoj4

Mkh\_WFUcic/edit



<a name="br12"></a> 

For the UI implementation, we might have used a more robust JavaScript framework such as Angular

or React

\-

\-

\-

\-

Would have improved the user experience as more functionalities could have been given to the

UI.

Mapping utility would have been a React or Angular component, not the Vega interface we

used.

Would allow for additional functionalities to be added down the line with the addition of new

components.

With given time restrictions, being able to master such a complex language such as Angular

was not feasible.



<a name="br13"></a> 

\-

\-

\-

\-

\-

Fixing a few bugs that have been observed while testing.

Graphs of populations. Ex: graph showing infection rate per state.

Using prediction algorithms from the field of AI, to predict future covid incidents.

Creating a full fledged server, instead of the current local one.

Having the datasets (Prison and COVID csv files) hosted on Github or some other domain to

allow for easier access to the data; the prison dataset requires the user to install the .csv file

and pull from a local file for the database, UI, and REST API

\-

Overall UI improvements to give the website a more professional look - the use of CSS and

other tools could have aided in this prospect



<a name="br14"></a> 

\-

\-

\-

\-

\-

\-

Agile Scrum

Software Development Life Cycle

Modeling of Software

Basic HTML

Basic Javascript

The process of connecting different frameworks together. Such as, using the vega javascript

framework to display the information from our database.

Full stack development: creating not only the client side applications but server side too

White box testing, being able to understand the code we have while we perform various tests

Jira to manage user stories, sprints, epics, etc.

\-

\-

\-



<a name="br15"></a> 



<a name="br16"></a> 

<https://imposters.atlassian.net/secure/RapidBoard.jspa?projectKey=P0&rapidView=2>

