class IP_analyzer:

    def __init__(self, log_route):
        self.ip_list = []
        self.log_route = log_route


#outputs and returns a list of unique IPs in a .log file
    def unique_ips(self):
        with open(self.log_route) as log:
            for row in log:
                segmented_row = row.split()
                self.ip_list.append(segmented_row[0])
            print(set(self.ip_list))
            return self.ip_list

#outputs and returns a sorted list with the most concurrent ips in the log file
    def sorted_ips(self):
        self.ips_dict = {}
        with open(self.log_route) as log:
            for row in log:
                segmented_row = row.split()
                ip = segmented_row[0]
                self.ips_dict[ip] = self.ips_dict.get(ip, 0) + 1
            sorted_ips = sorted(self.ips_dict.items(), key = lambda x: x[1], reverse = True)
            print(sorted_ips)
            return sorted_ips


#test_analysis = IP_analyzer("access.log")
#test_analysis.unique_ips()

#test_freq = IP_analyzer("access.log")
#test_freq.sorted_ips()


                

            
