import numpy as np

# Assuming a Vector class that supports required operations like Dot, Cross, Normalize, etc.

class Vector(np.ndarray):
    def __new__(cls, input_array):
        return np.asarray(input_array).view(cls)
    
    def sub(self, other):
        return Vector(self - other)
    
    def scale(self, scalar):
        return Vector(self * scalar)
    
    def normalize(self):
        norm = np.linalg.norm(self)
        if norm == 0: 
            return self
        return Vector(self / norm)
    
    def angle_between(self, other):
        # Compute the angle in radians between two vectors
        dot_product = np.dot(self, other)
        norms = np.linalg.norm(self) * np.linalg.norm(other)
        # To avoid precision issues that cause out-of-range values
        cos_angle = np.clip(dot_product / norms, -1.0, 1.0)
        return np.arccos(cos_angle)

    def cross(self, other):
        return Vector(np.cross(self, other))

    def __repr__(self):
        return f"Vector({self[0]}, {self[1]}, {self[2]})"


# ComputeAcceleration
def compute_acceleration(vec1, vec2, vector_lib):
    sub_result = vec1.sub(vec2)
    scaled_result = sub_result.scale(1.0 / vec2[2])  # Assuming the divisor is a component of vec2
    return scaled_result

# ClampDirToAng
def clamp_dir_to_ang(vec1, vec2, max_angle, matrix_lib):
    angle_between = vec1.angle_between(vec2)
    if angle_between > max_angle:
        # Calculate the direction to rotate
        direction = vec2.sub(vec1)
        cross_product = vec1.cross(vec2).normalize()
        rotation_matrix = matrix_lib.rotation_axis_matrix(cross_product)
        rotated_vec = rotation_matrix.rotate(vec1)
        return rotated_vec
    else:
        return vec1

# RemoveVectorDirection
def remove_vector_direction(vec1, vec2, vector_lib):
    dot_product = np.dot(vec1, vec2)
    scaled_vector = vec2.scale(dot_product)
    subtracted_vector = vec1.sub(scaled_vector)
    return subtracted_vector.normalize()


# Example matrix class for handling rotations
class Matrix:
    def rotation_axis_matrix(self, axis):
        # Assume some logic for creating a rotation matrix from an axis of rotation
        axis = axis.normalize()
        angle = np.pi / 4  # Assuming a 45-degree rotation for simplicity
        cos_angle = np.cos(angle)
        sin_angle = np.sin(angle)
        ux, uy, uz = axis

        rotation_matrix = np.array([
            [cos_angle + ux**2 * (1 - cos_angle), ux * uy * (1 - cos_angle) - uz * sin_angle, ux * uz * (1 - cos_angle) + uy * sin_angle],
            [uy * ux * (1 - cos_angle) + uz * sin_angle, cos_angle + uy**2 * (1 - cos_angle), uy * uz * (1 - cos_angle) - ux * sin_angle],
            [uz * ux * (1 - cos_angle) - uy * sin_angle, uz * uy * (1 - cos_angle) + ux * sin_angle, cos_angle + uz**2 * (1 - cos_angle)]
        ])
        return Matrix(rotation_matrix)

    def rotate(self, vector):
        return np.dot(self, vector)

    def __init__(self, matrix):
        self.matrix = matrix

    def __repr__(self):
        return f"Matrix({self.matrix})"


# Test the functions
vec1 = Vector([1, 2, 3])
vec2 = Vector([4, 5, 6])
vector_lib = Vector

# Example: ComputeAcceleration
acceleration = compute_acceleration(vec1, vec2, vector_lib)
print("Acceleration:", acceleration)

# Example: ClampDirToAng
matrix_lib = Matrix
clamped_direction = clamp_dir_to_ang(vec1, vec2, np.pi / 4, matrix_lib)
print("Clamped Direction:", clamped_direction)

# Example: RemoveVectorDirection
removed_direction = remove_vector_direction(vec1, vec2, vector_lib)
print("Removed Direction:", removed_direction)
