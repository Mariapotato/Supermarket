select prod_name, prod_measure, prod_price,(prod_price DIV $prod_price) from products
where prod_category = "$category" and prod_price < "$price"