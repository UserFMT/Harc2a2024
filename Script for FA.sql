--Выберите уникальные регионы сбора грибов.

select distinct name from Regions;

--Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».

select    
A1.name  "Название гриба",
A1. season "Сезон",
A1. Edible "Съедобность" 
from Mushrooms A1
join Categories A2 on A2. category_id = A1.category_id  
and A2.name = 'Трубчатые'

--Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.

select distinct 
A2.name "Категория",
count(1) "Количество"
from Mushrooms A1
join Categories A2 on A2. category_id = A1.category_id  
group by a2.name
order by count(1)  desc;

--Выведите название и описание съедобных грибов, которые лучше всего собирать в пяти самых больших по размеру (size) регионах.

select distinct A1.name, A1.description  
from  Mushrooms A1
where A1.edible
and A1.primary_region_id in (
select region_id from Regions order by size desc limit 5)


--Выведите названия всех грибов, которые растут весной, относятся к категории «Пластинчатые» и которые лучше всего собирать в местах размером до 6000 условных единиц (size).

select distinct A1.name
from  Mushrooms A1
join Categories A2 on A2. category_id = A1.category_id   and a2.name='Пластинчатые'
where
A1.season ='Весна'
and A1.primary_region_id in (
select A3.region_id from Regions A3 where A3.size < 6000 )
