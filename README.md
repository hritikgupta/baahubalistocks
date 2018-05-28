# BaahubaliStocks.com
### 'Stocks Aapke, Analysis Hamari’

This is the repository for our Stock Analyser project for the Course CS309 at IIT Mandi.

Contributors:
1. [ashking13th](https://github.com/ashking13th)
2. [Akai9866](https://github.com/Akai9866)
3. [hritikgupta](https://github.com/hritikgupta)

## How to use
1 Install Django
`sudo apt-get install python3-django`

2 Download this repository
3 Browse to the stocks directory in the terminal
4 `$ python manage.py migrate`
5 `$ python manage.py runserver`
6 Go to `localhost:8080` in your browser

## Overview
Day trading in stocks is risky, more so if you are untrained. When it comes to investing in stocks, it is important that the investor is capable of conducting a thorough technical analysis of stock charts. Technical analysis is used to define the process of forecasting future price movements based on the past price movements within stock charts. It is with the help of technical analysis that investors are able to make financial decisions of buying, holding, or selling stocks. 

By studying and evaluating past and current data, investors and traders attempts to gain an edge in the markets by making informed decisions. Such solutions and analysers are hard to find. If they exist, they cost you for the service.
BaahubaliStocks.com is a one-stop solution. Our site allows the customer to forecast which way the market is going to move and help the investor make a more financially sound investment decision. 
What all can be there?

The site will hold the historical and current trading data of stocks. It would give user the access to this raw data as well as processed data. Processed data can be like the minimum or maximum trading stock for a day, month or a year or min or max of a particular stock for a specific time frame.

Basic details of the stock like company it is linked to, all time high and low, initial offering date and price, dividend value shall be there in the details of a stock.

Background details of companies would also be there. This would keep record of all stocks linked to the company, its market value, profits, executives list among important details.

All this data can be used by our user to aid to his investment decisions.

## Definitions
**User** :	A customer, investor or analyst registered on our application.

**Stocks** :    A stock of a particular company at an exchange

**Company** :  A company, a commercial organization which may have one or more stocks trading in its name on the stock exchange.

**Favourite** : A user will be able to ‘favourite’ certain stocks or companies for easy access to them. 

## Design Features
**Login**
Users would be able to log in to our system using username and password.

**Stocks**
Stocks are the most important part. Stock prices will be stored in our database on which user can run query to get the max valued stock or the highest growing stock or the fastest growing stock which started within a specific time-frame given by the user.

**Company**
Any stock belongs to a company. A company may not be associated with a stock but all stocks shall certainly be associated with a company. User will be able to view details about a company as well as the stocks associated with it.

**Tags**
User can tag their stocks based on the companies they hold in, to get an overview of the type of stock.

**Bookmarks**
Users will be able to bookmark certain stocks that they can refer to in future.

## Target customer

People who have an eye for stock markets, be it analysts, investors, venture capitals, consultants or even enthusiasts.
As of now no low cost or free service is available in the market which does such a wide variety of tasks and provide predictions from a chunk of stock market data. Most of such services are very expensive. 

The platform will serve as a tool for users who are willing to invest in stock markets or are willing to get started with the same. 
Implementation

The solution will be implemented using Django Python framework with an underlying MySQL server database.

UI would use Bootstrap and JQuery objects. Backend development would be in Python Django framework using an underlying MySQL server.
Stock data would be fetched from the raw data available with the Alpha Vantage API and process it such that we can process our queries easily and efficiently. Data would be fetched and processed regularly and then stored in our local database.

Data visualizations in the form of tables and graphs would be made possible using the python libraries. Data could be sorted in a form as per the user’s choice. 

Company details will be fetched in real time from Wikipedia.
Users will have the ability to “favorite” or in more formal terms, bookmark any stocks they find of interest which will later give them a quick access to them.

## Required Hardware
For the purpose of this project all the data will be stored on our personal computers. Because of the constraints of our PC, we will store minute by minute stock data for the last 7 days, hour by hour stock data for the last one year and day wise data for the last 10 years.

## Performance Requirements:
On an PC which runs on an Intel Core i5 processor with 8 GB RAM, the maximum response time for any online request must be less than 2 secs. Around 50 MB memory is used for keeping record of a 100 million entries.

## ER Diagram :
An initial non normalized ER diagram for this project is attached here: 
![](https://github.com/ashking13th/baahubalistocks/blob/basic-structure/images/er-diag.PNG)

## Conclusion
BaahubaliStocks.com would be handy tool for thousands of people including investors and stock market enthusiasts to serve their purpose without spending a single buck, developed using Django, MySQL, HTML5, Bootstrap and JQuery on top of Alpha Vantage API and Python libraries. 
