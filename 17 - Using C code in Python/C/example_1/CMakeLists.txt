cmake_minimum_required(VERSION 3.17)
project(Example1 C)

set(CMAKE_C_STANDARD 99)

add_library(Example1 SHARED sum.c sum.h)