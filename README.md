# Udacity Database Logs Project

## Description

This program is created as the project for Udacity Fullstack Web Developer nanodegree program.
It serves as a reporting tool for the PostgreSQL database that was already
provided by Udacity. It answers each question (ex: What are 3 most popular
articles in the database) using only one SQL query per question.

## Requirements

In order to successfully run this program, it is required to have Python installed. Further instructions for downloading and installing Python can be found on  [official python website](https://www.python.org/).
##### Note
Python 3 is required.

Additional Python package required:
- psycopg2

Can be installed from the command line using pip:

`pip install psycopg2`

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

In terminal run a command:

`python3 dblogs.py`

or `cd` to the directory where the program is located and run:

`./dblogs.py`
