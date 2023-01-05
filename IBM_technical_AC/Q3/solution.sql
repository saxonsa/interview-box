create view collection as
select article.owner_id, article.article_id, category_article_mapping.category_id
from article, category_article_mapping
where article.article_id = category_article_mapping.article_id;

create view CategoryNum as
select owner_id, count(distinct category_id) as different_category_count
from collection
group by owner_id
order by different_category_count desc;

select owner.owner_id, owner.owner_name, CategoryNum.different_category_count
from owner, CategoryNum
where owner.owner_id = CategoryNum.owner_id;