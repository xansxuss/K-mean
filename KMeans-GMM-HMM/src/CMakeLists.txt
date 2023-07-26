include_directories(${CMAKE_SOURCE_DIR}/lib)
link_directories(${CMAKE_SOURCE_DIR}/lib)
add_executable(KMeans-test KMeans-test.cpp)
target_link_libraries(KMeans-test KMeans)