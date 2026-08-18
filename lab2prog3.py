import random
import time
import csv
import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree:

    def __init__(self):
        self.root_node = None

    def add(self, value):

        new_node = TreeNode(value)

        if self.root_node is None:
            self.root_node = new_node
            return

        current_node = self.root_node

        while True:

            if value < current_node.value:

                if current_node.left_child is None:
                    current_node.left_child = new_node
                    return

                current_node = current_node.left_child

            elif value > current_node.value:

                if current_node.right_child is None:
                    current_node.right_child = new_node
                    return

                current_node = current_node.right_child

            else:
                return

    def find(self, value):

        current_node = self.root_node

        while current_node is not None:

            if value == current_node.value:
                return True

            elif value < current_node.value:
                current_node = current_node.left_child

            else:
                current_node = current_node.right_child

        return False

    def minimum_node(self, node):

        current_node = node

        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node

    def remove(self, value):

        parent_node = None
        current_node = self.root_node

        while current_node is not None and current_node.value != value:

            parent_node = current_node

            if value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        if current_node is None:
            return

        if current_node.left_child is None or current_node.right_child is None:

            if current_node.left_child is not None:
                child_node = current_node.left_child
            else:
                child_node = current_node.right_child

            if parent_node is None:
                self.root_node = child_node

            elif parent_node.left_child == current_node:
                parent_node.left_child = child_node

            else:
                parent_node.right_child = child_node

        else:

            successor_parent = current_node
            successor_node = current_node.right_child

            while successor_node.left_child is not None:
                successor_parent = successor_node
                successor_node = successor_node.left_child

            current_node.value = successor_node.value

            if successor_parent.left_child == successor_node:
                successor_parent.left_child = successor_node.right_child
            else:
                successor_parent.right_child = successor_node.right_child

    def get_height(self):

        if self.root_node is None:
            return 0

        maximum_height = 0
        node_stack = [(self.root_node, 1)]

        while node_stack:

            current_node, level_number = node_stack.pop()

            maximum_height = max(maximum_height, level_number)

            if current_node.left_child is not None:
                node_stack.append(
                    (current_node.left_child, level_number + 1)
                )

            if current_node.right_child is not None:
                node_stack.append(
                    (current_node.right_child, level_number + 1)
                )

        return maximum_height


def create_data(size):

    random_values = list(range(1, size + 1))
    random.shuffle(random_values)

    sorted_values = list(range(1, size + 1))

    reverse_values = list(range(size, 0, -1))

    return {
        "Random": random_values,
        "Sorted": sorted_values,
        "Reverse-sorted": reverse_values
    }


def perform_test(input_data, size):

    search_tree = BinarySearchTree()

    start_clock = time.perf_counter()

    for number in input_data:
        search_tree.add(number)

    end_clock = time.perf_counter()

    construction_time = end_clock - start_clock

    tree_height = search_tree.get_height()

    search_values = random.choices(input_data, k=1000)

    start_clock = time.perf_counter()

    for search_number in search_values:
        search_tree.find(search_number)

    end_clock = time.perf_counter()

    total_search_time = end_clock - start_clock

    removal_values = random.sample(input_data, 500)

    start_clock = time.perf_counter()

    for removal_number in removal_values:
        search_tree.remove(removal_number)

    end_clock = time.perf_counter()

    total_delete_time = end_clock - start_clock

    return (
        construction_time,
        tree_height,
        total_search_time,
        total_delete_time
    )


input_sizes = [1000, 5000, 10000]

experiment_results = []

print("\nBST PERFORMANCE EXPERIMENT")
print("=" * 100)

for size in input_sizes:

    print(f"\nTesting n = {size}")
    print("-" * 100)

    generated_sets = create_data(size)

    for input_type, input_values in generated_sets.items():

        construction_time, height_value, search_duration, delete_duration = \
            perform_test(input_values, size)

        experiment_results.append({
            "n": size,
            "type": input_type,
            "build_time": construction_time,
            "height": height_value,
            "search_time": search_duration,
            "delete_time": delete_duration
        })

        print(
            f"{input_type:15} | "
            f"Build: {construction_time:.6f} sec | "
            f"Height: {height_value:5d} | "
            f"Search: {search_duration:.6f} sec | "
            f"Delete: {delete_duration:.6f} sec"
        )


