import os

input_path = "./"
output_path = "../categorization"
statistics = {}
statistics_skimmed = {}
overall = {}
overall_skimmed = {}

for file_name in ["categorization.txt", "categorization_skimmed.txt", "categorization_overall.txt"]:
    path = os.path.join(output_path, file_name)
    if os.path.exists(path):
        print(f"Removed {file_name}")
        os.remove(path)

for file_name in os.listdir(input_path):
    if file_name.endswith(".txt"):
        with open(os.path.join(input_path, file_name)) as f:
            file_contents = f.read()

        blocks = file_contents.split("\n")

        for block in blocks:
            if block.startswith("error") or block.startswith("warning") or block.startswith("help"):

                if block.startswith("error: aborting due"):
                    continue

                prefix = block.split(":")[0]
                if prefix in overall:
                    overall[prefix] = overall.get(prefix, 0) + 1
                else:
                    overall[prefix] = 1

                if file_name in statistics:
                    statistics[file_name][block] = statistics[file_name].get(
                        block, 0) + 1
                else:
                    statistics[file_name] = {block: 1}

                if block.startswith("error[E0433]") or block.startswith("error[E0658]") or block.startswith("warning:") or block.startswith("help: remove these parentheses"):
                    continue

                if file_name in statistics_skimmed:
                    statistics_skimmed[file_name][block] = statistics_skimmed[file_name].get(
                        block, 0) + 1
                else:
                    statistics_skimmed[file_name] = {block: 1}

                if prefix in overall_skimmed:
                    overall_skimmed[prefix] = overall_skimmed.get(
                        prefix, 0) + 1
                else:
                    overall_skimmed[prefix] = 1

with open(os.path.join(output_path, "categorization.txt"), "w") as f:
    for file_name, file_statistics in statistics.items():
        f.write(file_name + "\n")
        for description, count in file_statistics.items():
            f.write(description + ": " + str(count) + "\n")
        f.write("\n")

"""
Removes:
- error[E0433]: failed to resolve: use of undeclared crate or module `libc`
- error[E0433]: failed to resolve: maybe a missing crate `core`?
- all warning messages
- help messages that relate to styling issues (e.g. removing parentheses)
"""
with open(os.path.join(output_path, "categorization_skimmed.txt"), "w") as f:
    for file_name, file_statistics in statistics_skimmed.items():
        f.write(file_name + "\n")
        for description, count in file_statistics.items():
            f.write(description + ": " + str(count) + "\n")
        f.write("\n")

overall = dict(sorted(overall.items(), key=lambda x: x[1], reverse=True))
overall_skimmed = dict(sorted(overall_skimmed.items(), key=lambda x: x[1], reverse=True))
with open(os.path.join(output_path, "categorization_overall.txt"), "w") as f:
    f.write("Overall\n")
    for error_name, error_count in overall.items():
        f.write(error_name + ": " + str(error_count) + "\n")

    f.write("\nOverall Skimmed\n")
    for error_name, error_count in overall_skimmed.items():
        f.write(error_name + ": " + str(error_count) + "\n")
