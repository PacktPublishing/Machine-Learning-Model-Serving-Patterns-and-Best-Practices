import os

def update_model():
    if os.path.exists("train_directory/data.csv"):
        data = open("train_directory/data.csv", "r")
        print("Training the model with new data")
        os.remove("train_directory/data.csv")
        print("File deleted after training")
    else:
        print("No new data to train")

def create_file():
    file = open("train_directory/data.csv", "w")
    file.write("X, Y\n")
    file.write("100, 1\n")
    file.write("200, 2\n")


if __name__ == "__main__":
    create_file()
    # update_model()
