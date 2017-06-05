CREATE VIEW article_counter as 
SELECT articles.title, articles.author, count(log.path) 
as views FROM articles, log WHERE log.path LIKE '%'||articles.slug 
group by articles.title, articles.author order by views desc
;

CREATE VIEW Author_Count AS
SELECT
authors.name,
articles.title,
article_counter.views
FROM
authors
INNER JOIN articles ON authors.id = articles.author
INNER JOIN article_counter ON article_counter.title = articles.title;

create view author_leaderboard as
select
Author_Count.name,
sum(Author_Count.views) as views
FROM Author_Count group by Author_Count.name order by views desc;

create view article_leaderboard as
select title, views from article_counter order by views desc limit 3;	 
	 


create view date_overview as select total_query.date, error_query.error, total_query.total, ((error_query.error/total_query.total)*100) as percentage
from (select date(time), count(status) as error
from log
where status!= '200 OK'
group by date(time)) as error_query join
(select date(time), count(status) as total
from log
group by date(time)) as total_query on error_query.date=total_query.date;

create view bad_days as select date from date_overview where ((cast(error as float) / cast (total as float))*100)>1;

