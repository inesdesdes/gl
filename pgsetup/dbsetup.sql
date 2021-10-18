CREATE SCHEMA report;
CREATE EXTENSION dblink;
CREATE TABLE report.purchase (
    id int,
    order_date timestamp,
    order_status varchar(20),
    customer_id int,
    product varchar(50),
    quantity int,
    total_price int
);

COPY report.purchase(id,order_date,order_status,customer_id,product,quantity,total_price) 
FROM '/input_data/dummydata.csv' DELIMITER ','  CSV HEADER;
