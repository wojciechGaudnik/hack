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
CMAKE_COMMAND = /home/bq666/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/201.7223.86/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/bq666/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/201.7223.86/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/bq666/Workspace/hack/catWrapper

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/bq666/Workspace/hack/catWrapper/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/catWrapper.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/catWrapper.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/catWrapper.dir/flags.make

CMakeFiles/catWrapper.dir/main.cpp.o: CMakeFiles/catWrapper.dir/flags.make
CMakeFiles/catWrapper.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/bq666/Workspace/hack/catWrapper/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/catWrapper.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/catWrapper.dir/main.cpp.o -c /home/bq666/Workspace/hack/catWrapper/main.cpp

CMakeFiles/catWrapper.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/catWrapper.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/bq666/Workspace/hack/catWrapper/main.cpp > CMakeFiles/catWrapper.dir/main.cpp.i

CMakeFiles/catWrapper.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/catWrapper.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/bq666/Workspace/hack/catWrapper/main.cpp -o CMakeFiles/catWrapper.dir/main.cpp.s

# Object files for target catWrapper
catWrapper_OBJECTS = \
"CMakeFiles/catWrapper.dir/main.cpp.o"

# External object files for target catWrapper
catWrapper_EXTERNAL_OBJECTS =

catWrapper: CMakeFiles/catWrapper.dir/main.cpp.o
catWrapper: CMakeFiles/catWrapper.dir/build.make
catWrapper: CMakeFiles/catWrapper.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/bq666/Workspace/hack/catWrapper/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable catWrapper"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/catWrapper.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/catWrapper.dir/build: catWrapper

.PHONY : CMakeFiles/catWrapper.dir/build

CMakeFiles/catWrapper.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/catWrapper.dir/cmake_clean.cmake
.PHONY : CMakeFiles/catWrapper.dir/clean

CMakeFiles/catWrapper.dir/depend:
	cd /home/bq666/Workspace/hack/catWrapper/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/bq666/Workspace/hack/catWrapper /home/bq666/Workspace/hack/catWrapper /home/bq666/Workspace/hack/catWrapper/cmake-build-debug /home/bq666/Workspace/hack/catWrapper/cmake-build-debug /home/bq666/Workspace/hack/catWrapper/cmake-build-debug/CMakeFiles/catWrapper.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/catWrapper.dir/depend

