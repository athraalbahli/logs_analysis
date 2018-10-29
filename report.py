import psycopg2

DBNAME = "news"


def get_log():
    db = psycopg2.connect(database=DBNAME)
    question1 = db.cursor()
    question1.execute('''
    select b.title,count(path) as num from log as a join
    articles as b on substring(a.path,10) = b.slug
    where a.status = '200 OK'group by b.title order by num desc limit 3;
    ''')
    popular_articles = question1.fetchall()

    f.write("Most popular three articles of all time:\r\n")
    for article in popular_articles:
        f.write('''"{}" - {} views\r\n'''.format(article[0], article[1]))
    f.write('\r\n')

    question2 = db.cursor()
    question2.execute('''
    select (select name from authors where id = b.author)
    author_name, count(path) as views from log as a join articles as b on
    substring(a.path,10)  = b.slug where a.status = '200 OK' group by
    author_name order by views desc;
    ''')
    popular_authors = question2.fetchall()
    f.write("Most popular article authors of all time:\r\n")
    for author in popular_authors:
        f.write('''{} - {} views\r\n'''.format(author[0], author[1]))
    f.write('\r\n')

    question3 = db.cursor()
    question3.execute('''
    select TO_CHAR(a.time::timestamp::date,
    'Mon dd, yyyy'), ROUND(not_found::decimal/count(id) * 100,2)
    as errors from log as a left join
    (select time::timestamp::date, count(id) not_found from log  where
    status = '404 NOT FOUND' group by time::timestamp::date) as b on
    a.time::timestamp::date = b.time::timestamp::date group by
    a.time::timestamp::date,
    b.not_found having ROUND(not_found::decimal/count(id) * 100,2) > 1
    order by errors desc;
    ''')
    errors = question3.fetchall()
    f.write("Days with more than 1% of requests lead to errors:\r\n")
    for error in errors:
        f.write('''{} - {} % errors \r\n'''.format(error[0], error[1]))
    f.write('\r\n')
    db.close()


f = open("logs.txt", "w+")
f.write("Logs Analysis \r\n")
f.write('''
========================================================
========== \r\n\r\n
''')
get_log()
f.close()
print("information has been writtin on logs.text")
