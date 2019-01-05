cmake_minimum_required(VERSION 3.7)
project(qpropgen-examples)

set(CMAKE_CXX_STANDARD 11)

find_package(Qt5 REQUIRED Core)
include(../cmake/qpropgen.cmake)

qpropgen(QPROPGEN_SOURCES
    basesound.yaml
    defaults.yaml
    impl.yaml
    includes.yaml
    mutability.yaml
    usebaseclass.yaml
)

include_directories(${CMAKE_CURRENT_BINARY_DIR})

add_executable(example example.cpp ${QPROPGEN_SOURCES})
target_link_libraries(example Qt5::Core)
