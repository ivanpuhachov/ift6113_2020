cmake_minimum_required(VERSION 3.1)
project(example)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# libigl
option(LIBIGL_WITH_OPENGL            "Use OpenGL"         ON)
option(LIBIGL_WITH_OPENGL_GLFW       "Use GLFW"           ON)

find_package(LIBIGL REQUIRED QUIET)

set(
        main_src
        main.cpp
)

# Add your project files
add_executable(${PROJECT_NAME} ${main_src})
target_link_libraries(${PROJECT_NAME} igl::core igl::opengl_glfw)