print("\n\nFINAL RESULTS")
print("=" * 115)

print(
    f"{'N':>6} "
    f"{'Input Type':>18} "
    f"{'Build Time':>15} "
    f"{'Height':>10} "
    f"{'1000 Searches':>18} "
    f"{'500 Deletions':>18}"
)

print("-" * 115)

for experiment in experiment_results:

    print(
        f"{experiment['n']:>6} "
        f"{experiment['type']:>18} "
        f"{experiment['build_time']:>15.6f} "
        f"{experiment['height']:>10} "
        f"{experiment['search_time']:>18.6f} "
        f"{experiment['delete_time']:>18.6f}"
    )


with open("bst_results.csv", "w", newline="") as output_file:

    csv_writer = csv.writer(output_file)

    csv_writer.writerow([
        "N",
        "Input Type",
        "Build Time",
        "Height",
        "1000 Search Time",
        "500 Delete Time"
    ])

    for experiment in experiment_results:

        csv_writer.writerow([
            experiment["n"],
            experiment["type"],
            experiment["build_time"],
            experiment["height"],
            experiment["search_time"],
            experiment["delete_time"]
        ])


print("\nResults saved to bst_results.csv")


input_types = ["Random", "Sorted", "Reverse-sorted"]

plot_colors = {
    "Random": "blue",
    "Sorted": "red",
    "Reverse-sorted": "green"
}


# Graph 1: BST Height

plt.figure(figsize=(9, 6))

for input_type in input_types:

    x_values = []
    y_values = []

    for experiment in experiment_results:

        if experiment["type"] == input_type:
            x_values.append(experiment["n"])
            y_values.append(experiment["height"])

    plt.plot(
        x_values,
        y_values,
        marker="o",
        linewidth=2,
        label=input_type,
        color=plot_colors[input_type]
    )

plt.title("BST Height vs Input Size")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Tree Height")
plt.legend()
plt.grid(True)

plt.savefig("height_graph.png", dpi=300)
plt.show()


# Graph 2: Build Time

plt.figure(figsize=(9, 6))

for input_type in input_types:

    x_values = []
    y_values = []

    for experiment in experiment_results:

        if experiment["type"] == input_type:
            x_values.append(experiment["n"])
            y_values.append(experiment["build_time"])

    plt.plot(
        x_values,
        y_values,
        marker="o",
        linewidth=2,
        label=input_type,
        color=plot_colors[input_type]
    )

plt.title("BST Build Time vs Input Size")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Build Time (seconds)")
plt.legend()
plt.grid(True)

plt.savefig("build_time_graph.png", dpi=300)
plt.show()


# Graph 3: Search Time

plt.figure(figsize=(9, 6))

for input_type in input_types:

    x_values = []
    y_values = []

    for experiment in experiment_results:

        if experiment["type"] == input_type:
            x_values.append(experiment["n"])
            y_values.append(experiment["search_time"])

    plt.plot(
        x_values,
        y_values,
        marker="o",
        linewidth=2,
        label=input_type,
        color=plot_colors[input_type]
    )

plt.title("Time for 1000 Searches")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Search Time (seconds)")
plt.legend()
plt.grid(True)

plt.savefig("search_time_graph.png", dpi=300)
plt.show()


# Graph 4: Deletion Time

plt.figure(figsize=(9, 6))

for input_type in input_types:

    x_values = []
    y_values = []

    for experiment in experiment_results:

        if experiment["type"] == input_type:
            x_values.append(experiment["n"])
            y_values.append(experiment["delete_time"])

    plt.plot(
        x_values,
        y_values,
        marker="o",
        linewidth=2,
        label=input_type,
        color=plot_colors[input_type]
    )

plt.title("Time for 500 Deletions")
plt.xlabel("Number of Nodes (n)")
plt.ylabel("Deletion Time (seconds)")
plt.legend()
plt.grid(True)

plt.savefig("delete_time_graph.png", dpi=300)
plt.show()
