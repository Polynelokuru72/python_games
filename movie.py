import pandas as pd
from surprise import SVD, Reader, Dataset
from surprise.model_selection import train_test_split
from surprise import accuracy
import matplotlib.pyplot as plt

# Step 1: Load MovieLens dataset (using Surprise's built-in loader)
# MovieLens 100k dataset can be used, it's available within Surprise

# Define the reader format for the MovieLens dataset (user, movie, rating, timestamp)
reader = Reader(line_format='user item rating timestamp', sep='\t')

# Load the dataset
data = Dataset.load_builtin('ml-100k')

# Step 2: Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Step 3: Train the model using Singular Value Decomposition (SVD)
model = SVD()
model.fit(trainset)

# Step 4: Make predictions on the testset
predictions = model.test(testset)

# Step 5: Evaluate the model's performance using RMSE
rmse = accuracy.rmse(predictions)
print(f"RMSE: {rmse}")

# Step 6: Optionally, we can visualize the distribution of errors (residuals)
errors = [predicted_rating - actual_rating for (_, _, actual_rating, _, predicted_rating) in predictions]
plt.hist(errors, bins=50)
plt.title('Distribution of Errors (Residuals)')
plt.xlabel('Error')
plt.ylabel('Frequency')
plt.show()

# Step 7: Making a recommendation for a specific user
# Let's say we want to recommend a movie to user 1
user_id = 1
movie_id = 50  # Example movie ID

# Predict the rating that user 1 would give to movie 50
predicted_rating = model.predict(user_id, movie_id)
print(f"Predicted rating for User {user_id} on Movie {movie_id}: {predicted_rating.est}")
