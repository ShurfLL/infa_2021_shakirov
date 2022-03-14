#include <iostream>
#include <random>
#include <fstream>


int main(){
    std::ofstream outf ("data0_1.txt");
    int iter = 0;
    int avrgnumb = 30;
    int avrg = 0;
    int direction;
    int dislocation[3] = {0, 0, 1};
    //В массиве след. инфа про дислокацию: координаты, координаты, в которые сместится к концу итерации, состояние.
    for (int i = 50; i <= 400; i += 25) {
        dislocation[0] = i / 2;
        dislocation[1] = i / 2;
        for (int j = 0; j < avrgnumb; j++){
            while (dislocation[2] != 0) {
                std::random_device dev;
                std::mt19937 rng(dev());
                std::uniform_int_distribution<int> dist(1, 4);
                direction = dist(rng);
                switch (direction) {
                    case 1:
                        dislocation[0] += 1;
                        break;
                    case 2:
                        dislocation[0] -= 1;
                        break;
                    case 3:
                        dislocation[1] += 1;
                        break;
                    case 4:
                        dislocation[1] -= 1;
                        break;
                }
                if (dislocation[0] == 0 or dislocation[0] == i - 1) {
                    dislocation[2] = 0;
                }
                if (dislocation[1] < 0 or dislocation[1] > i - 1){
                    dislocation[1] = (2*i + dislocation[1]) % i;
                }
                iter++;
            }
            avrg += iter;
            dislocation[0] = i / 2;
            dislocation[1] = i / 2;
            dislocation[2] = 1;
            iter = 0;
        }
        avrg /= avrgnumb;
        outf << i*i  << " " << avrg << "\n";
        std::cout << i*i << " " << avrg << "\n";
        avrg = 0;
    }
    return 0;
}