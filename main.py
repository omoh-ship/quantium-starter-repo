import csv


def process_data(num:int, process_writer):
    """
    processes the data in daily_slaes_data csvs
    Args:
        num: the number in the daily sales data name. eg. daily_sales_data_1

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


def main(num:int):
    # list of headers in csv
    list_of_headers = ["Sales($)", "Date", "Region"]

    # open new file to save processed data
    with open(f'data/processed_sales_{num}.csv', 'a') as processed_sales_data:
        process_writer = csv.DictWriter(processed_sales_data, fieldnames=list_of_headers)
        process_writer.writeheader()

        # call the function that processes data
        process_data(num, process_writer)


if __name__ == '__main__':
    main(0)
    main(1)
    main(2)
