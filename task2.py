def get_cats_info(path):
    with open(path, "r") as sd:
        lines = [el.strip() for el in sd.readlines()]

        cats = list()

        for line in lines:
            cat_data = line.split(',')
            cat = {"id": cat_data[0], "name": cat_data[1], "age": cat_data[2]}
            cats.append(cat)

        return cats