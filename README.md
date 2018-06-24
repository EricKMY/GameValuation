# GameValuation
# GameValuation

environment setting:
  Anaconda(python3):
    requrire 3 package pymysql, scikit learn and Django

  MySQL:
    set yor database as follow:
      MYSQL_HOST = 'localhost'
      MYSQL_DBNAME = 'steam'
      MYSQL_USER = 'root'
      MYSQL_PASSWD = '5566'

      import topseller2017.sql into 'steam',
      set a new sechma in 'steam' called "top_seller",
      the colume are excatly the same as topseller2017.sql

    Steps:
      1.open Anaconda shell
      2.go to "GameValuation/scrapysteam"
      3.insert "crawl scrapy topsellerspider"
      4.go to "GameValuation/DataClassification"
      5.run "main.py"
