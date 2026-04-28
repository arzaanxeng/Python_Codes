"""
You are building an internal tool for “Innova-Tech HR.” The company needs to quickly
ingest employee profiles (IDs, names, and technical skills) and then search that database
to assemble a “Dream Team” for upcoming client projects based on required skills.
You are provided with raw data pulled from an old HR system. It is a list of strings
formatted as "EMP_ID|Name|Skill1,Skill2,Skill3".
Input Data:
raw_data = [
"E101|Alice Smith|Python,SQL,AWS",
"E102|Bob Jones|Java,Spring,SQL",
"E103|Charlie Day|Python,React,NodeJS",
"E104|Diana Prince|AWS,Docker,Kubernetes"
]
Target Structure: {"E101": {"name": "Alice Smith", "skills": ["Python", "SQL", "AWS"]}}
Return the populated roster dictionary.

Now that you have a searchable database, you need to find employees for a new project.
If no employees have the skill, append the string "No staff available for this skill." to the
list.
Return the capable_staff list.
Overall Flow Required:
1. Call build_database(raw_data) and store the result in a variable called company_db.
2. Set up a while True loop to act as the user interface.
• Ask the HR manager: "Enter a required skill to search for (or QUIT): "
• If they type quit, break the loop.
• Call your find_engineers() function, passing in your company_db and the user's input.
• Use a for loop to print out the names of the available engineers nicely formatted.
"""

raw_data = [
    "E101|Alice Smith|Python,SQL,AWS",
    "E102|Bob Jones|Java,Spring,SQL",
    "E103|Charlie Day|Python,React,NodeJS",
    "E104|Diana Prince|AWS,Docker,Kubernetes",
    "E105|Diana Walker|Python,Docker,Java",
    "E106|James Andrew|AWS,SQL,Kubernetes",
]


def build_database(raw_data):
    roster = {}
    for entry in raw_data:
        parts = entry.split("|")
        if len(parts) != 3:
            continue

        emp_id, name, skills_string = parts

        skills = [skill.strip().lower() for skill in skills_string.split(",")]
        roster[emp_id] = {"name": name, "skills": skills}
    return roster


def find_engineers(company_db, required_skill):
    capable_staff = []
    required_skill = required_skill.lower()

    for emp_id, info in company_db.items():
        if required_skill in info["skills"]:
            capable_staff.append(info["name"])
    if not capable_staff:
        capable_staff.append("No staff available for this skill.")

    return capable_staff


def main():
    company_db = build_database(raw_data)
    while True:
        user_input = input("\nEnter a required skill to search for (or QUIT): ").strip()

        if user_input.lower() == "quit":
            print("Exiting HR Tool. Good luck with your project!")
            break

        # 3. Search and Display
        results = find_engineers(company_db, user_input)

        print(f"\n==== Search Results for '{user_input}' ====")

        for person in results:
            print(f"- {person}")

if __name__ == "__main__":
    main()