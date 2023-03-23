add_executable(test_example test_example.cpp)
target_link_libraries(test_example lib)
add_test(NAME test_example COMMAND test_example)

add_executable(test_example_2 test_example_2.cpp)
target_link_libraries(test_example_2 lib)
add_test(NAME test_example_2 COMMAND test_example_2)
