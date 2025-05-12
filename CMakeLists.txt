cmake_minimum_required(VERSION 3.10)

# Remove git hash from version number if present
string(REGEX REPLACE "([0-9.]+).*" "\\1" VERSION "${VERSION}")

project(systrace VERSION ${VERSION} LANGUAGES C DESCRIPTION "Systrace library")

include(GNUInstallDirs)

add_library(systrace SHARED src/systrace.c)

set_target_properties(systrace
    PROPERTIES VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
    PUBLIC_HEADER src/systrace.h)

configure_file(systrace.pc.in systrace.pc @ONLY)

install(TARGETS systrace
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

install(FILES ${CMAKE_BINARY_DIR}/systrace.pc
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig)
