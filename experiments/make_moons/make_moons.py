# PLEASE NOTE THAT THE CODE TO DISPLAY THE RESULTS 
# IS NOT PART OF THE GBC ALGORITHM AND IS MADE BY AI. 
# I WILL MAKE IT MYSELF IN THE FUTURE.
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.cluster import KMeans

# ============================================================
# 1. CONFIGURATION
# ============================================================
N_SAMPLES = 500
NOISE = 0.15
PURITY_THRESHOLD = 0.95

RANDOM_STATE = 42
MIN_CHILD_SIZE = 1
MAX_DEPTH = 100

CLASS_COLOURS = {0: "red", 1: "blue"}

# ============================================================
# 2. GENERATE DATASET
# ============================================================
X, y = make_moons(
    n_samples=N_SAMPLES,
    noise=NOISE,
    random_state=RANDOM_STATE
)

# ============================================================
# 3. CALCULATE GRANULAR BALL PROPERTIES
# ============================================================
def calculate_ball(indices):
    """
    Calculate the properties of a granular ball.

    Returns:
        centre: Mean position of its samples.
        radius: Maximum distance from the centre.
        purity: Proportion of the dominant class.
        dominant_class: Most frequent class.
    """
    points = X[indices]
    labels = y[indices]
    centre = np.mean(points, axis=0)
    distances = np.linalg.norm(points - centre, axis=1)
    radius = np.max(distances)
    counts = np.bincount(labels, minlength=2)
    purity = np.max(counts) / len(indices)
    dominant_class = np.argmax(counts)

    return centre, radius, purity, dominant_class


# ============================================================
# 4. SPLIT GRANULAR BALL USING SPATIAL K-MEANS
# ============================================================
def split_ball(indices):
    """
    Split a granular ball into two smaller balls.

    K-Means uses only feature coordinates.
    Class labels are NOT used during splitting.
    """
    points = X[indices]
    if len(points) < 2 * MIN_CHILD_SIZE:
        return None

    kmeans = KMeans(
        n_clusters=2,
        random_state=RANDOM_STATE,
        n_init=10
    )

    clusters = kmeans.fit_predict(points)
    ball_1 = indices[clusters == 0]
    ball_2 = indices[clusters == 1]

    if (len(ball_1) < MIN_CHILD_SIZE or len(ball_2) < MIN_CHILD_SIZE):
        return None

    return ball_1, ball_2

# ============================================================
# 5. RECURSIVE GRANULAR BALL GENERATION
# ============================================================
def generate_balls(indices, depth=0):
    """
    Recursively split impure granular balls.

    Stop when:
        1. Purity reaches the specified threshold.
        2. Maximum recursion depth is reached.
        3. Further splitting is impossible.
    """
    _, _, purity, _ = calculate_ball(indices)
    if purity >= PURITY_THRESHOLD:
        return [{"indices": indices,"reason": "Purity reached"}]

    if depth >= MAX_DEPTH:
        return [{"indices": indices,"reason": "Maximum depth reached"}]

    children = split_ball(indices)
    if children is None:
        return [{"indices": indices,"reason": "Cannot split further"}]

    ball_1, ball_2 = children
    return (generate_balls(ball_1, depth + 1) + generate_balls(ball_2, depth + 1))

# ============================================================
# 6. RUN GRANULAR BALL COMPUTING
# ============================================================
initial_ball = np.arange(len(X))
granular_balls = generate_balls(initial_ball)

# ============================================================
# 7. DISPLAY GRANULAR BALL RESULTS
# ============================================================
print("\nRESULTS")
print("=" * 55)
print("Dataset samples:", len(X))
print("Purity threshold:", PURITY_THRESHOLD)
print("Final granular balls:", len(granular_balls))

unresolved_balls = []
for i, ball in enumerate(granular_balls):
    indices = ball["indices"]
    centre, radius, purity, dominant_class = calculate_ball(indices)
    counts = np.bincount(y[indices], minlength=2)

    print(f"\nBall {i + 1}")
    print("-" * 30)
    print("Total samples:", len(indices))
    print("Class 0 (Red):", counts[0])
    print("Class 1 (Blue):", counts[1])
    print("Dominant class:", dominant_class)
    print(f"Purity: {purity:.4f}")
    print(f"Radius: {radius:.4f}")
    print("Status:", ball["reason"])

    if purity < PURITY_THRESHOLD:
        unresolved_balls.append(i + 1)

# ============================================================
# 8. VERIFY PURITY
# ============================================================
print("\nPURITY VERIFICATION")
print("=" * 55)
if not unresolved_balls:
    print("All granular balls reached the purity threshold.")
