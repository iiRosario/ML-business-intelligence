import csv
import os

def read_csv(input_file, rows, year):
    try:
        with open(input_file, 'r', newline='') as csv_in:
            reader = csv.reader(csv_in)
            count = 0
            for row in reader:
                if(count != 0):
                    row.append(year)
                    row[0] = "Liander N.V."
                    row[1] = "LIANDER"
                    row[6] = float(row[6])
                    row[7] = float(row[7])
                    row[8] = float(row[8])
                    row[9] = float(row[9])
                    row[11] = float(row[11])
                    row[12] = float(row[12])
                    row[13] = float(row[13])
                    if(int(row[14]) >= 2011):
                        row.append((int(row[14]) % 2011) + 1)
                    else:
                        row.append("")
                    rows.append(row)
                if(count > 25000):
                    break
                count+=1
            return rows
    except Exception as e:
        print(f"An error occurred while reading CSV: {e}")
        return None

def write_csv(output_file, data):
    try:
        with open(output_file, 'w', newline='') as csv_out:
            writer = csv.writer(csv_out)
            for row in data:
                writer.writerow(row)
        #print("CSV contents written successfully.")
    except Exception as e:
        print(f"An error occurred while writing CSV: {e}")


if __name__ == "__main__":
    input_path = "datasets/energy/Electricity/"
    files = os.listdir(input_path)

    output_path = "all_data.csv"
    csv_data = []
    first_row = ["net_manager","purchase_area","street","zipcode_from","zipcode_to","city",
                 "num_connections","delivery_perc","perc_of_active_connections","type_conn_perc",
                 "type_of_connection","annual_consume","annual_consume_lowtarif_perc",
                 "smartmeter_perc", "year", "weatherid"]
    csv_data.append(first_row)

    for filename in files:
        read_csv(input_path + filename, csv_data, filename.split(".")[0][-4:])
    write_csv(output_path, csv_data)


    
