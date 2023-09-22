import typing
from enum import Enum, auto

class CertificateOptions(Enum):
    دكتوراة = 0
    ماجستير = 1
    بكالوريوس = 2
    دبلوم = 3
    ثانوية_صناعية_تجارية = 4
    ثانوية_عامة = 5
    اعدادية = 6
    ابتدائية = 7
    بدون_مؤهل = 8

# Printing the enum members and their indices
for option in CertificateOptions:
    print(f"{option.name}: {option.value}")


print(CertificateOptions.دكتوراة.value)
