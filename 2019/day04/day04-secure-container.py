#!/usr/bin/env python

import re

# input: 128392-643281

valid_pw_part1 = []
def is_valid_password(pw):
    pw = str(pw)
    validation = ""
    for i in range(len(pw)-1):
        if pw[i+1] < pw[i]:
            return False
    for i in range(len(pw)-1):
        if pw[i] == pw[i+1]:
            validation += "1"
            break
    if validation == "1":
        valid_pw_part1.append(int(pw))
        return True
    else:
        return False

cnt1 = 0
for password in range(128392,643281):
    if is_valid_password(password):
        cnt1 += 1

print("In the range 128392-643281, there are", cnt1, "valid passwords for part 1.")

# Copy the list because the solution for part 2 is a subset:
valid_pw_part2 = valid_pw_part1[:]

def is_valid_password2(pw):
    # use negative look-behind=?<! and look-ahead=?!
    # https://stackoverflow.com/a/14163475/12155532
    for i in range(10):
        if bool(re.search(r"(?<!%s)%s%s(?!%s)" %(i, i, i, i), str(pw))):
            return True
    return False


cnt2 = 0
for password in valid_pw_part2:
    if is_valid_password2(password):
        cnt2 += 1

print("In the range 128392-643281, there are", cnt2, "valid passwords for part 2.")


### DEBUG OUTPUT
#print(is_valid_password2(135679), "False")
#print(is_valid_password2(223450), "False")
#print(is_valid_password2(123789), "False")
#print(is_valid_password2(111123), "False")
#print(is_valid_password2(111111), "False")
#print(is_valid_password2(122345), "True")
#print(is_valid_password2(112233), "True")
#print(is_valid_password2(111122), "True")



