import csv
import os
import glob
import pandas as pd

# list of headers in csv
LIST_OF_HEADERS = ["Sales($)", "Date", "Region"]


def process_data(num:int, process_writer):
    """
    processes the data in daily_sales_data csvs by watering the csv down to display data for only the pink morsel
    and the process writer ready to write a new csv with processed results
    Args:
        num: the number in the daily sales data name. eg. daily_sales_data_1
        process_writer

    Returns:

    """
    # open the daily sales data csv
    with open(f'data/daily_sales_data_{num}.csv', 'r') as sales_data:
        csv_reader = csv.reader(sales_data, delimiter=",")

        # skip the headings for processing
        next(csv_reader)

        # iterate through rows in the data to format data
        for row in csv_reader:
            if row[0] == "pink morsel":
                row[1] = row[1].replace('$', '0')
                sales = float(row[1]) * float(row[2])
                date = row[3]
                region = row[4]

                process_writer.writerow({"Sales($)": sales, "Date": date, "Region": region})


def processed_sales_generator(nums: list, list_of_headers):
    # open new file to save processed data
    for num in nums:
        num = int(num)
        with open(f'data/processed_sales_{num}.csv', 'a') as processed_sales_data:
            process_writer = csv.DictWriter(processed_sales_data, fieldnames=list_of_headers)
            # write the headers down first in the new csv
            process_writer.writeheader()

            # call the function that processes data and writes the data inside processed_sales_data
            process_data(num, process_writer)


def combine_csvs():
    home = os.getcwd()

    # merging the files
    joined_files = os.path.join(f'{home}', "data\processed_sales*.csv")

    # A list of all joined files is returned
    joined_list = glob.glob(joined_files)

    # # Finally, the files are joined
    big_df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    big_df.to_pickle('data/combined.pkl')

    # Then you can load it back using:
    # big_df = pd.read_pickle('data/combined')
    print(big_df.tail())


