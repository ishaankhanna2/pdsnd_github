import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    --20220320 update:
    This command is essential for narrowing/filtering down the data set that we are analyzing for efficiency for runtime and efficiency (Ishaan)
    --

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (city not in CITY_DATA.keys()):
        city = input("What city would you like to view data for: ")
        city = city.lower()
        if city not in CITY_DATA.keys():
            print('\nThe city title that you inputted is invalid. Please retry\n')
    filter_list = ['month','day of the week','all']
    typeoffilter = ''
    while (typeoffilter not in filter_list):
        typeoffilter = input("Would you like to filter your dataset by month, day of the week, or consider all records(type 'all' if you want to consider all)?\n")
        typeoffilter = typeoffilter.lower()
        if typeoffilter not in filter_list:
            print('\nThe input you gave is invalid. Acceptable inputs include: "month", "day of the week" & "all". Please retry\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    if typeoffilter == 'month':
        month_list = ['january','february','march','april','may','june']
        month = ''
        while (month not in month_list):
            month = input("What month would you like to filter on: January, February, March, April, May, or June?")
            month = month.lower()
            day = 'all'


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if typeoffilter == 'day of the week':
        day = input("What day of the week would you like to filter on: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
        day = day.lower()
        month = 'all'
    if typeoffilter == 'all':
        month = 'all'
        day = 'all'
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Frequent Month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('Most Frequent Day of the week: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    print('Most Frequent Start Station:', popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    print('Most Frequent End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + df['End Station']
    popular_route = df['route'].mode()[0]

    print('Most Frequent Route:', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel_time = sum(df['Trip Duration'])
    print('The total trip duration of all trips is: ', tot_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = np.mean(df['Trip Duration'])
    print('The average trip duration of all trips is: ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = pd.value_counts(df['User Type'])
    print(user_types)
    if len(df.columns) == 9:

    # TO DO: Display counts of gender
        gender_types = pd.value_counts(df['Gender'])
        print(gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_yr = int(min(df['Birth Year']))
        print('The earliest year of birth is: ', earliest_yr)

        most_recent_yr = int(max(df['Birth Year']))
        print('The most recent year of birth is: ', most_recent_yr)

        most_common_yr = int(df['Birth Year'].mode()[0])
        print('The most common year of birth is: ', most_common_yr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def rawdataoutput(df):
    dataoutput = ['yes', 'no']
    counter = 0
    fiverowsofdata = input("Would you like to output the first five rows of data?. Please answer 'Yes' or 'No'")
    fiverowsofdata = fiverowsofdata.lower()
    while fiverowsofdata not in dataoutput:
        print('Entry is invalid. Please type "Yes" or "No"')
        fiverowsofdata = input("Would you like to output the first five rows of data?. Please answer 'Yes' or 'No'")
        fiverowsofdata = fiverowsofdata.lower()
    print(df.head())
    while fiverowsofdata == 'yes':
        fiverowsofdata = input("Would you like to output five more rows of data?. Please answer 'Yes' or 'No'")
        while fiverowsofdata not in dataoutput:
            print('Entry is invalid. Please type "Yes" or "No"')
            fiverowsofdata = input("Would you like to output the first five rows of data?. Please answer 'Yes' or 'No'")
            fiverowsofdata = fiverowsofdata.lower()
        counter += 5
        print(df[counter:counter + 5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdataoutput(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
