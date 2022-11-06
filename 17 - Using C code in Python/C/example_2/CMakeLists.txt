cmake_minimum_required(VERSION 3.17)
project(Example2 C)

set(CMAKE_C_STANDARD 99)

add_library(Example2 SHARED rational.c rational.h)