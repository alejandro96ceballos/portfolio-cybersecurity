class Password_analyzer:
    #checks for common vulnerabilities of passwords
    def weakness_analyzer(self, file_route, blacklist_route):
        with open(blacklist_route) as blacklist:
            blacklist_set = set(line.strip() for line in blacklist)
        with open(file_route) as password_file:
            with open("output.txt", "a") as output:
                for row in password_file:
                    reasons = []
                    clean_row = row.strip()
                    if clean_row.isdigit():
                        reasons.append("only contains numbers")
                    if len(clean_row) <= 8:
                        reasons.append("is 8 or less characters")
                    if clean_row.lower() == clean_row:
                        reasons.append("is only written in lower characters")
                    if clean_row.isalnum():
                        reasons.append("It does not contain any symbols")
                    if clean_row in blacklist_set:
                        reasons.append("It appears in compromised passwords files")
                    
                    if len(reasons) == 0:
                        output.write(f"The password {clean_row} is safe")
                    if len(reasons) != 0:
                        reasons_string = ", ".join(reasons)
                        output.write(f"The password {clean_row} is not safe because {reasons_string}\n")

analysis = Password_analyzer()
analysis.weakness_analyzer("users_passwords.txt", "compromised_passwords.txt")
