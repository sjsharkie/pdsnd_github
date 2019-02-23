## See read_me.txt in workspace for more information ##
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = input("Let's Explore a City, Please select Chicago (ch), Washington (dc) or New York City (ny)").lower()
    if city == 'ch':
        print("Chicago")
        city = 'chicago'
    if city == 'dc':
        print("Washington")
        city = 'washington'
    if city == 'ny':
        print("New York City")
        city = 'new york city'
    while city not in CITY_DATA:
        city = input("Sorry please select: ch, dc, ny")
        if city == 'ch':
            print("Chicago")
            city = 'chicago'
        if city == 'dc':
            print("Washington")
            city = 'washington'
        if city == 'ny':
            print("New York City")
            city = 'new york city'

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Pick a Month by entering a number: January (1), February (2), March (3), April (4), May (5), June (6), All (7)")
    if month == '1':
        print("January")
        month = 'january'
    if month == '2':
        print("February")
        month = 'february'
    if month == '3':
        print("March")
        month = 'march'
    if month == '4':
        print("April")
        month = 'april'
    if month == '5':
        print("May")
        month = 'may'
    if month == '6':
        print("June")
        month = 'june'
    if month == '7':
        print("All Months")
        month = 'all'
    while month not in MONTH_LIST:
        month = input("Sorry please select a number 1 to 6 for January to June (7 for All)")
        if month == '1':
            print("January")
            month = 'january'
        if month == '2':
            print("February")
            month = 'february'
        if month == '3':
            print("March")
            month = 'march'
        if month == '4':
            print("April")
            month = 'april'
        if month == '5':
            print("May")
            month = 'may'
        if month == '6':
            print("June")
            month = 'june'
        if month == '7':
            print("All Months")
            month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Pick a day: Monday (1), Tuesday (2), Wednesday (3), Thursday (4), Friday (5), Saturday (6), Sunday (7), or All (8)")
    if day == '1':
        print("Monday")
        day = 'monday'
    if day == '2':
        print("Tuesday")
        day = 'tuesday'
    if day == '3':
        print("Wednesday")
        day = 'wednesday'
    if day == '4':
        print("Thursday")
        day = 'thursday'
    if day == '5':
        print("Friday")
        day = 'friday'
    if day == '6':
        print("Saturday")
        day = 'saturday'
    if day == '7':
        print("Sunday")
        day = 'sunday'
    if day == '8':
        print("All")
        day = 'all'
    while day not in DAY_LIST:
        day = input("Sorry please select a number 1 to 8")
        if day == '1':
            print("Monday")
            day = 'monday'
        if day == '2':
            print("Tuesday")
            day = 'tuesday'
        if day == '3':
            print("Wednesday")
            day = 'wednesday'
        if day == '4':
            print("Thursday")
            day = 'thursday'
        if day == '5':
            print("Friday")
            day = 'friday'
        if day == '6':
            print("Saturday")
            day = 'saturday'
        if day == '7':
            print("Sunday")
            day = 'sunday'
        if day == '8':
            print("All")
            day = 'all'
    print("The city: " + city)
    print("The month: " + month)
    print("The day: " + day) 
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name  
    if month != 'all':  
        month = MONTH_LIST.index(month)
        df = df.loc[df['month'] == month]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mode_month = df['month'].mode()[0]
    print('The most common month: ', mode_month)

    # TO DO: display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('The most common day: ', mode_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mode_hour = df['hour'].mode()[0]
    print('Most Common Hour:', mode_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start = df['Start Station'].value_counts().idxmax()
    print('The most common start station: ', mode_start)

    # TO DO: display most commonly used end station
    mode_end = df['End Station'].value_counts().idxmax()
    print('The most common end station: ', mode_end)

    # TO DO: display most frequent combination of start station and end station trip
    mode_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most common trip: ', mode_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = sum(df['Trip Duration'])
    print('Total travel time: ', total_travel/3600, "hours")

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel/3600, "hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df["Gender"].value_counts()
        print('\n', gender, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df["Birth Year"]
        print('The earliest birthyear: ' +str(int(birth_year.min())))
        print('The most recent birthyear: ' +str(int(birth_year.max())))
        print('The most common birthyear: ' +str(int(birth_year.mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def five_rows(df):
    again = 'yes'
    i = 0
    while True:
        again = input('\nWould you like to see five rows of data? Enter yes or no.\n')
        print(df.iloc[i:i+5, :])
        i = i + 5
        if again.lower() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        five_rows(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
## See read_me.txt also in workspace for more information ##