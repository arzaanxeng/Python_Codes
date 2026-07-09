
info = {
    "name" : "Arzaan",
    "Grade": "A",
    "Branch": "Electrical"
}

for key , value in info.items():
    print(f"{key:<10} : {value}")

Failing_Grade = ["F" , "DF"]
print("="*25)
if info["Grade"] in Failing_Grade:
    print("Status : Failed")
else :
    print(f"\nStatus : Passed")

