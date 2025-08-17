cmake_minimum_required(VERSION 3.22)
project(imgui)

set(GLFW_BUILD_X11 ON CACHE BOOL "")
set(GLFW_BUILD_WAYLAND OFF CACHE BOOL "")
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "")
set(GLFW_BUILD_TESTS OFF CACHE BOOL "")
set(GLFW_BUILD_DOCS OFF CACHE BOOL "")
set(GLFW_INSTALL OFF CACHE BOOL "")

include(FetchContent)
FetchContent_Declare(
    glfw
    GIT_REPOSITORY https://github.com/glfw/glfw.git
    GIT_TAG master # TODO: glfw has no recent up-to-date release TAGS
)
FetchContent_MakeAvailable(glfw)

add_library(imgui STATIC)

target_sources(imgui PRIVATE
    imgui.cpp
    imgui_demo.cpp
    imgui_draw.cpp
    imgui_tables.cpp
    imgui_widgets.cpp
    backends/imgui_impl_glfw.cpp
    backends/imgui_impl_opengl3.cpp
)
target_include_directories(imgui PUBLIC
    ./
    ./backends
)

find_package(OpenGL REQUIRED)
target_link_libraries(imgui PUBLIC glfw OpenGL::GL)

install(TARGETS imgui glfw
        DESTINATION ${CMAKE_BINARY_DIR}/lib
        COMPONENT libraries)