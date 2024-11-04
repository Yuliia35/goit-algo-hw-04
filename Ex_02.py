from pathlib import Path as File_cat


def get_cats_info(path):
    cats = []
    try:
        with open (path, "r", encoding="utf-8") as File_cat:
            for line in File_cat:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(",")
                    cat_info = {'id':cat_id, 'name':name,'age':age}
                    cats.append(cat_info)
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
    except ValueError:
        print(f"Error: The was an issue with the data format in the file.")
    return cats


cats_info = get_cats_info("C:\Projects/File_cat.txt")
print(cats_info)