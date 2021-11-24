def vowel_filter(function):
    def wrapper():
        text = function()
        filtered = [x for x in text if x.lower() in 'aeiouy']
        return filtered
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
