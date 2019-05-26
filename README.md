## HighMarkHealth
They key objective was to help Highmark to understand the underlying data of claims and help them shape policies. We also a decision support tool which can help in taking a decision when they are rejecting the pre-auth.

## Problem 
Reduce time spent in the appeal process for cases that never should have been denied.

## Motivation
Highmark an 18.8 billion revenue company, with their Health Plan membership is stable with 4.5 million members in their core markets of Pennsylvania, West Virginia and Delaware. Highmark remains the commercial market share leader in western PA with a **retention rate** of **94** percent and membership of 2.3 million, as they continue to offer key differentiators with their client services and ancillary product offerings.

Every year more than a million medical claims are filed in the United States of America. The ever- increasing cost of healthcare, changing dynamics of the policies around health care a competition from other healthcare companies create few of the business risks such as
1. Constantly Optimization their hospital network.
2. Retention of customers from competitors.
3. Maintain 60 Days or less turnaround time for appeals. 
4. Avoid Mispricing medical trend.

Our capstone tries to solve two of the above issues, Faster claims process and insight into the types of claims costing time and money to highmark. We provide a Exploratory tool and an Decision support tool to help with the process. Our tool will help highmark to keep or improve their medical star ratings, reduce in time spent, higher customer satisfaction and help them increase their revenue.

## Project Methodology
The dataset for this project was open source and was available from the Office of Medicare Hearings and Appeals (OMHA). We built exploratory data analysis web tool to identify the underlying data through the united states. We built multiple machine learning models and finally settled on the best performing model for the available dataset. With that knowledge we built another web tool and combines our machine learning model with predictive tool to give an easy access to use the models which we built.

## Installation
* Step 1
- Python
Linux:
```sh
sudo apt-get install python3
```
MacOS
Install Xcode
```sh
xcode-select --install
```
If you dont have [HomeBrew](https://brew.sh) please install it first
```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python 3
```sh
brew install python3
```

* Step 2
Install anaconda for all in one installation.
- [Anaconda](https://www.anaconda.com/distribution/)

Or Install manually

```sh
python3 -m pip install --upgrade pip
```
NumPy
```sh
python3 -m pip install --user numpy
```
Scipy
```sh
python3 -m pip install --user scipy
```
Pandas
```sh
python3 -m pip install --user pandas
```
scikit
```sh
pip install -U scikit-learn
```
Jyupter NoteBook
```sh
python3 -m pip install jupyter
```
* Step 3
- Django
```sh
pip install Django
```
- PostgreSQL
Please Intall for the DataBase according to your operating system [PostgreSQL](https://www.postgresql.org/download/)


## Tech/framework used
	- Python3
	- Django
	- BootStarp
	- PostgreSQL
	- Machine Learning Models via SkLearn & native installation.
	- AWS



## How to use?
Run the 
cd into this directory
```sh
jupyter notebook
```
run the **prediction model.ipynb**
Place the **finalmodel.pkl** under the folder in
PredictiveWeb/predictive_framework/model/replacethiswith_finalmodel.pkl

Run the PredictiveWeb django project.

## Contribute

You can contribute to this opensoure project by contacting

* [Suman Giri](Suman.Giri@highmark.com) - Highmark Health
* [Melih Ozbek](Melih.Ozbek@highmark.com) - Highmark Health
* [Aditya Kamatar](adityakamatar@gmail.com) - Carnegie Mellon University
* [Jie Lou](jlou1@andrew.cmu.edu) - Carnegie Mellon University
* [Juwen Zhang](juwenz@andrew.cmu.edu) - Carnegie Mellon University
* [Shekhar Tanwar](stanwar@andrew.cmu.edu) - Carnegie Mellon University
* [Donald Taylor](dtaylor@scivelo.pitt.edu) - Univeristy of Pittsburgh


## License
This will be updated shortly.