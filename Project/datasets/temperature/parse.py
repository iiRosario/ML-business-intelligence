import csv

def parse_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            data.append(row)
    return data

def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        for row in data:
            csv_writer.writerow(row)

if __name__ == "__main__":
    file_path = 'KNMI_20200710.csv'  
    data = parse_csv(file_path)
    

    for line in data[1:]:
        line[1] = line[1][:4]
        #print(line)

    current_year = data[1][1]
    last_year = current_year

    print(current_year)
    

    new_data = []
    new_data.append(data[0])
    i = 1
    while i < len(data[1:]):
        avg_TG = 0
        avg_TN = 0
        avg_TX = 0
        avg_T10N = 0
        avg_SQ = 0
        avg_SP = 0
        avg_Q  = 0
        avg_DR = 0
        avg_UG = 0
        avg_UX = 0
        avg_UN = 0
        count_lines = 0
        while i < len(data[1:]):
            line = data[i]
            current_year = line[1]    
            #print(f"current: {current_year} && last: {last_year}")
            if(current_year == last_year):
                count_lines += 1
                avg_TG += float(line[2])
                avg_TN += float(line[3])
                avg_TX += float(line[4])
                avg_T10N += float(line[5])
                avg_SQ += float(line[6])
                avg_SP += float(line[7])
                avg_Q  += float(line[8])
                avg_DR += float(line[9])
                avg_UG += float(line[10])
                avg_UX += float(line[11])
                avg_UN += float(line[12])
                last_year = current_year
                i+=1
            else:
                avg_TG = round((avg_TG / count_lines) * 0.1, 2)
                avg_TN = round((avg_TN / count_lines) * 0.1, 2)
                avg_TX = round((avg_TX / count_lines) * 0.1, 2)
                avg_T10N = round(avg_T10N / count_lines, 2)
                avg_SQ = round(avg_SQ / count_lines, 2)
                avg_SP = round(avg_SP / count_lines, 2)
                avg_Q  = round(avg_Q / count_lines, 2)
                avg_DR = round(avg_DR / count_lines, 2)
                avg_UG = round(avg_UG / count_lines, 2)
                avg_UX = round(avg_UX / count_lines, 2)
                avg_UN = round(avg_UN / count_lines, 2)
                new_line = [260, last_year, avg_TG, avg_TN, avg_TX, avg_T10N, avg_SQ, avg_SP, avg_Q, avg_DR, avg_UG, avg_UX, avg_UN]
                new_data.append(new_line)
                print(new_line)
                last_year = current_year
                break

    write_to_csv("parsed_data.csv", data)
    write_to_csv("new_data.csv", new_data)