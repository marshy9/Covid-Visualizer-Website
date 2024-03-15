<h1> Covid Visualizer Website </h1>


**● Website Description:**

This product is a COVID-19 data visualizer that allows the user to view COVID-19 data in a meaningful way; this application allows the user to view COVID-19 cases, as well as COVID-19 deaths, on a map of the United States.

The map is divided into cells that correspond to each of the counties that exist in a particular state.

The user can zoom in and out on the map, as well as hover over a particular county in order to view the corresponding information (deaths, cases).

![image](https://github.com/marshy9/Covid-Visualizer-Website/assets/55929958/7d4eea04-5049-44f2-a35b-0842fa1576a7)


**● Tools Used:**
Jupyter Notebook to develop a python script to build the SQLite database
VS Code to develop the HTML, and Javascript files needed to create the user interface
flask for the REST API

![image](https://github.com/marshy9/Covid-Visualizer-Website/assets/55929958/a8116107-7b56-48aa-859f-173e28569daa)


The data visualizer also includes a legend in order to provide the user with context for relative levels of cases and deaths by county.
The map makes use of a color ramp in order to help display the data in a meaningful way; the darker the color, the higher concentration of deaths or cases in that particular county.
The application allows users to view prison COVID-19 data via a state searcher.
Graphical representation of US map Implemented with the use of Vega Javascript.
Implemented using sqlite3 and python, 

**● Creation of two distinct tables:**

Prison data and COVID data

![image](https://github.com/marshy9/Covid-Visualizer-Website/assets/55929958/3d4289de-deb2-4701-a241-384c7cf7fdef)

Allows the user to supply queries to the local database in sqlite, and returns the results to the user (in a visible form)