else:
    print("Unresolved granular balls:", unresolved_balls)
    for i in unresolved_balls:
        indices = granular_balls[i - 1]["indices"]
        _, _, purity, _ = calculate_ball(indices)
        print(f"Ball {i}: Purity = {purity:.4f}")

# ============================================================
# 9. VERIFY SAMPLE ASSIGNMENT
# ============================================================
all_indices = np.concatenate([
    ball["indices"] for ball in granular_balls
])

assignment_valid = (
    len(all_indices) == len(X)
    and len(np.unique(all_indices)) == len(X)
    and np.array_equal(
        np.sort(all_indices),
        np.arange(len(X))
    )
)

print("\nSAMPLE ASSIGNMENT VERIFICATION")
print("=" * 55)
print("Every sample assigned exactly once:", assignment_valid)

# ============================================================
# 10. VERIFY GRANULAR BALL BOUNDARIES
# ============================================================
print("\nBOUNDARY VERIFICATION")
print("=" * 55)
for i, ball in enumerate(granular_balls):
    indices = ball["indices"]
    centre, radius, _, _ = calculate_ball(indices)
    distances = np.linalg.norm(X[indices] - centre, axis=1)
    outside = np.sum(distances > radius + 1e-10)
    print(f"Ball {i + 1}: Points outside = {outside}")

# ============================================================
# 11. GEOMETRIC PURITY VERIFICATION
# ============================================================
print("\nGEOMETRIC PURITY VERIFICATION")
print("=" * 55)
for i, ball in enumerate(granular_balls):
    indices = ball["indices"]
    centre, radius, membership_purity, _ = calculate_ball(indices)
    distances = np.linalg.norm(X - centre, axis=1)
    inside_indices = np.where(distances <= radius + 1e-10)[0]
    counts = np.bincount(y[inside_indices], minlength=2)
    geometric_purity = np.max(counts) / len(inside_indices)

    print(f"\nBall {i + 1}")
    print("Samples assigned:", len(indices))
    print("Samples geometrically inside:", len(inside_indices))
    print("Red samples inside:", counts[0])
    print("Blue samples inside:", counts[1])
    print(f"Membership purity: {membership_purity:.4f}")
    print(f"Geometric purity: {geometric_purity:.4f}")

# ============================================================
# 12. VISUALISATION
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

# Original dataset
ax = axes[0]
for class_label in [0, 1]:
    points = X[y == class_label]
    ax.scatter(points[:, 0],points[:, 1], color=CLASS_COLOURS[class_label], s=20, alpha=0.8)

ax.set_title("Original Dataset")

# GBC decomposition
ax = axes[1]
for ball in granular_balls:
    indices = ball["indices"]
    centre, radius, purity, dominant_class = calculate_ball(indices)
    ax.add_patch(plt.Circle(centre, radius, fill=False, color=CLASS_COLOURS[dominant_class], linewidth=1.5))

for class_label in [0, 1]:
    points = X[y == class_label]
    ax.scatter(points[:, 0],points[:, 1],color=CLASS_COLOURS[class_label],s=20,alpha=0.8)

for i, ball in enumerate(granular_balls):
    indices = ball["indices"]
    centre, _, purity, _ = calculate_ball(indices)
    ax.scatter(centre[0],centre[1],marker="x",color="black",s=50)
    status = "*" if purity < PURITY_THRESHOLD else ""
    ax.annotate(f"B{i + 1}{status}\n{purity:.2f}",centre,xytext=(4, 5),textcoords="offset points",fontsize=7)

ax.set_title("GBC Decomposition")

# Granular ball membership
ax = axes[2]
ball_colours = plt.cm.tab20(np.linspace(0, 1, max(len(granular_balls), 1)))
for i, ball in enumerate(granular_balls):
    indices = ball["indices"]
    points = X[indices]
    centre, radius, _, _ = calculate_ball(indices)
    colour = ball_colours[i]
    ax.scatter(points[:, 0],points[:, 1],color=colour,s=20)
    ax.add_patch(plt.Circle(centre,radius,fill=False,color=colour,linewidth=1.5))
    ax.scatter(centre[0],centre[1],marker="x",color="black",s=45)
    ax.annotate(f"B{i + 1}",centre,xytext=(4, 5),textcoords="offset points",fontsize=7)

ax.set_title("Granular Ball Membership")

# Common formatting
for ax in axes:
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")
    ax.grid(alpha=0.2)
    ax.axis("equal")

plt.suptitle(f"Granular Ball Computing | Purity Threshold = {PURITY_THRESHOLD}")
plt.tight_layout()
plt.show()