# Install script for directory: /media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/src/ros_basics_tutorials

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/build/ros_basics_tutorials/catkin_generated/installspace/ros_basics_tutorials.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ros_basics_tutorials/cmake" TYPE FILE FILES
    "/media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/build/ros_basics_tutorials/catkin_generated/installspace/ros_basics_tutorialsConfig.cmake"
    "/media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/build/ros_basics_tutorials/catkin_generated/installspace/ros_basics_tutorialsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ros_basics_tutorials" TYPE FILE FILES "/media/ashwin/0a3f0d0a-6132-40ed-a7c9-67a456fc8683/ashwin/catkin_ws/src/ros_basics_tutorials/package.xml")
endif()

