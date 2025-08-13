class Album:
    # initalise ablum_name, number_of_songs, album_artist
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    # __str__ method that returns a string
    def __str__(self):
        return (
            f"{self.album_name}, {self.album_artist}, {self.number_of_songs}"
        )
    # Sorting according to the number of songs

    @staticmethod
    def bubble_sort(albums):
        n = len(albums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if albums[j].number_of_songs > albums[j + 1].number_of_songs:
                    albums[j], albums[j + 1] = albums[j + 1], albums[j]
        return albums


def swap_list(items):
    swap = len(album1)
    for i in range(swap):
        album1[0], album1[2] = album1[2], album1[0]
    return items


# Create an empty list
album1 = [
    Album("Testify", 22, "Mmuso Worship"),
    Album("Jesus to the city", 16, "Mmuso Worship"),
    Album("KOA", 18, "Kabza De Small"),
    Album("Aluta Continua", 12, "Babalwa M"),
    Album("Ivy League", 21, "Kelvin Momo"),
]

# Correctly call the static method using the class name
sorted_list = Album.bubble_sort(album1)

for album in sorted_list:
    print(album)

print("\n")

swapped_list = swap_list(sorted_list)

for swap in swapped_list:
    print(swap)

# Create a new list
album2 = []

new_songs = [
    Album("Dark Side of the Moon", "Pink Floyd", 9),
    Album("Oops!... I Did It Again", "Britney Spears", 16)
]
# Add 5 albums from albums1
album2.append(album1)
new_1 = album2.append(new_songs)

print("\n")

print(album2)