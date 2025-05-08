class BlacklistCheck:

    def __init__(self, blacklist_route):
        self.blacklist = []
        with open(blacklist_route) as blacklist_file:
            for row in blacklist_file:
                self.blacklist.append(row.strip())
            for year in range(1950, 2025):
                self.blacklist.append(str(year))
        self.insecure_passwords = []



    #compares the content of a file with the instance blacklist    
    def checker(self, file_route):

        set_blacklist = set(self.blacklist)
        with open(file_route) as text_file:
            for row in text_file:
                password = row.strip()
                if password in set_blacklist:
                    self.insecure_passwords.append(password)
            if len(self.insecure_passwords) == 0:
                print(f"No insecure passwords in {file_route}")
            else:
                print(self.insecure_passwords)

    #brute force checker for 1950-2025 year of birth passwords
            


chek1 = BlacklistCheck("scripts/Basic/blacklist.txt")
chek1.checker("scripts/Basic/passwords.txt")
        

    