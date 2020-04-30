import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to filter the data by: chicago, new york city, or washington? ').lower()
        if city not in ("chicago", "new york city", "washington"):
            print("Please choose one of the three cities mentioned above.")
            continue
        else:
                break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which day of the month would you like to filter by: all, january, february, march, april, may, june, july, august, september, october, november, december: ").lower()
        if month not in ("all", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
            print("Please choose one of the selections using the right format.")
            continue
        else:
            break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day of the week would you like to filter by: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday: ").lower()
        if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            print("Please choose one of the days of the week or all days of the week with the proper format. ")
            continue
        else:
            break
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
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november', 'december']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
        # filter by day of week if applicable
        if day != 'all':
            # filter by day of week to create the new dataframe
            f = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month:", common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week:", common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start = df['hour'].mode()[0]
    print("The most common start hour:", common_start)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_station = df['Start Station'].mode()[0]
    print('The most common starting station:', common_station)
    
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common ending station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    combine_stations = df['Start Station'] + "*" + df['End Station']
    common_station = combine_stations.value_counts().idxmax()
    print('Most frequent used combinations are:\n{} \nto\n{}'.format(common_station.split('*')[0], common_station.split('*')[1]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    start_time = time.time()
    total_travel = sum(df['Trip Duration'])
    print('The total travel time is:', total_travel/86400, 'days.')

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('The average travel time is:', mean_travel/60, 'minutes.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts(dropna=False)
    print('The following are the user count:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('These are the gender counts:\n', gender)
    except KeyError:
        print('There is no gender types supported with this selection.')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_year = df['Birth Year'].min()
        print('The earliest year is:', early_year)
    except KeyError:
        print('The earliest year is not available for this month.')
    try:
        most_recent = df['Birth Year'].max()
        print('The most recent year is:', most_recent)
    except KeyError:
        print('Most recent year is not available for this month.')

    try:
        most_common = df['Birth Year'].mode()[0]
        print('Most common year is:', most_common)
    except KeyError:
        print('There is not a most common year for this month.')
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_view(df):
    """Ask if the user wants to see raw data with 5 rows at a time"""
    raw_count = 0
    show_raw = input('Do you wan to see five lines of raw data? Enter yes or no.\n ').lower()
    while True:
        if show_raw == 'yes':
            print (df.iloc[raw_count : raw_count + 5])
            raw_count += 5
            show_raw = input('Would you like to see five more linees? Enter yes or no. ').lower()
            continue
        else:
            break
        

                       
                  

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_view(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
