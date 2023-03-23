cmake_minimum_required(VERSION 3.26)

project(
  systems_project
  VERSION 1.0
  DESCRIPTION "System analysis and design project"
  LANGUAGES CXX C)

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
  set(CMAKE_CXX_EXTENSIONS OFF)
endif()

enable_testing()

include_directories(include)

add_subdirectory(lib)
add_subdirectory(tests)
