def input_to_list(count: int):
    lines = []
    for _ in range(count):
        lines.append(input().split())
    return lines


def unique_chemical(elements):
    unique_elements = set()
    for el in elements:
        for element in el:
            unique_elements.add(element)
    return unique_elements


chemical_elements = input_to_list(int(input()))
chemical_compounds = unique_chemical(chemical_elements)
print(*[x for x in chemical_compounds], sep='\n')