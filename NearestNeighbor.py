import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_cost(points, path):
    cost = 0
    num_cities = len(points)

    for i in range(num_cities - 1):
        start_city = path[i]
        end_city = path[i+1]
        distance = calculate_distance(points[start_city], points[end_city])
        cost += distance

    # Son şehirden başlangıç noktasına dönüş maliyeti
    start_city = path[-1]
    end_city = path[0]
    distance = calculate_distance(points[start_city], points[end_city])
    cost += distance

    return cost

def tsp_nearest_neighbor(points):
    num_cities = len(points)
    visited = [False] * num_cities
    path = []
    current_city = 0  # Başlangıç noktası

    for _ in range(num_cities):
        path.append(current_city)
        visited[current_city] = True
        nearest_distance = float('inf')
        nearest_city = None

        for i in range(num_cities):
            if not visited[i] and i != current_city:
                distance = calculate_distance(points[current_city], points[i])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_city = i

        current_city = nearest_city

    return path

# Metin dosyasından veri okuma
def read_data_from_file(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append([x, y])
    return points

# Örnek kullanım
file_path = 'tsp_85900_1.txt'
points = read_data_from_file(file_path)
path = tsp_nearest_neighbor(points)
cost = calculate_cost(points, path)

print("En kısa yol:", path)
print("Maliyet:", cost)
