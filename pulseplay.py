import streamlit as st
import pandas as pd



# Load dataset
df = pd.read_csv("spotify_tracks.csv")

# Define mood-to-genre mapping
mood_genres = {
    "Chill": ["acoustic", "chill", "ambient", "indie", "lo-fi"],
    "Happy": ["pop", "dance", "funk", "soul", "reggae"],
    "Energetic": ["edm", "electronic", "rock", "metal", "house", "techno"],
    "Romantic": ["rnb", "soul", "acoustic", "ballad"],
    "Sad": ["acoustic", "indie", "blues", "piano", "soft-rock"],
    "Party": ["hip hop", "trap", "edm", "reggaeton", "pop"],
    "Focus": ["classical", "instrumental", "ambient", "lo-fi", "piano"]
}

# Define function for recommendations
def recommend_music(mood, num_recommendations=5):
    possible_genres = mood_genres.get(mood, [])
    mood_tracks = df[df['genre'].str.lower().isin(possible_genres)]
    recommendations = mood_tracks.sort_values(by="popularity", ascending=False).head(20)
    if len(recommendations) > num_recommendations:
        return recommendations.sample(num_recommendations)
    return recommendations

# Streamlit UI
st.title(":orange[PulsePlay]: Your Mood-Based Music Recommendation App")
st.write("Select your current mood and get music recommendations tailored to that vibe!")

# Sidebar for additional controls
st.sidebar.title("About")
st.sidebar.write("PulsePlay is a music recommendation app that suggests tracks based on your current mood."
                 " Simply select your mood from the dropdown menu, and we'll provide you with a list of songs"
                 " that match your vibe.")

# Mood and recommendation number selection
mood = st.selectbox("What's your mood today?", list(mood_genres.keys()))
top_k = st.sidebar.number_input("Select number of recommendations (Top K)", min_value=1, max_value=20, value=5)

# Get recommendations
recommended_tracks = recommend_music(mood, num_recommendations=top_k)

# Display recommendations
st.subheader(f"Top {top_k} Recommendations for a {mood} mood")
for idx, row in recommended_tracks.iterrows():
    st.markdown(f"**{row['name']}** by *{row['artists']}* (Genre: {row['genre']})")


