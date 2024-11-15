import pandas as pd

# Task 1: Remove From Output
def task_1(df):
    columns_to_drop = ['Sheet Identifier', 'Asset Class', 'Reason Considered Risk-On',
                    '52-Week High Date', '52-Week Low Date', 'Months Since 52-Week Low', 'Gain from 52W Low']
    df.drop(columns=columns_to_drop, inplace=True)

# Task 2: Remove 200 SMA Sheet from the final Excel Output
def task_2(df):
    df.drop('200 SMA Sheet', axis=1, inplace=True)

# Task 3: Convert to Percentage without Decimals or with 2 Decimals
def task_3(df):
    percentage_columns_without_decimals = ['1-Week Gain', '1-Month Gain', '3-Month Gain', '6-Month Gain', '1-Year Gain', 'Drawdown from 52W High']
    df[percentage_columns_without_decimals] = df[percentage_columns_without_decimals].round(0).astype(int)

    percentage_columns_with_2_decimals = ['200D SMA Slope - This Week', '200D SMA Slope - RoC']
    df[percentage_columns_with_2_decimals] = df[percentage_columns_with_2_decimals].round(2)

# Task 4: Expand Data Retrieval Window to 15 years
def task_4(df):
    # Expand data retrieval window to 15 years (assuming there is a 'High' column containing high prices)
    max_high_5_year = df['High'].rolling(window=5*252).max()  # 252 business days in a year
    max_high_15_year = df['High'].rolling(window=15*252).max()

    # Add new columns to the DataFrame
    df['5Y High Date'] = max_high_5_year
    df['15Y High Date'] = max_high_15_year