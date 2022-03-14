#include <iostream>
#include <random>
#include <fstream>

int N = 300;
int step = 5;

void iteration(int dislocation[2]) {
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int> dist(1, 2);
    int direction = dist(rng);
    switch (direction) {
        case 1:
            dislocation[0] += 1;
            break;
        case 2:
            dislocation[0] -= 1;
            break;
        default:
            break;

    }
}

void simple_cryst_upd(int dislocation[2], int n) {
    if (dislocation[0] == 0 or dislocation[0] == n - 1) {
        dislocation[1] = 0;
    }
}

int main() {
    std::ofstream outf("data3.txt");
    int iter = 0;
    int avrgnumb = 20;
    int avrg = 0;
    int dislocation[2];
    for (int n = step; n < N; n += step) {
        for (int i = 0; i < avrgnumb; i++) {
            dislocation[0] = n / 2;
            dislocation[1] = 1;
            while (dislocation[1] != 0) {
                iteration(dislocation);
                simple_cryst_upd(dislocation, n);
                iter += 1;
            }
            avrg += iter;
            iter = 0;
        }
        avrg /= avrgnumb;
        outf << n * n << " " << avrg << "\n";
        std::cout << n* n << " " << avrg << "\n";
        avrg = 0;
    }

    return 0;
}

