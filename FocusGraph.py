import matplotlib.pyplot as plt

def focus_graph():
    with open("focus.txt", "r") as file:
        content = file.read()

    content = content.split(",")

    # Filter out empty strings and convert to float
    content = [float(item) for item in content if item.strip()]

    x1 = list(range(len(content)))

    print(content)
    y1 = content

    plt.plot(x1, y1, color="red", marker="o")
    plt.title("YOUR FOCUSED TIME", fontsize=16)
    plt.xlabel("Times", fontsize=14)
    plt.ylabel("Focus Time", fontsize=14)
    plt.grid()
    plt.show()
