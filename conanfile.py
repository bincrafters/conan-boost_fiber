#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostFiberConan(base.BoostBaseConan):
    name = "boost_fiber"
    url = "https://github.com/bincrafters/conan-boost_fiber"
    lib_short_names = ["fiber"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_only_deps = [
        "algorithm",
        "format"
    ]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_context",
        "boost_core",
        "boost_filesystem",
        "boost_intrusive",
        "boost_predef",
        "boost_smart_ptr"
    ]
