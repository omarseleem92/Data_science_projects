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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
                try:
                    city=(input("Please enter a city (chicago, new york city, washington)\n")).lower()
                    if city not in ["chicago","new york city","washington"]:
                        print("You entered a wrong city name \n")
                        continue
                except:
                    print("Please enter a correct city name (chicago, new york city, washington)\n")
                    continue
                else:
                    # Input is correct
                    # we are ready to exit the loop.
                    break



    # get user input for month (all, january, february, ... , june)
    while True:
                try:
                       month=input("Please enter a month (january,february,march,..)\n")
                       if month not in ["january","february","march","april","may", "june","all"]:
                            print("You entered a wrong month")
                            continue
                except:
                        print("Sorry, Please enter a correct month")

                else:
                    # Input is correct
                    # we are ready to exit the loop.
                    break


    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
                try:
                    day=(input("Please enter a day as an integer (1,2,3,.., or all for a complete month)\n"))
                    a=list(range(1,32))
                    day_list=[]
                    for item in a:
                        day_list.append(str(item))
                    day_list.append("all")
                    if day not in day_list:
                        print("you entered a wrong day\n")
                        continue
                    if day !="all":
                        day=int(day)



                except:
                    print("Sorry, Please enter a correct day\n")

                else:
                    # Input is correct
                    # we are ready to exit the loop.
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

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
        df = df[df['day'] == day]


    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # extract start hour from Start Time to create new columns

    df['hour'] =df['Start Time'].dt.hour

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("The most common month is",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day'].value_counts().idxmax()
    print("The most common  day is",popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station is" , common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station is" , common_end_station)

    # display most frequent combination of start station and end station trip
    common_combination=df.groupby(['Start Station','End Station']).size().nlargest(1)
    print("Most frequent combination of start station and end station trip\n" , common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("Total Travel Time is", total_travel_time)

    # display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("Mean Travel Time is", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print("user_types:")
    print(user_types)

    if "Gender" in list(df):

        # Display counts of gender
        user_gender = df['Gender'].value_counts()

        print("Gender Counts:")
        print(user_gender)
    else:
        print("There is no Gender data")

    # Display earliest, most recent, and most common year of birth

    if "Birth Year" in list(df):

        # Earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest year of birth is",earliest_birth_year)

        # Most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        print("Most recent year of birth is",most_recent_birth_year)


        # Most common year of Birth
        common_birth_year = df['Birth Year'].value_counts()
        print("Most common year of birth is",common_birth_year.idxmax())

    else:
        print("There is no Birth year data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
        start_loc = 0
        while True:
            try:
                view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
                if view_data not in ["yes", "no"]:
                    print("You entered {}, please enter yes or no".format(view_data))
                    continue
                if view_data=="yes":
                        print(df.iloc[start_loc:start_loc+5])
                        start_loc += 5
                        view_data = input("Do you wish to continue?: ").lower()
                        continue
            except:
                print("Please enter yes or no")
            else:
                # input is true
                break





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
