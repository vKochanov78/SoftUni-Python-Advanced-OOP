import os


def save_extensions(dir_name):
    extensions = {}

    for filename in os.listdir(dir_name):
        ext = filename.split('.')[1]  # ext -> Extension
        ext = '.' + ext

        if ext not in extensions:
            extensions[ext] = []
        extensions[ext].append(filename)

    return sorted(extensions.items(), key=lambda x: (x, x[1]))


def report_files(data):
    with open("report.txt", "w") as file:

        for key, items in data:
            file.write(f"\nFound files for ( {key} ) extension -> ({len(items)}):\n")
            for item in items:
                file.write(f"- - - > {item}\n")

    with open("report.txt", "r") as file:
        data = file.readlines()
    with open("report.txt", "w") as file:
        file.writelines(data[1:])

    print("\nCheck report.txt for the found content.")


directory = input(
    "You should enter - > ./docs\n"
    "Desired directory to search: "
)
result = save_extensions(directory)
report = report_files(result)