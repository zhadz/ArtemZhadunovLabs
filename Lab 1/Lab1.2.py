# TODO Найдите количество книг, которое можно разместить на дискете
one_symbol_b = 4
symbols_in_line = 25
lines_in_page = 50
pages_in_book = 100
v_disc_mb = 1.44

v_one_line_b = symbols_in_line * one_symbol_b
v_one_page_b = v_one_line_b * lines_in_page
v_one_book_b = v_one_page_b * pages_in_book
v_one_book_mb = v_one_book_b / (1024 ** 2)
max_books = v_disc_mb // v_one_book_mb
print("Количество книг, помещающихся на дискету:", int(max_books))
