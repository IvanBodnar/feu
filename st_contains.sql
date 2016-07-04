
select  ST_Contains((select geom from trabajo.comunas where gid = 12), ST_SetSRID(ST_Point(-58.468228, -34.678193), 4326));

table trabajo.comunas;


select  ST_Contains(ST_Multi(ST_Union(geom)), ST_SetSRID(ST_Point(-58.488812, -34.684275), 4326)) from trabajo.comunas;