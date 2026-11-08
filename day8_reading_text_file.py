file_path="sample_prompt.txt"
try:
    with open(file_path, "r") as f:
        content=f.read()
    print("======file read successfully======")
    print(content)
    print("===================================")

    with open(file_path, "r") as f:
        lines=f.readlines()
    print(f"Total lines in file:{len(lines)}")
    for idx, line in enumerate(lines, 1):
        print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print(f"Error the file '{file_path}' was not found!! ")