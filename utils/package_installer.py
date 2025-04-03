# import subprocess
# import sys
# import pkg_resources

# def read_requirements(file_path):
#     requirements = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             if line.strip() and not line.startswith('#'):
#                 pkg, version = line.strip().split('==')
#                 requirements.append((pkg, version))
#     return requirements

# def check_and_install(package, version):
#     try:
#         pkg_resources.get_distribution(package)
#     except pkg_resources.DistributionNotFound:
#         subprocess.check_call([sys.executable, "-m", "pip", "install", f"{package}=={version}"])

# requirements = read_requirements('./requirements.txt')
# for package, version in requirements:
#     check_and_install(package, version)