from conans import ConanFile, tools, os

class BoostFiberConan(ConanFile):
    name = "Boost.Fiber"
    version = "1.64.0"
    generators = "txt" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/boostorg/fiber"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "fiber"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing" 
    requires =  "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Context/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Intrusive/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing"

                      #assert1 config0 context12 core2 intrusive6 predef0 smart_ptr4
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

