import matplotlib.pyplot as plt
import os

accuracy_before = [0.82, 0.81, 0.80]
accuracy_after = [0.82, 0.88, 0.90]

plt.plot(accuracy_before)
plt.plot(accuracy_after)
plt.xlabel("Time")
plt.ylabel("Accuracy")
plt.title("Federated HeartCare Performance")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(BASE_DIR, "webapp/static/performance.png")

plt.savefig(IMG_PATH)
plt.close()

print("✔ Performance graph updated")
