import numpy as np
import cv2


class SeamCarving:
    def __init__(self, image, scale):
        self.image = image
        self.scale = scale

    def compute_energy_map(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        gradient_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        gradient_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        energy_map = np.abs(gradient_x) + np.abs(gradient_y)
        return energy_map

    def find_seam(self):
        energy_map = self.compute_energy_map()
        rows, cols = energy_map.shape
        dp = np.zeros_like(energy_map, dtype=np.float64)
        dp[0] = energy_map[0]

        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    dp[i, j] = energy_map[i, j] + min(dp[i-1, j], dp[i-1, j+1])
                elif j == cols - 1:
                    dp[i, j] = energy_map[i, j] + min(dp[i-1, j-1], dp[i-1, j])
                else:
                    dp[i, j] = energy_map[i, j] + \
                        min(dp[i-1, j-1], dp[i-1, j], dp[i-1, j+1])

        seam = []
        j = np.argmin(dp[-1])
        seam.append((rows - 1, j))

        for i in range(rows - 2, -1, -1):
            if j == 0:
                j = np.argmin(dp[i, j:j+2])
            elif j == cols - 1:
                j = np.argmin(dp[i, j-1:j+1]) + j - 1
            else:
                j = np.argmin(dp[i, j-1:j+2]) + j - 1
            seam.append((i, j))

        return seam

    def delete_seam(self, seam):
        rows, cols, _ = self.image.shape
        new_image = np.zeros((rows, cols-1, 3), dtype=np.uint8)

        for i, j in seam:
            new_image[i] = np.delete(self.image[i], j, axis=0)

        return new_image

    def seam_carving(self):
        width = int(self.image.shape[1] * self.scale)

        for _ in range(self.image.shape[1] - width):
            seam = self.find_seam()

            for i, j in seam:
                self.image[i, j] = [0, 0, 255]  # 将线条标记为红色

            cv2.imshow("Seam Carving", self.image)
            cv2.waitKey(1)

            self.image = self.delete_seam(seam)
        cv2.destroyAllWindows()

        return self.image
