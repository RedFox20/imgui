import mama
import os

# Explore Mama docs at https://github.com/RedFox20/Mama
class imgui(mama.BuildTarget):

    local_workspace = 'packages'

    def settings(self):
        self.config.prefer_gcc('imgui')

    def dependencies(self):
        pass

    def configure(self):
        pass

    def build(self):
        self.cmake_build()

    def package(self):
        build_dir = self.build_dir()
        src_dir = self.source_dir()

        # copy imgui headers into build/include/imgui/
        os.makedirs(f'{build_dir}/include/imgui/', exist_ok=True)
        self.copy(src_dir, f'{build_dir}/include/', filter='.h')

        # copy {build}/_deps/glfw-src/include/GLFW to /include/GLFW
        self.copy(f'{build_dir}/_deps/glfw-src/include/GLFW',
                  f'{build_dir}/include')

        self.export_includes('include', build_dir=True)
        self.export_includes('include/imgui', build_dir=True)

        # libs are installed by CMake to build/lib/*
        self.export_lib('lib/libimgui.a')
        self.export_lib('lib/libglfw3.a')

    def deploy(self):
        self.papa_deploy('deploy')

    def start(self, args: str):
        pass

    def test(self, args):
        pass

