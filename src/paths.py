from sublime_lib import ResourcePath


__all__ = ['USER_DATA_PATH', 'PACKAGE_PATH']

USER_DATA_PATH = ResourcePath('Packages/User/JS Custom')
PACKAGE_PATH = ResourcePath.from_file_path(__file__).parent.parent
