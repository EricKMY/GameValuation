# GameValuation
# GameValuation

Environment Setting:

  Anaconda(python3):
    requrire 3 package pymysql, scikit learn and Django

  MySQL:
    set yor database as follow:
      HOST_NAME = 'localhost'
      DB_NAME = 'steam'
      USER_NAME = 'root'
      PASSWD = '5566'

      import topseller2017.sql into 'steam' schema as a new table called 'top_seller_2017',
      set a new table in 'steam' schema called 'top_seller',
      the colume are excatly the same as 'top_seller_2017'.

Steps:
  1.open Anaconda shell
  2.go to folder "GameValuation/scrapysteam"
  3.run "crawl scrapy topsellerspider"
  4.go to folder "GameValuation/DataClassification"
  5.run "main.py"
