def insert_lines_markdown(file_path, dest_path, lines, mark):
    mark_idx = -1
    
    with open(file_path, "r") as f:
        old_lines = f.readlines()
    
    for (idx, old_line) in enumerate(old_lines):
        if old_line.startswith("<!-- {} -->".format(mark)):
            mark_idx = idx
    
    if mark_idx == -1:
        return
    
    old_lines[mark_idx + 1: mark_idx + 1] = lines

    with open(dest_path, "w") as f:
        f.write("".join(old_lines))