#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostFiberConan(ConanFile):
    name = "boost_fiber"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_fiber"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["fiber"]
    is_header_only = False

    options = {"shared": [True, False]}
    default_options = "shared=False"

    source_only_deps = ["format"]

    requires = (
        "boost_package_tools/1.66.0@bincrafters/testing",
        "boost_assert/1.66.0@bincrafters/testing",
        "boost_config/1.66.0@bincrafters/testing",
        "boost_context/1.66.0@bincrafters/testing",
        "boost_core/1.66.0@bincrafters/testing",
        "boost_filesystem/1.66.0@bincrafters/testing",
        "boost_intrusive/1.66.0@bincrafters/testing",
        "boost_predef/1.66.0@bincrafters/testing",
        "boost_smart_ptr/1.66.0@bincrafters/testing"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.66.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
