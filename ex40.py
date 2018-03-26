class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

skyfall_song = Song(["When the sky falls",
                    "They will crumble",
                    "They will stand tall, togther at Skyfall",
                    "When the sky falls"])

heaven_n_hell = Song(["Sing me a song",
                    "You're a singer",
                    "Bring me along, you're a bringer of evil"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

skyfall_song.sing_me_a_song()

heaven_n_hell.sing_me_a_song()
