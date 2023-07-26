# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xanxus/workspaces/K-mean/cpp

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xanxus/workspaces/K-mean/cpp/build

# Include any dependencies generated for this target.
include src/CMakeFiles/kmeans.dir/depend.make

# Include the progress variables for this target.
include src/CMakeFiles/kmeans.dir/progress.make

# Include the compile flags for this target's objects.
include src/CMakeFiles/kmeans.dir/flags.make

src/CMakeFiles/kmeans.dir/k_means.o: src/CMakeFiles/kmeans.dir/flags.make
src/CMakeFiles/kmeans.dir/k_means.o: ../src/k_means.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xanxus/workspaces/K-mean/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object src/CMakeFiles/kmeans.dir/k_means.o"
	cd /home/xanxus/workspaces/K-mean/cpp/build/src && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/kmeans.dir/k_means.o -c /home/xanxus/workspaces/K-mean/cpp/src/k_means.cpp

src/CMakeFiles/kmeans.dir/k_means.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/kmeans.dir/k_means.i"
	cd /home/xanxus/workspaces/K-mean/cpp/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xanxus/workspaces/K-mean/cpp/src/k_means.cpp > CMakeFiles/kmeans.dir/k_means.i

src/CMakeFiles/kmeans.dir/k_means.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/kmeans.dir/k_means.s"
	cd /home/xanxus/workspaces/K-mean/cpp/build/src && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xanxus/workspaces/K-mean/cpp/src/k_means.cpp -o CMakeFiles/kmeans.dir/k_means.s

# Object files for target kmeans
kmeans_OBJECTS = \
"CMakeFiles/kmeans.dir/k_means.o"

# External object files for target kmeans
kmeans_EXTERNAL_OBJECTS =

src/kmeans: src/CMakeFiles/kmeans.dir/k_means.o
src/kmeans: src/CMakeFiles/kmeans.dir/build.make
src/kmeans: lib/libarray.a
src/kmeans: /usr/local/lib/libopencv_dnn.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_highgui.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_ml.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_objdetect.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_shape.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_stitching.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_superres.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_videostab.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_calib3d.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_features2d.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_flann.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_photo.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_video.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_videoio.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_imgcodecs.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_imgproc.so.3.4.10
src/kmeans: /usr/local/lib/libopencv_core.so.3.4.10
src/kmeans: src/CMakeFiles/kmeans.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xanxus/workspaces/K-mean/cpp/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable kmeans"
	cd /home/xanxus/workspaces/K-mean/cpp/build/src && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/kmeans.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
src/CMakeFiles/kmeans.dir/build: src/kmeans

.PHONY : src/CMakeFiles/kmeans.dir/build

src/CMakeFiles/kmeans.dir/clean:
	cd /home/xanxus/workspaces/K-mean/cpp/build/src && $(CMAKE_COMMAND) -P CMakeFiles/kmeans.dir/cmake_clean.cmake
.PHONY : src/CMakeFiles/kmeans.dir/clean

src/CMakeFiles/kmeans.dir/depend:
	cd /home/xanxus/workspaces/K-mean/cpp/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xanxus/workspaces/K-mean/cpp /home/xanxus/workspaces/K-mean/cpp/src /home/xanxus/workspaces/K-mean/cpp/build /home/xanxus/workspaces/K-mean/cpp/build/src /home/xanxus/workspaces/K-mean/cpp/build/src/CMakeFiles/kmeans.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : src/CMakeFiles/kmeans.dir/depend

