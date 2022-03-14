cmake_minimum_required(VERSION 3.21)
project(3rd_sem)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address -Wextra -Wall  -Wpedantic")
add_executable(3rd_sem 2nd_ex.cpp)
