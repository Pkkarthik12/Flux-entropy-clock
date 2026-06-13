import numpy as np
from loguru import logger

class EntropyEngine:
    def __init__(self):
        """
        The AI core that translates raw data into kinetic 'Time Deconstruction' vectors.
        """
        # Random non-linear mapping for the "Entropy Translation"
        self.translation_matrix = np.random.randn(3, 3)
        logger.info("Entropy Engine warm-up complete. Non-linear mapping initialized.")

    def calculate_chaos_vector(self, entropy_samples):
        """
        Uses a transformation to calculate how the physical clock should move.
        :return: (speed, direction_x, direction_y)
        """
        # Map samples through the entropy matrix
        transformed = np.dot(entropy_samples, self.translation_matrix)
        
        # Calculate 'Clock Speed' - how fast time is deconstructing
        speed = float(np.sum(np.abs(transformed)) / 3.0)
        
        # Calculate target physical coordinates for the actuator
        coord_x = float(np.sin(transformed[0]) * 100) # Range -100 to 100
        coord_y = float(np.cos(transformed[1]) * 100)
        
        logger.info(f"Chaos Vector Calculated | Speed: {speed:.2f} | Target: ({coord_x:.1f}, {coord_y:.1f})")
        
        return {
            "speed": speed,
            "coord_x": coord_x,
            "coord_y": coord_y,
            "is_volatile": speed > 1.5
        }
