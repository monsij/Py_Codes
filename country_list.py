#monsij
from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country_counts.get(country)==None:
        #country_list.add(country:1)
        country_counts[country]=1
    else:
        #k = country_list.get(country)
        country_counts[country] += 1
