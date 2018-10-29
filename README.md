
# Logs Analysis Poject

This is a python project that analyis the data on a database and print the result on text file.

## Getting Started

in order to run this poject you have to install some tools and have a linux environment 

### Prerequisites

* [python3](https://www.python.org/)
* [virtualBox](https://www.virtualbox.org/wiki/Downloads)
* [vagrant](https://www.vagrantup.com/downloads.html)


### Instructions
1. Install vaitualbox and vagrant 
2. Download a linux image inside  a newly created directory:
 	```
 	mkdir virtualdir
 	cd virtualdir
 	vagrant init ubuntu/trusty64
 	vagrant up
 	```
3. [Download the data from here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 
4. login to your Linux machine 
 	```
 	vagrant ssh
 	```

5. update the packages
 	```
 	sudo apt-get update && sudo apt-get upgrade
 	```
6. cd into the vagrant directory and load the data
 	```
 	cd /vagrant
 	psql -d news -f newsdata.sql
 	```
7. clone the the repository
 	```
 	https://github.com/athraalbahli/logs_analysis.git
 	```

 8. cd into the project and run the python file
 	```
 	cd logs_analysis
 	python3 report.py
 	```



