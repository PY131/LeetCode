#include "math.h"
#include <iostream>

int Math::max_points(std::vector<std::vector<int>> &points) {
    if (points.size() < 3) {
        return points.size();
    }

    int res = 0;
    for (size_t i = 0; i < points.size(); i++) {
        for (size_t j = i + 1; j < points.size(); j++) {
            // now check the line passing points[i] and points[j]
            int count = 2;
            for (size_t k = j + 1; k < points.size(); k++) {
                long xi = points[i][0];
                long yi = points[i][1];
                long xj = points[j][0];
                long yj = points[j][1];
                long xk = points[k][0];
                long yk = points[k][1];
                if ((xj - xi) * yk == (yj - yi) * xk + (yi * xj - yj * xi)) {
                    count++;
                }
            }
            if (res < count) {
                res = count;
            }
        }
    }
    return res;
}
