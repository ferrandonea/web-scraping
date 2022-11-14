import time
elapsed_time = dict()

start = time.perf_counter()
import bs4_parsing
elapsed_time["bs4_time"] = time.perf_counter()-start

start = time.perf_counter()
import parsel_parsing
elapsed_time["parsel_time"] = time.perf_counter()-start

start = time.perf_counter()
import selectolax
elapsed_time["selectolax_time"] = time.perf_counter()-start

print ("="*12)
print ("COMPARACION DE TIEMPO")
for modulo in ["bs4", "parsel", "selectolax"]:
    mod_t = modulo + "_time"
    print (f"{modulo}: {elapsed_time[mod_t]}")


