include_directories(${CMAKE_SOURCE_DIR}/lib)
link_directories(${CMAKE_SOURCE_DIR}/lib)
add_executable(kmeans k_means.cpp)
target_link_libraries(kmeans array)
target_link_libraries(kmeans PRIVATE ${OpenCV_LIBS})