import pandas as pd
import pytest

flights=pd.read_csv("flights.csv")
airports=pd.read_csv("airports.csv")
planes=pd.read_csv("planes.csv")

#*********************************************************************************************************
"""
    :param df: flights.csv
    :return: total number of days does the flights table cover
    :logic: here I combined year, month, day columns and converted to date datatype and found unique
            no. of days from the flights table.
    """
def days(df):
    days_count=pd.to_datetime(df[['year','month','day']]).nunique()
    return days_count

#*********************************************************************************************************

"""
    :param df: flights.csv,airports.csv
    :return: total number of departure cities (not airports) does the flights database cover
    :logic: connecting 
"""
def cities(flights, airports):
    res=list((pd.merge(flights,airports,how='left',left_on='origin',right_on='IATA_CODE')).CITY.unique())
    return res

#*********************************************************************************************************

def relationship(flights, planes):
    """
    Here we are having two columns common between flights and planes tables, which are
    tailnum and year.
    from above two common fields we consider tailnum column as keys in both the table.
    In
    """

    print(planes.shape) # (3322, 9)
    print(planes.tailnum.nunique())  # 3322
    print(flights.shape) # (336776, 16)
    print(flights.tailnum.nunique()) # 4043

    # from the above line we got unique tailnum as 3322 which is actual size of planes table
    # i.e., for unique tailnums from planes table we are having many connections in table flights.
    # therefore we can conclude that there exists 1-many relationship between planes and flights table

    return "one-to-many relationship"

#*********************************************************************************************************

"""
    Here I took tailnum and manufacturer as dictionary into manf
    mapped manf dict with tailnum filed of flights and fetched manufacturer column into manf
    then I created seperate dataframe f3 with manf as index and taking only positive delays and making negative 
        delays as 0 since those -ve values represents early arrival of flight, which is good thing and
        not considered as delay
    finally I grouped on manf and aggregated as sum of delays and sorted in descending order and finally 
        fetched first row only. 
"""
def most_delays_manf(flights):
    manf = dict(list(zip(planes.tailnum, planes.manufacturer)))
    flights['manf']=flights.tailnum.map(manf)
    f3=flights.set_index('manf')[['dep_delay','arr_delay']]
    res=list(((pd.DataFrame((f3.where(f3 > 0, 0)['dep_delay'] + f3.where(f3 > 0, 0)['arr_delay']),
                        columns=['total_delay'])).reset_index()).groupby('manf').total_delay.agg(['sum']).sort_values(
        by='sum', ascending=False).reset_index().loc[0])
    return res


#*********************************************************************************************************

"""
    Here first I concatenated origin and destination then counted values and took combination with maximum
        occurances from the first row
    using the above two origin and dest city code I fetched their city names from airports table  
"""
def two_connected_cities(flights):
    city_codes=(flights.origin + '_' + flights.dest).value_counts().index[0].split('_') # ['JFK', 'LAX']
    res=list(airports[airports['IATA_CODE'].isin(city_codes)]['CITY'])
    return res

#*********************************************************************************************************

if __name__=='__main__':

# 1. how many total number of days does the flights table cover?
    print(days(flights)) # 365

# 2. how many departure cities (not airports) does the flights database cover?
    print(cities(flights,airports)) # ['Newark', 'New York']

# 3. what is the relationship between flights and planes tables?
    print(relationship(flights,planes)) # one-to-many relationship

# 4. which airplane manufacturer incurred the most delays in the analysis period?
    print(most_delays_manf(flights)) # ['EMBRAER', 2589621.0]

# 5. which are the two most connected cities?
    print(two_connected_cities(flights)) # ['New York', 'Los Angeles']