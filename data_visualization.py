import matplotlib.pyplot as plt

def visualize_data(data):
    # Simulate data visualization
    plt.plot(data)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Data Visualization")
    plt.show()

if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    visualize_data(data)
