#!/bin/bash

# The current directory
CURR_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#Error and exit if anything fails
set -e

echo "================================================================"
echo "Setup .bashrc"
echo "================================================================"
# Shell config files that various shells source when they run.
# This is where we want to add aliases, source ROS environment
# variables, etc.
SHELL_CONFIG_FILES=(
    "$HOME/.bashrc"\
            "$HOME/.zshrc"
    )

# All lines listed here will be added to the shell config files
# listed above, if they are not present already
declare -a new_shell_config_lines=(
    # Make sure that all shells know where to find our custom gazebo models,
    # plugins, and resources. Make sure to preserve the path that already exists as well
    "export PYTHONPATH=$PYTHONPATH:$CURR_DIR/models/research:$CURR_DIR/models/research/slim"
)

# Add all of our new shell config options to all the shell
# config files, but only if they don't already have them
for file_name in "${SHELL_CONFIG_FILES[@]}"; 
do
    echo "Setting up $file_name"
    for line in "${new_shell_config_lines[@]}"; 
    do
        if ! grep -Fq "$line" $file_name 
        then
            echo "$line" >> $file_name 
        fi
    done
done

#Installing python dependencies

sudo apt-get install -y virtualenv

virtualenv subbots_python
source $CURR_DIR/subbots_python/bin/activate
pip install -r $CURR_DIR/requirements.txt

wget -O protobuf.zip https://github.com/google/protobuf/releases/download/v3.0.0/protoc-3.0.0-linux-x86_64.zip
unzip -o protobuf.zip

./bin/protoc models/research/object_detection/protos/*.proto --python_out=models/research --proto_path=models/research

rm -r $CURR_DIR/protobuf.zip $CURR_DIR/bin $CURR_DIR/include $CURR_DIR/readme.txt

export PYTHONPATH=$PYTHONPATH:$CURR_DIR/models/research:$CURR_DIR/models/research/slim

wget https://www.dropbox.com/s/u2w40r3ye13us20/linux_v1.4.0.zip

unzip -o linux_v1.4.0.zip

rm -r linux_v1.4.0.zip

#Testing installation
python $CURR_DIR/models/research/object_detection/builders/model_builder_test.py
