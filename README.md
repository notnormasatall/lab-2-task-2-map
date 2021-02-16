# Module descriprion

The user enters coordinates and a year. The module
returns a map with the 10< closest filming locations in that year.
The location entered by the user is marked with a red mark, the filming location with a blue one.
All markers are connected to the main with a blue line. With a click on a marker
the user gets basic information about the film (title, year, address, distance
from the entered location).

# Result

The program helps to make a brief analysis of how many movies and where
were filmed in a certain year near a certain location.

# Example of the running process

Ввід здійснюється в одному рядку через пробіл (рік, широта, довгота)

### 2004 -37.9064862 144.7533059 - Australia
![text](Australia.jpg?raw=true "text")
### 2012 49.651179 24.2450 - Ukraine
![text](Ukraine.jpg?raw=true "text")
### 2011 38.9072 77.03692011 38.9072 77.0369 - China
![text](China.jpg?raw=true "text")

## Description of html file structure and markup tags

map.html file has a basic html structure.

<!DOCTYPE html> defines the file's markup language.

The main information of the file stays between the <head> </head> tags.
<script> </script> tags define some important information, <style>
</style> tags define css style of the file.

<body> </body> tags create the html fileand contain information 
that is displayed in the web browser (in this case it is map Class).

<script> </script> consists from all actions called in the main.py
module, but written in js.

## License
[MIT](https://github.com/notnormasatall/lab-2-task-2-map/blob/main/LICENSE)
