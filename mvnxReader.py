import mvnx
import numpy as np

if __name__ == "__main__":
    sbj01_bend1 = mvnx.load('sbj01_bend1.mvnx')
    sensorOrientation = np.array(sbj01_bend1.sensorOrientation)
    orientation = np.array(sbj01_bend1.orientation)
    print(sensorOrientation)
    print(orientation.shape)
