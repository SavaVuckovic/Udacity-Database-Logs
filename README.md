# Udacity Database Logs Project

## Description

This program is created as the project for Udacity Fullstack Web Developer nanodegree program.
It serves as a reporting tool for the PostgreSQL database that was already
provided by Udacity. It answers each question (ex: What are 3 most popular
articles in the database) using only one SQL query per question.

## Requirements

In order to successfully run this program, it is required to have Python 3 installed. Further instructions for downloading and installing Python can be found on  [official python website](https://www.python.org/).

Additional Python package required:
- psycopg2

Can be installed from the command line using pip:

`pip install psycopg2`

You should also have vagrant and linux vm with PostgreSQL installed.

VM provided by udacity can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip)

Data to populate the PostgreSQL database, also provided by Udacity, can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Example output:

Top 3 most popular articles are:

	 Candidate is jerk, alleges rival --- 338647 views
	 Bears love berries, alleges bear --- 253801 views
	 Bad things gone, say good people --- 170098 views

Most popular article authors are:

	 Ursula La Multa --- 507594 views
	 Rudolf von Treppenwitz --- 423457 views
	 Anonymous Contributor --- 170098 views
	 Markoff Chaney --- 84557 views

On following days, more than 1% of requests have lead to errors: 

	 2016-07-17 --- 2.263 % errors

## Usage:

Download the VM provided by Udacity, set it u using `vagrant up` (it may take some time), and when it is done, ssh into it using `vagrant ssh`.

After that, download the database data provided by Udacity. After unzipping it, you should get the file named 'newsdata.sql'.  This file should be placed into vagrant directory so that it can be shared with vagrant VM. Than from vagrant VM run:

`psql -d news -f newsdata.sql`

In terminal run a command:

`python3 dblogs.py`

or `cd` to the directory where the program is located and run:

`./dblogs.py`
