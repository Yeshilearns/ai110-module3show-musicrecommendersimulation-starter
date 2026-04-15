"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")
  
    profiles = [
        {"name": "High-Energy Pop", "prefs": {"genre": "pop", "mood": "happy", "energy": 0.9}},
        {"name": "Chill Lofi", "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.3}},
        {"name": "Intense Rock", "prefs": {"genre": "rock", "mood": "intense", "energy": 0.9}},
        {"name": "Conflicting Preferences", "prefs": {"genre": "pop", "mood": "sad", "energy": 0.9}}
    ]
    for profile in profiles:
        print(f"\n=== {profile['name']} ===\n")

        recommendations = recommend_songs(profile["prefs"], songs, k=5)
        
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print("-" * 30)
            print()


if __name__ == "__main__":
    main()
