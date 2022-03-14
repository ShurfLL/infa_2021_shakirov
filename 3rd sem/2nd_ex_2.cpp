#include <iostream>
#include <random>
#include <fstream>

int N = 50;
int step = 5;

void iteration(int dislocations[][5], int size_of_arr) {
    for (int i = 0; i < size_of_arr; i++) {
        if (dislocations[i][4] != 0) {
            std::random_device dev;
            std::mt19937 rng(dev());
            std::uniform_int_distribution<int> dist(1, 4);
            int direction = dist(rng);
            switch (direction) {
                case 1:
                    dislocations[i][2] += 1;
                    break;
                case 2:
                    dislocations[i][2] -= 1;
                    break;
                case 3:
                    dislocations[i][3] += 1;
                    break;
                case 4:
                    dislocations[i][3] -= 1;
                    break;
                default:
                    break;
            }
        }
    }
}

void cryst_upd(int dislocations[][5], int size_of_arr) {
    for (int i = 0; i < size_of_arr; i++) {
        for (int j = 0; j < size_of_arr; j++) {
            if (i != j and dislocations[i][4] != 0) {
                if (dislocations[i][2] == dislocations[j][2] and dislocations[i][3] == dislocations[j][3]) {
                    dislocations[i][2] = dislocations[i][0];
                    dislocations[i][3] = dislocations[i][1];
                    dislocations[i][4] = 0;
                } else if (dislocations[i][2] == N - 1 or dislocations[i][2] == 0 or dislocations[i][0] == N - 1 or
                            dislocations[i][0] == 0) {
                    dislocations[i][4] = 0;
                } else if (i != j and
                           ((dislocations[i][2] - dislocations[j][2]) * (dislocations[i][2] - dislocations[j][2]) +
                            (dislocations[i][3] - dislocations[j][3]) * (dislocations[i][3] - dislocations[j][3]) ==
                            1)) {
                    dislocations[i][4] = 0;
                }
            }
        }
        if (dislocations[i][3] < 0 or dislocations[i][3] > N - 1){
            dislocations[i][3] = (2 * N + dislocations[i][3]) % N;
        }
        dislocations[i][0] = dislocations[i][2];
        dislocations[i][1] = dislocations[i][3];
    }
}

int cryst_state(int dislocations[][5], int size_of_arr) {
    int res = 0;
    for (int i = 0; i < size_of_arr; i++) {
        res += dislocations[i][4];
    }
    return res;
}

void give_rand_pos(int dislocations[][5], int size_of_arr) {
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<int> dist1(0, N * N - 1);
    int shuffle[N * N];
    for (int i = 0; i < N * N; i++) {
        shuffle[i] = i;
    }
    for (int i = 0; i < N * N; i++) {
        std::swap(shuffle[i], shuffle[dist1(rng)]);
    }
    for (int i = 0; i < size_of_arr; i++) {
        dislocations[i][0] = shuffle[i] / N;
        dislocations[i][1] = shuffle[i] % N;
        dislocations[i][2] = dislocations[i][0];
        dislocations[i][3] = dislocations[i][1];
        dislocations[i][4] = 1;
    }
}

int main() {
    std::ofstream outf("data1_1.txt");
    int iter = 0;
    int avrgnumb = 20;
    int avrg = 0;
    for (int numb_of_dis = step; numb_of_dis <= N * N; numb_of_dis += step) {
        for (int i = 0; i < avrgnumb; i++) {
            int dislocations[numb_of_dis][5];
            give_rand_pos(dislocations, numb_of_dis);
            while (cryst_state(dislocations, numb_of_dis) != 0) {
                iteration(dislocations, numb_of_dis);
                cryst_upd(dislocations, numb_of_dis);
                iter++;
            }
            avrg += iter;
            iter = 0;
        }
        avrg /= avrgnumb;
        std::cout << 1.0 * numb_of_dis / (N * N) << " " << avrg << "\n";
        outf << 1.0 * numb_of_dis / (N * N) << " " << avrg << "\n";
        avrg = 0;
    }
    return 0;
}

