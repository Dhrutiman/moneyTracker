# Money Tracker 

![Project Image](static/images/moneyTrackerHomePage.png?raw=true "Home Page")

> This is a ReadMe

---

### Table of Contents
You're sections headers will be used to reference location of destination.

- [Description](#description)
- [How To Use](#how-to-use)
- [License](#license)
- [Author Info](#author-info)

---

## Description
moneyTracker is a money tracking web app. Which provide us with our monthly expenses, daily transactions, and other information in a gook looking graph and charts. For that, we have to upload our bank transaction statement as a CSV file and add category and subject to each entered transactions to show in our homepage.

>NOTE: This app is not going to be host online.

#### Technologies

- Python 3.7
- Django 3.0.8
- Bootstrap
- HTML and CSS
- Chart.js

[Back To The Top](#Money-Tracker )

---

## How To Use

#### Installation
First, clone the GitHub repo and run the [requirements.txt](requirements.txt) file in the main project directory (moneytracher) to import all required liberals and dependency.
```posh
(dhruti) C:\Myproject\moneyTracker>pip install -r requirements.txt
```
Now start up the Django server and open the [localhost](http://127.0.0.1:8000/) url in your browser.

```posh 
(dhruti) C:\Myproject\moneyTracker>python manage.py runserver
```
First to use the app, you have to create a super-user for login and other function.

```posh 
(dhruti) C:\Myproject\moneyTracker>python manage.py createsuperuser
```
#### Adding transaction to database
In the browser navigate to get_csv/upload and upload a bank statement in csv formate. Then add category to all the recent transiction you have uplode.

![Project Image](static/images/monetTrackerUplodeCSV?raw=true "UplodeCSvPage")

![Project Image](static/images/moneyTrackerAddCategoryTotransiction.png?raw=true "AddCategoryPage")

[Back To The Top](#Money-Tracker )

---


## License

MIT License

Copyright (c) [2020] [Dhrutiman Sethi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#Money-Tracker )

---

## Author Info

- LinkedIn - 

[Back To The Top](#Money-Tracker )
