search = input("Enter the year of interest: ")

min_life_expectancy = float('999')
max_life_expectancy = float('000')
total_life_expectancy = 0
country_count = 0
min_year_life_expectancy = float('999')
max_year_life_expectancy = float('000')

with open("./life-expectancy.csv") as spanish_flu:
    next(spanish_flu)

    for line in spanish_flu:
        data = line.split(',')
        life_expectancy = float(data[3])
        country = data[0]
        year = data[2]   

        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_country = country
            min_year = year

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_country = country
            max_year = year
            
        if year == search and life_expectancy < min_year_life_expectancy:
            min_year_life_expectancy = life_expectancy
            year_min_country = country
            year_min_year = year
        
        if year == search and life_expectancy > max_year_life_expectancy:
            max_year_life_expectancy = life_expectancy
            year_max_country = country
            year_max_year = year
            
        if year == search:
            total_life_expectancy += life_expectancy
            country_count += 1
            
average_life_expectancy = float(total_life_expectancy / country_count)

print(f"\nThe overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_year}\n")

print(f"For the year: {search}\nThe average life expectancy across all countries was {average_life_expectancy}")
print(f"The max life expectancy was in {year_max_country} with {max_year_life_expectancy}")
print(f"The min life expectancy was in {year_min_country} with {min_year_life_expectancy}")