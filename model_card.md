# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
VibeMatch Recommender

---

## 2. Intended Use   

This recommender suggests songs based on user preferences like genre, mood, and energy. It assumes users can describe their music taste using these features. This system is designed for classroom learning to understand how recommendation systems work, not for real-world deployment.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Each song has features such as genre, mood, and energy. The user provides their preferred genre, mood, and target energy level. The system compares each song to the user’s preferences and assigns a score. Songs that match the genre or mood get extra points, and songs with energy levels closer to the user’s target receive higher scores. The system then ranks all songs based on their scores and returns the top recommendations.


---

## 4. Data  

The dataset contains around 20 songs with different genres such as pop, lofi, rock, and ambient. Each song includes features like energy, tempo, valence, danceability, and acousticness. I added additional songs to increase variety. However, the dataset is still small and does not represent all types of music or user preferences.

---

## 5. Strengths  

The system works well when user preferences are clear and consistent. For example, profiles like Chill Lofi and Intense Rock produced recommendations that matched the expected vibe. The scoring logic captures energy similarity effectively and provides reasonable results in most cases.

---

## 6. Limitations and Bias 

One limitation I noticed is that the system heavily depends on how the scoring weights are set. For example, when genre had a higher weight, the recommender mostly returned songs from the same genre, even if other features didn’t match well. After increasing the importance of energy, the system started prioritizing songs with similar energy levels, even if the genre was different. This shows that the recommender can be biased toward certain features depending on how the scoring is designed. It also struggled with conflicting preferences, where it didn’t always balance mood, genre, and energy properly.
---

## 7. Evaluation  

I tested the system using multiple user profiles, including High-Energy Pop, Chill Lofi, Intense Rock, and a conflicting preferences profile. I compared how the top recommendations changed based on different inputs and checked whether the results matched the expected vibe.

For profiles like Chill Lofi and Intense Rock, the recommendations felt accurate and aligned with the user’s preferences. However, for the conflicting preferences profile (pop, sad, high energy), the system mostly returned high-energy pop songs instead of sad songs. This showed that the system prioritizes genre and energy more than mood.

I also tested a weight change experiment, where I increased the importance of energy and reduced the importance of genre. This caused the system to favor songs with similar energy even more, sometimes ignoring genre completely. This confirmed that the recommender is very sensitive to how features are weighted.
---

## 8. Future Work  

In the future, I would improve the system by adding more features and a larger dataset. I would also explore better ways to balance multiple preferences instead of relying on fixed weights. Another improvement would be making the recommendations more diverse and improving how explanations are generated.
---

## 9. Personal Reflection  

This project helped me understand how recommendation systems actually work behind the scenes. I realized that even simple scoring rules can produce useful results, but small changes in weights can significantly affect the outcome. One interesting thing I noticed was how the system handled conflicting preferences, which made me think about how real apps sometimes recommend things that don’t fully match what I want.