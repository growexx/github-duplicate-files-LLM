def load_data(file_path):
    # Simulate loading data from a file
    data = [1, 2, 3, 4, 5]
    return data

def preprocess_data(data):
    # Simulate data preprocessing
    processed_data = [x * 2 for x in data]
    return processed_data

if __name__ == "__main__":
    data = load_data("data.csv")
    processed_data = preprocess_data(data)
    print("Processed Data:", processed_data)
