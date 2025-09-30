my_playlist = [
    {'title': 'Vancouver', 'singer': 'BIG Naughty (서동현)'},
    {'title': 'Circle', 'singer': 'Post Malone'},
    {'title': 'Speed Demon', 'singer': 'Justin Bieber'}
]

print("--- My Favorite Playlist ---")

for song in my_playlist:
    # f-string과 딕셔너리의 key를 사용해 '제목 - 가수' 형태로 출력합
    print(f"{song['title']} - {song['singer']}")