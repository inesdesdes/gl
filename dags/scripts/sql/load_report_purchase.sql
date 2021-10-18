COPY (
SELECT  id,
        order_date,
        order_status,
        customer_id,
        product,
        quantity ,
        total_price
    
       from report.user_purchase -- we should have a date filter here to pull only required data
) TO '{{ params.user_purchase }}' WITH (FORMAT CSV, HEADER);