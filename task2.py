from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)

    cats = list()

    if file_path.exists():
        with open(path, "r", encoding='utf-8') as sd:
            lines = [el.strip() for el in sd.readlines()]



            for line in lines:
                cat_data = line.split(',')
                cat = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
                cats.append(cat)

            return cats
        
    else:
        print('Provided path does not exist')

    return cats