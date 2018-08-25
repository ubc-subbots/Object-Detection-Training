#       to build, it should be added as a rosdep. This script should  #
#       only contain other dependecies, like those required for gazebo#
#######################################################################

######################################################################
# This script will download and install dependencies for the project #
######################################################################

echo "================================================================"
echo "Installing ROS dependencies..."
echo "================================================================"

# Update Rosdeps
rosdep update

# The current directory
CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Clone any ros dependencies of this repo
rosws update

# Install all required dependencies to build this repo
rosdep install --from-paths src --ignore-src --rosdistro kinetic -y
catkin_make install

echo "================================================================"
echo "Finished installing ROS dependencies."
echo "================================================================"
echo ""
echo "================================================================"
echo "Installing Misc. Utilities"
echo "================================================================"

sudo apt-get install -y\
    clang-format\
    python-rosinstall\
    python-pip


echo "================================================================"
echo "Installing Project Dependent ROS packages."
echo "================================================================"

# Setup rosinstall
mkdir -p external_pkg
rosinstall external_pkg /opt/ros/kinetic .rosinstall
rosinstall . /opt/ros/kinetic

# Build external packages
catkin_make --source external_pkg

pip install virtualenv

virtualenv subbots_python
source /$CURR_DIR/subbots_python/bin/activate
pip freeze -r $CURR_DIR/requirements.txt --local



