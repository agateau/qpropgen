find_program(QPROPGEN_CMD qpropgen)
if (QPROPGEN_CMD)
    message(STATUS "Found qpropgen: ${QPROPGEN_CMD}")
else()
    set(QPROPGEN_CMD python3 "${CMAKE_CURRENT_LIST_DIR}/../qpropgen/fromsrc.py")
    message(STATUS "Using bundled qpropgen from ${QPROPGEN_CMD}")
endif()

# Call qpropgen on the qpropgen files passed as argument.
#
# Usage: qpropgen(outvar file1.yaml [file2.yaml ...])
#
# Example:
#
#    set(prj_SRCS main.cpp)
#    qpropgen(prj_QPROPGEN foo.yaml bar.yaml)
#    add_executable(prj ${prj_SRCS} ${prj_QPROPGEN})
function(qpropgen OUT)
    foreach(yaml ${ARGN})
        get_filename_component(basename ${yaml} NAME_WE)
        get_filename_component(dirname ${yaml} DIRECTORY)

        set(out_dir ${CMAKE_CURRENT_BINARY_DIR}/${dirname})
        set(header ${out_dir}/${basename}.h)
        set(impl ${out_dir}/${basename}.cpp)

        set(cmd ${QPROPGEN_CMD})
        list(APPEND cmd "${yaml}" -d "${out_dir}")
        add_custom_command(
            OUTPUT
                ${header}
                ${impl}
            COMMAND
                ${cmd}
            DEPENDS
                ${yaml}
            WORKING_DIRECTORY
                ${CMAKE_CURRENT_SOURCE_DIR}
        )
        set(impl_list ${impl_list} ${impl})

        # Run moc on the generated files, this way they are usable regardless
        # of whether automoc is enabled
        qt5_wrap_cpp(moc_list ${header})
        # Avoid the warning about CMake policy CMP0071
        # (see "cmake --help-policy CMP0071")
        set_property(SOURCE ${impl} PROPERTY SKIP_AUTOGEN ON)
    endforeach()

    set(${OUT} ${moc_list} ${impl_list} PARENT_SCOPE)
endfunction()
