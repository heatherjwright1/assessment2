USE foundation_assessment_ii;

-- Write a query to return the name and time of all movies that play after
-- 12:00 given there is at least 1 available seat. Display the results in time order.

-- 4.2 

select mi.movie_Name, mi.movie_ID, sh.available_Seats, sh.start_Time
from movie_info mi
join showings sh
on mi.movie_ID = sh.movie_ID
where available_Seats > 1 and sh.start_Time > '12:00:00'
order by 
case
when time (sh.start_Time) >= '12:00:00' then 0
else 1
end;

-- 4.3. movie_Name from movie_info

select mi.movie_Name mi, sh.showings
from movie_info mi
join showings sh
on mi.movie_ID = sh.movie_ID
(select mi.movie_Name mi, sh.showings
from movie_info mi
order by COUNT (*) desc
limit 1)
;