# PostGIS

### docker-compose.yml
```
version: "3"

services:
  db:
    image: kartoza/postgis
    environment:
      - POSTGRES_DBNAME=djangopostgist
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgrespassword
    ports:
      - 5432:5432
    volumes:
      - dbdata:/var/lib/postgresql/data

volumes:
  dbdata:
```

### 新增places表
```SQL
create table places(
    name VARCHAR(100)
);
```

### 新增欄位
```SQL
SELECT AddGeometryColumn ('public', 'places', 'geom', 4326, 'POINT', 2);
```

### 新增資料
```SQL
INSERT INTO places(name, geom)
VALUES ('台北101', ST_GeomFromText('POINT(121.5645294 25.0338489)', 4326));
```

### 查詢格式(ST_AsKML)
```SQL
select name, ST_AsKML(geom) from public.places;
-- 台北101	<Point><coordinates>121.564529399999998,25.033848899999999</coordinates></Point>
```

### 查詢格式(ST_AsGML)
```SQL
select name, ST_AsGML(geom) from public.places;
台北101	<gml:Point srsName="EPSG:4326"><gml:coordinates>121.5645294,25.0338489</gml:coordinates></gml:Point>
```

### 查詢格式(ST_AsGeoJSON)
```SQL
select name, ST_AsGeoJSON(geom) from public.places;
台北101	{"type":"Point","coordinates":[121.5645294,25.0338489]}
```

### 計算距離(公里)
```SQL
SELECT ST_Distance(
    ST_GeogFromText('POINT(121.5173748 25.0477022)'), --台北車站
    ST_GeogFromText('POINT(121.5645294 25.0338489)') --台北101
) / 1000;  --5.0000050618300005
```

### 根據某個點計算距離
```SQL
select id, name,
    round(
        (ST_Distance(geom, ST_GeogFromText('POINT(121.539737 25.070699)')) / 1000)::numeric(8, 5),
        4
    ) as distance_km --算距離四捨到小數後4
from places
order by distance_km desc --依照距離遞增/減排序
limit 1; --最近的
-- id   name    distance_km
--  1   台北101    4.7877
--  3   台北車站    3.4031

```

```SQL
select 
        id, name, address, location,
        round(
                (ST_DistanceSphere(location, 'SRID=4326;POINT(121.519233 25.068416)'::geometry) / 1000)::numeric(8, 5),
                4
        ) as distance_km
from places
where ST_DistanceSphere(
        places.location,
        'SRID=4326;POINT(121.519233 25.068416)'::geometry
) < 10000
order by distance_km desc;
```

### Reference
* PostGIS官網 [link](https://postgis.net/install/)
* XXX [link]()
* XXX [link]()