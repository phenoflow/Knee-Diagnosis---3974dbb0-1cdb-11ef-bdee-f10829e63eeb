# Romi Haas, Ljoudmila Busija, Alexandra Gorelik, Denise A O'Connor, Christopher Pierce, Danielle Mazza, Rochelle Buchbinder, 2024.

import sys, csv, re

codes = [{"code":"241641004.0","system":"snomedct"},{"code":"250102002.0","system":"snomedct"},{"code":"1126007.0","system":"snomedct"},{"code":"81512004.0","system":"snomedct"},{"code":"202413005.0","system":"snomedct"},{"code":"74016001.0","system":"snomedct"},{"code":"249913002.0","system":"snomedct"},{"code":"309566008.0","system":"snomedct"},{"code":"274056002.0","system":"snomedct"},{"code":"30989003.0","system":"snomedct"},{"code":"239832006.0","system":"snomedct"},{"code":"6188005.0","system":"snomedct"},{"code":"63643000.0","system":"snomedct"},{"code":"36701003.0","system":"snomedct"},{"code":"248491001.0","system":"snomedct"},{"code":"22878006.0","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('knee-diagnosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["knee-diagnosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["knee-diagnosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["knee-diagnosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
