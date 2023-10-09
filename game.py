import random
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

def preprocess():
	# Load the dataset from a CSV file
	data = pd.read_csv("your_dataset.csv")

	# Handle missing values
	imputer = SimpleImputer(strategy="mean")
	data["column_with_missing_values"] = imputer.fit_transform(data[["column_with_missing_values"]])

	# Encode categorical variables
	encoder = LabelEncoder()
	data["categorical_column"] = encoder.fit_transform(data["categorical_column"])

	# Standardize numerical features
	scaler = StandardScaler()
	data[["numerical_feature_1", "numerical_feature_2"]] = scaler.fit_transform(data[["numerical_feature_1", "numerical_feature_2"]])

	# Other preprocessing tasks can be added here as needed

	# Save the preprocessed data to a new CSV file
	data.to_csv("preprocessed_dataset.csv", index=False)


def guess_the_number():
    print("Welcome to Guess the Number!")
    player_name = input("Enter your name: ")

    high_scores = {}
    try:
        with open("high_scores.txt", "r") as f:
            for line in f:
                name, score = line.strip().split(":")
                high_scores[name] = int(score)
    except FileNotFoundError:
        pass

    while True:
        print("Choose a difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-200)")
        print("4. Custom")
        choice = input("Enter the level number (1/2/3/4): ")
        
        if choice == '1':
            max_number = 50
        elif choice == '2':
            max_number = 100
        elif choice == '3':
            max_number = 200
        elif choice == '4':
            max_number = int(input("Enter the maximum number for the custom range: "))
        else:
            print("Invalid choice. Please select a valid level.")
            continue

        secret_number = random.randint(1, max_number)
        attempts = 0
        max_attempts = 7

        while attempts < max_attempts:
            try:
                guess = int(input(f"Guess the number (1-{max_number}): "))
                attempts += 1

                if guess < secret_number:
                    print("Higher! Try again.")
                elif guess > secret_number:
                    print("Lower! Try again.")
                else:
                    print(f"Congratulations, {player_name}! You guessed the number in {attempts} attempts.")
                    if player_name not in high_scores or attempts < high_scores[player_name]:
                        high_scores[player_name] = attempts
                        with open("high_scores.txt", "w") as f:
                            for name, score in high_scores.items():
                                f.write(f"{name}:{score}\n")
                        print("New High Score!")

                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if attempts >= max_attempts:
            print(f"Sorry, {player_name}, you've reached the maximum number of attempts. The secret number was {secret_number}.")

        print("Leaderboard - Top 5:")
        sorted_scores = sorted(high_scores.items(), key=lambda x: x[1])[:5]
        for i, (name, score) in enumerate(sorted_scores):
            print(f"{i + 1}. {name}: {score} attempts")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    guess_the_number()

